import requests
import os
import platform
import socket
import psutil
import json

def get_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=5).text
    except requests.RequestException:
        return "Unavailable"

def get_system_info():
    try:
        user = os.getlogin()
    except OSError:
        user = os.environ.get("USERNAME", "Unknown")

    data = {
        "platform": platform.platform(),
        "hostname": socket.gethostname(),
        "cpu": platform.processor(),
        "ram": round(psutil.virtual_memory().total / (1024 ** 3)),
        "disk": round(psutil.disk_usage("/").total / (1024 ** 3)),
        "ip": get_ip(),
        "user": user,
    }
    return data

def save_system_info(filename="system_info.txt"):
    system_info = get_system_info()
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(system_info, file, indent=4)

if __name__ == "__main__":
    save_system_info()
