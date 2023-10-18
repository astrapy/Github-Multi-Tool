import os
import json
import requests
import datetime
from pystyle import Write, System, Colors
from colored import fg, attr
from colorama import Fore, Style, init
from urllib.parse import urlparse
import ctypes

init(autoreset=True)

class Utils:
    def update_title(module):
        tokens = len(open('data/tokens.txt').readlines())
        ctypes.windll.kernel32.SetConsoleTitleW(f'Github Multi Tool - Made By Radu & Astra - Module : {module} | Tokens : {tokens} | https://github.com/H4cK3dR4Du & https://github.com/astrapy')

    def get_time():
        return datetime.datetime.now().strftime('%H:%M:%S')
