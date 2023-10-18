from modules.modules import Modules
from utils.utils import Utils
from colorama import Fore, Style, init
from urllib.parse import urlparse
from pystyle import Write, System, Colors, Colorate
import os, sys, time as tm, json, random, string, ctypes, threading, concurrent.futures

init(autoreset=True)

def tool():
    line = f"{Fore.LIGHTCYAN_EX}={Fore.LIGHTBLUE_EX}={Fore.BLUE}=" * 40
    Utils.update_title("Menu")
    System.Clear()
    print(f"""
{Fore.LIGHTCYAN_EX}\t\t\t\t\t╔═╗╦╔╦╗╦ ╦╦ ╦╔╗   ╔╦╗╦ ╦╦ ╔╦╗╦  ╔╦╗╔═╗╔═╗╦  
{Fore.LIGHTBLUE_EX}\t\t\t\t\t║ ╦║ ║ ╠═╣║ ║╠╩╗  ║║║║ ║║  ║ ║   ║ ║ ║║ ║║  
{Fore.BLUE}\t\t\t\t\t╚═╝╩ ╩ ╩ ╩╚═╝╚═╝  ╩ ╩╚═╝╩═╝╩ ╩   ╩ ╚═╝╚═╝╩═╝

{line}
\t\t\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}1{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Token Checker\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}8{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Repository Update Boost
\t\t\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}2{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Issue Creator\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}9{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Star Adder
\t\t\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}3{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Repository Fork\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}10{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Star Deleter
\t\t\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}4{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Profile View Booster\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}11{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}GitHub String Scraper
\t\t\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}5{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Repository Flooder\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}12{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Topic Finder
\t\t\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}6{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Issue Closer\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}13{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Project Flooder
\t\t\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}7{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Repository Deleter\t\t{Fore.LIGHTCYAN_EX}({Fore.BLUE}>>{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Next Page
{line}
""")
    Write.Print("""
┌──(Github@Multi-Tool) ~ [Ϟ]
|
└─> """, Colors.blue_to_cyan, interval=0.000); opc = input(Fore.CYAN)
    if opc == "1":
        print()
        Utils.update_title("Token Checker")
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.token_checker, args=(token,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        
        Write.Print("""
┌──(Github@Multi-Tool) ~ [Ϟ]
| Press ENTER
└─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()
    elif opc == "2":
        Utils.update_title("Issue Creator")
        owner = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Repository Owner ~>{Fore.RESET} ")
        name = input(f"{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Repository Name ~>{Fore.RESET} ")
        issue_title = input(f"{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Issue Title ~>{Fore.RESET} ")
        issue_body = input(f"{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Issue Message ~>{Fore.RESET} ")
        print()
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.issue_creator, args=(owner, name, token, issue_title, issue_body))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        Write.Print("""
┌──(Github@Multi-Tool) ~ [Ϟ]
| Press ENTER
└─> """, Colors.blue_to_cyan, interval=0.000)
        input(Fore.CYAN)
        tool()
    elif opc == "3":
        Utils.update_title("Repository Fork")
        url = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Repository URL ~>{Fore.RESET} ")
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.repo_fork, args=(token, url,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        
        Write.Print("""
┌──(Github@Multi-Tool) ~ [Ϟ]
| Press ENTER
└─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()
    elif opc == "4":
        Utils.update_title("Profile View Booster")
        Modules.get_proxies()
        camo_url = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Camo URL ~>{Fore.RESET} ")
        print()
        for i in range(50):
            threading.Thread(target=Modules.view_booster,args=(camo_url,)).start()

        Write.Print("""
┌──(Github@Multi-Tool) ~ [Ϟ]
| Press ENTER
└─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()
        
    elif opc == "5":
        Utils.update_title("Repository Flooder")
        name = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Name ~>{Fore.RESET} ")
        description = input(f"{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Description ~>{Fore.RESET} ")
        howmany = input(f"{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}How Many Repos ~>{Fore.RESET} ")
        print()
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.repository_flooder, args=(token, name, description, howmany,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        Write.Print("""
┌──(Github@Multi-Tool) ~ [Ϟ]
| Press ENTER
└─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()
        
    elif opc == "6":
        Utils.update_title("Issue Closer")
        owner = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Repository Owner ~>{Fore.RESET} ")
        name = input(f"{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Repository Name ~>{Fore.RESET} ")
        issue_range = input(f"{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Issue Range (Example, 1 or 7,12) ~>{Fore.RESET} ")
        print()
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.issue_closer, args=(owner, name, token, issue_range))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        Write.Print("""
┌──(Github@Multi-Tool) ~ [Ϟ]
| Press ENTER
└─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()
    elif opc == "7":
        Utils.update_title("Repository Deleter")
        print()
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.repository_deleter, args=(token,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        
        Write.Print("""
┌──(Github@Multi-Tool) ~ [Ϟ]
| Press ENTER
└─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()
    elif opc == "8":
        Utils.update_title("Repository Update Boost")
        url = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Repository URL ~>{Fore.RESET} ")
        parsed_url = urlparse(url)
        needed = parsed_url.path.strip('/')
        repo_url = f"https://api.github.com/repos/{needed}"
        print()
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.repository_update_booster, args=(repo_url, token,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        
        Write.Print("""
┌──(Github@Multi-Tool) ~ [Ϟ]
| Press ENTER
└─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()
    elif opc == "9":
        Utils.update_title("Star Botter")
        urls = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Enter URLs (link,link2) ~>{Fore.RESET} ").split(',')
        print()
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.star_add, args=(token, urls,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        Write.Print("""
    ┌──(Github@Multi-Tool) ~ [Ϟ]
    | Press ENTER
    └─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()

    elif opc == "10":
        Utils.update_title("Star Deleter")
        urls = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Enter URLs (link,link2) ~>{Fore.RESET} ").split(',')
        print()
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.star_delete, args=(token, urls,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        Write.Print("""
    ┌──(Github@Multi-Tool) ~ [Ϟ]
    | Press ENTER
    └─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()
    elif opc == "11":
        Utils.update_title("GitHub String Scraper")
        search = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Enter string to search on GitHub ~>{Fore.RESET} ")
        print()
        Modules.string_find(search)

        Write.Print("""
    ┌──(Github@Multi-Tool) ~ [Ϟ]
    | Press ENTER
    └─> """, Colors.blue_to_cyan, interval=0.000)
        tool()
    elif opc == "12":
        Utils.update_title("Topic Finder")
        topic = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Topic ~>{Fore.RESET} ")
        print()
        Modules.search_topic(topic)

        Write.Print("""
    ┌──(Github@Multi-Tool) ~ [Ϟ]
    | Press ENTER
    └─> """, Colors.blue_to_cyan, interval=0.000)
        tool()

    elif opc == "13":
        Utils.update_title("Project Flooder")
        url = input(f"\n{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Repository URL ~>{Fore.RESET} ")
        parsed_url = urlparse(url)
        needed = parsed_url.path.strip('/')
        repo_url = f"https://api.github.com/repos/{needed}/projects"
        howmany = input(int(f"{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}How Many ~>{Fore.RESET} "))
        title = input(f"{Fore.CYAN}({Fore.BLUE}>{Fore.CYAN}) {Fore.LIGHTBLUE_EX}Title ~>{Fore.RESET} ")
        print()
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        threads = []
        for token in tokens:
            thread = threading.Thread(target=Modules.project_flooder, args=(token, repo_url, title,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        Write.Print("""
    ┌──(Github@Multi-Tool) ~ [Ϟ]
    | Press ENTER
    └─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
        tool()
    else:
        tool() 
if __name__ == "__main__":
    tool()
