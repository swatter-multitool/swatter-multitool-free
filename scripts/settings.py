import os
import logging
import sys
import asyncio
import threading
import json
import webbrowser
from datetime import datetime 
import sys
from os.path import isfile, join
import fade
import colorama
import urllib
from capmonster_python import HCaptchaTask
from random import randint
import websocket
from colorama import Fore
import time              
import shutil
from tkinter import Tk
from discord_webhook import DiscordWebhook, DiscordEmbed
from tkinter.filedialog import askopenfilename
import psutil
import os
import re
import sys
import requests
from time import sleep
from colorama import Fore
from zipfile import ZipFile
from bs4 import BeautifulSoup
import random
import logging
import requests,os,discord,datetime,threading,sys
import json as js
import asyncio
from tasksio import TaskPool
from datetime import datetime
from aiohttp import ClientSession
import capmonster_python
import discum
import string
import time
import requests
import itertools, base64, concurrent.futures
from pystyle import *
import json
from threading import Thread
from itertools import cycle
import tkinter
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import threading, httpx, ctypes, requests, subprocess
import discord
from discord.ext import commands
import stdiomask
from itertools import count
import ctypes
import aiohttp, asyncio
import io, re
import zipfile
from bs4 import BeautifulSoup
from distutils.version import LooseVersion
from urllib.request import urlopen, urlretrieve
from multiprocessing.spawn import spawn_main
import discord 
import subprocess

hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
now = datetime.now()
zeit = now.strftime("%H:%M:%S")
google_target_ver = 0


developer = f'albaner#0069'


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }


def sumtokens():
    with open("tokens.txt") as f:
        count = sum(1 for _ in f)
        # tokensanzahl = print(str(count))
        # tokensanzahl = print(f"Token >> {Fore.LIGHTWHITE_EX}{str(count)}")
        tokenanzahl = str(count)
        return tokenanzahl

def sumproxies():
    with open("proxies.txt") as f:
        count = sum(1 for _ in f)
        # proxyanzahl = print(f"Proxy >> {Fore.LIGHTWHITE_EX}{str(count)}")
        proxyanzahl = str(count)
        return proxyanzahl


def albaner():
    albaner = f'''                                       .▄▄ · ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄▄▄▄▄▄▄▄▄▄▄ .▄▄▄  
                                       ▐█ ▀. ██· █▌▐█▐█ ▀█ •██  •██  ▀▄.▀·▀▄ █·
                                       ▄▀▀▀█▄██▪▐█▐▐▌▄█▀▀█  ▐█.▪ ▐█.▪▐▀▀▪▄▐▀▀▄ 
                                       ▐█▄▪▐█▐█▌██▐█▌▐█ ▪▐▌ ▐█▌· ▐█▌·▐█▄▄▌▐█•█▌
                                        ▀▀▀▀  ▀▀▀▀ ▀▪ ▀  ▀  ▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀
    '''
    return albaner

def shadow():
    shadow = f'''                                ███████╗██╗    ██╗ █████╗ ████████╗████████╗███████╗██████╗ 
                                ██╔════╝██║    ██║██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
                                ███████╗██║ █╗ ██║███████║   ██║      ██║   █████╗  ██████╔╝
                                ╚════██║██║███╗██║██╔══██║   ██║      ██║   ██╔══╝  ██╔══██╗
                                ███████║╚███╔███╔╝██║  ██║   ██║      ██║   ███████╗██║  ██║
                                ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝                                                     
    '''
    return shadow



def eyes():
    cateyes = f'''                                                   .::!!!!!!!:.
                  .!!!!!:.                        .:!!!!!!!!!!!!  
                  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$  
                      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P  Made by {developer}
                      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#   Discord Server: https://discord.gg/viertel
                      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
                      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
                        "*$bd$$$$      '*$$$$$$$$$$$o+#" 
                             """"          """""""
    '''
    return cateyes



def validateToken(token):
    base_url = "https://discord.com/api/v9/users/@me"
    message = "You need to verify your account in order to perform creepy action."

    r = requests.get(base_url, headers=getheaders(token))
    if r.status_code != 200:
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        sleep(1)
    j = requests.get(f'{base_url}/billing/subscriptions', headers=getheaders(token)).json()
    try:
        if j["message"] == message:
            print(f"\n{Fore.RED}Phone Locked Token!{Fore.RESET}")
            sleep(1)
    except:
        pass

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]


def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers


def setTitle(_str):
    ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")

def getTempDir():
    system = os.name
    if system == 'nt':
        #if its windows
        return os.getenv('temp')


def getTheme():
    themes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8"]
    with open(getTempDir()+"\\colors", 'r') as f:
        text = f.read()
        if not any(s in text for s in themes):
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid theme was given, Switching to default. . .')
            sleep(2.5)
            setTheme("bluered")
        return text

def setTheme(new: str):
    with open(getTempDir()+"\\colors", 'w'): 
        pass
    with open(getTempDir()+"\\colors", 'w') as f:
        f.write(new)

def setDesign(new: str):
    with open(getTempDir()+"\\design", 'w'): pass
    with open(getTempDir()+"\\design", 'w') as f:
        f.write(new)

def banner(theme=None):
    try:
        with open(getTempDir()+ "\\design", 'r') as f:
            thatdesign = f.read()
    except:
        with open(getTempDir() + "\\design", 'x') as yyy:
            fy = yyy.write('ghost')
            pass


    if thatdesign == "eyes":
        bannerTheme = eyes()

    elif thatdesign == "swatter":
        bannerTheme = albaner()

    elif thatdesign == "shadow":
        bannerTheme = shadow()
    
    else:
        bannerTheme = eyes()
    
    if theme == "blue":
        print(Fore.BLUE + bannerTheme)
    elif theme == "blueblack":
        print(Colorate.Horizontal(Colors.blue_to_black, bannerTheme, 1))
    elif theme == "bluecyan":
        print(Colorate.Horizontal(Colors.blue_to_cyan, bannerTheme, 1))
    elif theme == "bluegreen":
        print(Colorate.Horizontal(Colors.blue_to_green, bannerTheme, 1))
    elif theme == "bluepurple":
        print(Colorate.Horizontal(Colors.blue_to_purple, bannerTheme, 1))
    elif theme == "bluered":
        print(Colorate.Horizontal(Colors.blue_to_red, bannerTheme, 1))
    elif theme == "bluewhite":
        print(Colorate.Horizontal(Colors.blue_to_white, bannerTheme, 1))
    elif theme == "blackblue":
        print(Colorate.Horizontal(Colors.black_to_blue, bannerTheme, 1))
    elif theme == "blackgreen":
        print(Colorate.Horizontal(Colors.black_to_green, bannerTheme, 1))
    elif theme == "blackred":
        print(Colorate.Horizontal(Colors.black_to_red, bannerTheme, 1))
    elif theme == "blackwhite":
        print(Colorate.Horizontal(Colors.black_to_white, bannerTheme, 1))
    elif theme == "red":
        print(Fore.RED + bannerTheme)
    elif theme == "redblack":
        print(Colorate.Horizontal(Colors.red_to_black, bannerTheme, 1))
    elif theme == "redblue":
        print(Colorate.Horizontal(Colors.red_to_blue, bannerTheme, 1))
    elif theme == "redgreen":
        print(Colorate.Horizontal(Colors.red_to_green, bannerTheme, 1))
    elif theme == "redpurple":
        print(Colorate.Horizontal(Colors.red_to_purple, bannerTheme, 1))
    elif theme == "redwhite":
        print(Colorate.Horizontal(Colors.red_to_white, bannerTheme, 1))
    elif theme == "redyellow":
        print(Colorate.Horizontal(Colors.red_to_yellow, bannerTheme, 1))
    elif theme == "purpleblue":
        print(Colorate.Horizontal(Colors.purple_to_blue, bannerTheme, 1))
    elif theme == "purplered":
        print(Colorate.Horizontal(Colors.purple_to_red, bannerTheme, 1))
    elif theme == "rainbow":
        print(Colorate.Horizontal(Colors.rainbow, bannerTheme, 1))
    elif theme == "yellowgreen":
        print(Colorate.Horizontal(Colors.yellow_to_green, bannerTheme, 1))
    elif theme == "green":
        print(Fore.GREEN + bannerTheme)
    elif theme == "greenblue":
        print(Colorate.Horizontal(Colors.green_to_blue, bannerTheme, 1))
    elif theme == "greencyan":
        print(Colorate.Horizontal(Colors.green_to_cyan, bannerTheme, 1))
    elif theme == "greenred":
        print(Colorate.Horizontal(Colors.green_to_red, bannerTheme, 1))
    elif theme == "greenwhite":
        print(Colorate.Horizontal(Colors.green_to_white, bannerTheme, 1))
    elif theme == "greenyellow":
        print(Colorate.Horizontal(Colors.green_to_yellow, bannerTheme, 1))
    elif theme == "greenblack":
        print(Colorate.Horizontal(Colors.green_to_black, bannerTheme, 1))
    elif theme == "cyanblue":
        print(Colorate.Horizontal(Colors.cyan_to_blue, bannerTheme, 1))
    elif theme == "cyangreen":
        print(Colorate.Horizontal(Colors.cyan_to_green, bannerTheme, 1))
    elif theme == "yellowred":
        print(Colorate.Horizontal(Colors.yellow_to_red, bannerTheme, 1))
    elif theme == "reset":
        print(Fore.RESET + bannerTheme)

    else:
        print(Colorate.Horizontal(Colors.rainbow, bannerTheme, 1))

def textfarbe(new: str):
    if getTheme() == "blue":
        print(Fore.BLUE + new)
    elif getTheme() == "blueblack":
        print(Colorate.Horizontal(Colors.blue_to_black, new, 1))
    elif getTheme() == "bluecyan":
        print(Colorate.Horizontal(Colors.blue_to_cyan, new, 1))
    elif getTheme() == "bluegreen":
        print(Colorate.Horizontal(Colors.blue_to_green, new, 1))
    elif getTheme() == "bluepurple":
        print(Colorate.Horizontal(Colors.blue_to_purple, new, 1))
    elif getTheme() == "bluered":
        print(Colorate.Horizontal(Colors.blue_to_red, new, 1))
    elif getTheme() == "bluewhite":
        print(Colorate.Horizontal(Colors.blue_to_white, new, 1))
    elif getTheme() == "blackblue":
        print(Colorate.Horizontal(Colors.black_to_blue, new, 1))
    elif getTheme() == "blackgreen":
        print(Colorate.Horizontal(Colors.black_to_green, new, 1))
    elif getTheme() == "blackred":
        print(Colorate.Horizontal(Colors.black_to_red, new, 1))
    elif getTheme() == "blackwhite":
        print(Colorate.Horizontal(Colors.black_to_white, new, 1))
    elif getTheme() == "red":
        print(Fore.RED + new)
    elif getTheme() == "redblack":
        print(Colorate.Horizontal(Colors.red_to_black, new, 1))
    elif getTheme() == "redblue":
        print(Colorate.Horizontal(Colors.red_to_blue, new, 1))
    elif getTheme() == "redgreen":
        print(Colorate.Horizontal(Colors.red_to_green, new, 1))
    elif getTheme() == "redpurple":
        print(Colorate.Horizontal(Colors.red_to_purple, new, 1))
    elif getTheme() == "redwhite":
        print(Colorate.Horizontal(Colors.red_to_white, new, 1))
    elif getTheme() == "redyellow":
        print(Colorate.Horizontal(Colors.red_to_yellow, new, 1))
    elif getTheme() == "purpleblue":
        print(Colorate.Horizontal(Colors.purple_to_blue, new, 1))
    elif getTheme() == "purplered":
        print(Colorate.Horizontal(Colors.purple_to_red, new, 1))
    elif getTheme() == "rainbow":
        print(Colorate.Horizontal(Colors.rainbow, new, 1))
    elif getTheme() == "yellowgreen":
        print(Colorate.Horizontal(Colors.yellow_to_green, new, 1))
    elif getTheme() == "green":
        print(Fore.GREEN + new)
    elif getTheme() == "greenblue":
        print(Colorate.Horizontal(Colors.green_to_blue, new, 1))
    elif getTheme() == "greencyan":
        print(Colorate.Horizontal(Colors.green_to_cyan, new, 1))
    elif getTheme() == "greenred":
        print(Colorate.Horizontal(Colors.green_to_red, new, 1))
    elif getTheme() == "greenwhite":
        print(Colorate.Horizontal(Colors.green_to_white, new, 1))
    elif getTheme() == "greenyellow":
        print(Colorate.Horizontal(Colors.green_to_yellow, new, 1))
    elif getTheme() == "greenblack":
        print(Colorate.Horizontal(Colors.green_to_black, new, 1))
    elif getTheme() == "cyanblue":
        print(Colorate.Horizontal(Colors.cyan_to_blue, new, 1))
    elif getTheme() == "cyangreen":
        print(Colorate.Horizontal(Colors.cyan_to_green, new, 1))
    elif getTheme() == "yellowred":
        print(Colorate.Horizontal(Colors.yellow_to_red, new, 1))
    elif getTheme() == "8":
        print(Fore.RESET + new)


class Chrome_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://chromedriver.storage.googleapis.com/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if google_target_ver:
            self.target_version = google_target_ver

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = base_ = "chromedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_chromedriver()
            if not self.__class__.installed:
                if self.patch_binary():
                    self.__class__.installed = True

    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open(self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect

    def get_release_version_number(self):
        path = (
            "LATEST_RELEASE"
            if not self.target_version
            else f"LATEST_RELEASE_{self.target_version}"
        )
        return LooseVersion(urlopen(self.__class__.DL_BASE + path).read().decode())

    def fetch_chromedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract(self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name


def getDriver():
    drivers = ["chromedriver.exe"]
    Write.Print("\nChecking Downloaded Drivers!", Colors.purple_to_blue, interval=0.015)
    sleep(0.5)
    for driver in drivers:
        if os.path.exists(os.getcwd() + os.sep + driver):
            Write.Print("\nChromeDriver is Already Installed...", Colors.purple_to_blue, interval=0.015)
            sleep(0.5)
            return driver
    else:
        Write.Print("\nInstalling Drivers!\n\n", Colors.purple_to_blue, interval=0.015)
        if os.path.exists(os.getenv('localappdata') + '\\Google'):
            Chrome_Installer()
            Write.Print("\nChromeDriver.exe Has Been Installed Successfully!", Colors.purple_to_blue, interval=0.015)
            return "chromedriver.exe"

        else:
            Write.Print("\nERROR | No Compatible Driver Found... Proceeding with ChromeDriver!\n\n", Colors.purple_to_blue, interval=0.015)
            Chrome_Installer()
            Write.Print("\nTrying ChromeDriver.exe\n\n", Colors.purple_to_blue, interval=0.015)
            return "chromedriver.exe"
