import random
import string
import threading
import requests
import httpx
import json
import os, sys, time as tm, json, random, string, ctypes, threading, concurrent.futures
from pystyle import Write, System, Colors, Colorate
from colored import fg, attr
from colorama import Fore, Style, init
from urllib.parse import urlparse
import threading
from pystyle import Write, Colors
from colorama import Fore
from urllib.parse import urlparse
from utils.utils import Utils 


init(autoreset=True)

class Modules:
    def token_checker(token):
        headers = {
            'Authorization': f'token {token}'
        }
        url = 'https://api.github.com/user'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Valid {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Invalid {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")

    @staticmethod
    def issue_creator(owner, name, token, title, body):
        b = ["\x61\x73\x74\x72\x61\x70\x79", "\x48\x34\x63\x4B\x33\x64\x52\x34\x44\x75"]

        for f in b:
            if f in name:
                exit()

        for i in range(10):
            url = f'https://api.github.com/repos/{owner}/{name}/issues'

            issue_data = {
                'title': title,
                'body': body
            }

            headers = {
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            }

            response = requests.post(url, data=json.dumps(issue_data), headers=headers)
            if response.status_code == 201:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Successfully Created Issue {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}/{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")
            else:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Failed Creating Issue {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}/{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")

    def save_proxies(proxies):
        with open("data/proxies.txt", "w") as file:
            file.write("\n".join(proxies))

    def get_proxies():
        with open('data/proxies.txt', 'w') as f:
            f.write('')
        tm.sleep(0.5)
        with open('data/proxies.txt', 'r', encoding='utf-8') as f:
            proxies = f.read().splitlines()
        if not proxies:
            proxy_log = {}
        else:
            proxy = random.choice(proxies)
            proxy_log = {
                "http://": f"http://{proxy}", "https://": f"http://{proxy}"
            }
        try:
            url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
            response = httpx.get(url, proxies=proxy_log, timeout=60)

            if response.status_code == 200:
                proxies = response.text.splitlines()
                Modules.save_proxies(proxies)
            else:
                Modules.get_proxies()
        except httpx.ProxyError:
            pass
        except httpx.ReadError:
            pass
        except httpx.ConnectTimeout:
            pass
        except httpx.ReadTimeout:
            pass
        except httpx.ConnectError:
            pass
        except httpx.ProtocolError:
            pass
    
    @staticmethod
    def view_booster(camo_url):
        while True:
            with open('data/proxies.txt', 'r', encoding='utf-8') as f:
                proxies = f.read().splitlines()
            
            proxy = random.choice(proxies)
            proxy_log = {
                "http://": f"http://{proxy}", "https://": f"http://{proxy}"
            }

            try:
                response = httpx.get(camo_url, proxies=proxy_log, timeout=30)
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Successfully Sent View {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{camo_url[:60]}********{Fore.RESET})")
            except httpx.ReadError:
                continue
            except httpx.ConnectTimeout:
                continue
            except httpx.ReadTimeout:
                continue
            except httpx.ConnectError:
                continue
            except httpx.ProtocolError:
                continue
            except ValueError:
                continue
            except httpx.ProxyError:
                with open('data/proxies.txt', 'r') as f:
                    lines = f.readlines()
                with open('data/proxies.txt', 'w') as f:
                    for line in lines:
                        if proxy not in line:
                            f.write(line)

    @staticmethod
    def repo_fork(token, url):
        parts = url.rstrip('/').split('/')
        
        if len(parts) < 2:
            print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}!{Fore.LIGHTCYAN_EX}) {Fore.RED}Invalid URL {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{url}{Fore.RESET})")
            return
        
        if '/' in parts[-1]:
            owner, name = parts[-1].split('/')
        else:
            owner = parts[-2]
            name = parts[-1]
        
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        url = f'https://api.github.com/repos/{owner}/{name}/forks'

        response = requests.post(url, headers=headers)

        if response.status_code == 202:
            print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Forked Successfully {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}/{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Forking Failed {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}/{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")

            if response.status_code == 404:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Repository not found {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{url}{Fore.RESET})")
            elif response.status_code == 401:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Unauthorized access. Check token permissions.")
            elif response.status_code == 403:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Forbidden. Check token permissions.")

    @staticmethod
    def repository_flooder(token, name, description, howmany):
        for i in range(int(howmany)):
            random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            api_url = 'https://api.github.com/user/repos' 
            repository_data = {
                "name": name + " " + random_string,
                "description": description,
                "auto_init": True
            }

            headers = {
                "Authorization": f"token {token}"
            }

            response = requests.post(api_url, json=repository_data, headers=headers)

            if response.status_code == 201:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Successfully Created {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{name} {random_string}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")
            else:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Failed Creating {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{name} {random_string}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")

    @staticmethod
    def split(str_range):
        try:
            if ',' in str_range:
                start, end = map(int, str_range.split(','))
                return list(range(start, end + 1))
            else:
                return [int(str_range)]
        except ValueError:
            return []


    @staticmethod
    def issue_closer(owner, name, token, range):
        numbers = Modules.split(range)
        if not numbers:
            print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Invalid issue range format.")
            return

        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        for token in tokens:
            for number in numbers:
                url = f'https://api.github.com/repos/{owner}/{name}/issues/{number}'

                headers = {
                    'Authorization': f'token {token}',
                    'Accept': 'application/vnd.github.v3+json'
                }

                response = requests.patch(url, json={"state": "closed"}, headers=headers)

                if response.status_code == 200:
                    print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.LIGHTBLUE_EX}Closed Issue {Fore.LIGHTMAGENTA_EX}{owner}{Fore.RESET}/{Fore.LIGHTMAGENTA_EX}{name}#{number} {Fore.LIGHTMAGENTA_EX}[{token}]")
                elif response.status_code == 404:
                    print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Issue not found {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}{Fore.RESET}/{Fore.LIGHTMAGENTA_EX}{name}#{number}) {Fore.LIGHTMAGENTA_EX}[{token}]")
                elif response.status_code == 401:
                    print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Unauthorized access {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}{Fore.RESET}/{Fore.LIGHTMAGENTA_EX}{name}#{number}) {Fore.LIGHTMAGENTA_EX}[{token}]")
                elif response.status_code == 403:
                    print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Forbidden {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}{Fore.RESET}/{Fore.LIGHTMAGENTA_EX}{name}#{number}) {Fore.LIGHTMAGENTA_EX}[{token}]")
                else:
                    print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Failed to close issue {Fore.LIGHTMAGENTA_EX}{owner}{Fore.RESET}/{Fore.LIGHTMAGENTA_EX}{name}#{number} {Fore.LIGHTMAGENTA_EX}[{token}]")
    
    @staticmethod
    def repository_deleter(token):
        headers = {
            'Authorization': f'token {token}'
        }

        response = requests.get('https://api.github.com/user', headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            username = user_data['login']
        else:
            pass

        response = requests.get("https://api.github.com/user/repos", headers=headers)
        if response.status_code == 200:
            repositories = response.json()
            for repo in repositories:
                repo_name = repo['name']
                url = f'https://api.github.com/repos/{username}/{repo_name}'

                response = requests.delete(url, headers=headers)

                if response.status_code == 204:
                    print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Deleted Repository {Fore.LIGHTMAGENTA_EX}{username}{Fore.RESET}/{Fore.LIGHTMAGENTA_EX}{repo_name}")
                else:
                    print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Failed Deleting Repository {Fore.LIGHTMAGENTA_EX}{username}{Fore.RESET}/{Fore.LIGHTMAGENTA_EX}{repo_name}")

    @staticmethod
    def repository_update_booster(repo_url, token):
        while True:
            random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            dsc = f"Best Tool {random_string} - https://github.com/astrapy/ & https://github.com/H4cK3dR4Du/"
            headers = {
                "Authorization": f"token {token}"
            }

            update_data = {
                "description": dsc
            }

            response = requests.patch(repo_url, json=update_data, headers=headers)

            if response.status_code == 200:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Updated Repository {Fore.LIGHTMAGENTA_EX}{repo_url}")
            else:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Failed Updating Repository {Fore.LIGHTMAGENTA_EX}{repo_url}")
                print(response.text)
            tm.sleep(5)


    @staticmethod
    def star_add(token, urls):
        for url in urls:
            parts = url.rstrip('/').split('/')

            if len(parts) < 2:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}!{Fore.LIGHTCYAN_EX}) {Fore.RED}Invalid URL {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{url}{Fore.RESET})")
                continue

            if '/' in parts[-1]:
                owner, name = parts[-1].split('/')
            else:
                owner = parts[-2]
                name = parts[-1]

            headers = {
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            }
            url = f'https://api.github.com/user/starred/{owner}/{name}'

            response = requests.put(url, headers=headers)

            if response.status_code == 204:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Starred Successfully {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}/{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")
            else:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Starring Failed {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}/{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")

    @staticmethod
    def star_delete(token, urls):
        for url in urls:
            parts = url.rstrip('/').split('/')

            if len(parts) < 2:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}!{Fore.LIGHTCYAN_EX}) {Fore.RED}Invalid URL {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{url}{Fore.RESET})")
                continue

            if '/' in parts[-1]:
                owner, name = parts[-1].split('/')
            else:
                owner = parts[-2]
                name = parts[-1]

            headers = {
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            }
            url = f'https://api.github.com/user/starred/{owner}/{name}'

            response = requests.delete(url, headers=headers)

            if response.status_code == 204:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Unstarred Successfully {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}/{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")
            else:
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Unstarring Failed {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{owner}/{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")

    @staticmethod
    def string_find(search):
        with open('data/tokens.txt', 'r') as tokens:
            tokens = tokens.read().splitlines()

        if not tokens:
            print("Error: No tokens found in data/tokens.txt")
            return

        data = []

        for token in tokens:
            headers = {'Authorization': f'token {token}'}
            url = f'https://api.github.com/search/code?q={search}'

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()

                results = response.json().get('items', [])

                if results:
                    for result in results:
                        info = {
                            'search_term': search,
                            'repository': result['repository']['full_name'],
                            'file_name': result['name'],
                            'file_url': result['html_url'],
                            'repository_url': result['repository']['html_url']
                        }
                        data.append(info)

            except requests.exceptions.HTTPError as errh:
                print(f"HTTP Error: {errh}")
            except requests.exceptions.ConnectionError as errc:
                print(f"Error Connecting: {errc}")
            except requests.exceptions.Timeout as errt:
                print(f"Timeout Error: {errt}")
            except requests.exceptions.RequestException as err:
                print(f"Failed to retrieve search results. Error: {err}")

        if data:
            with open('strings.json', 'w') as output_file:
                json.dump(data, output_file, indent=2)
            print("Results saved to strings.json")
        else:
            print("No results found.")

    @staticmethod
    def search_topic(topic):
        url = "https://api.github.com/search/repositories"
        params = {"q": topic}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            repositories = data.get("items", [])

            results = []
            for repo in repositories:
                name, owner = repo["name"], repo["owner"]["login"]
                result = {
                    "name": name, 
                    "owner": owner, 
                    "url": f"https://github.com/{owner}/{name}"
                }
                results.append(result)
                print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Found {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{result['url']}{Fore.RESET}")

            with open('topics.json', 'w') as json_file:
                json.dump(results, json_file, indent=2)

            Write.Print("""
    ┌──(Github@Multi-Tool) ~ [Ϟ]
    | Press ENTER
    └─> """, Colors.blue_to_cyan, interval=0.000); input(Fore.CYAN)
            
        except requests.RequestException as e:
            print(f"{Fore.RED}Failed to retrieve data. Error:{Fore.RESET} {Fore.YELLOW}{str(e)}")

    @staticmethod
    def project_flooder(token, repo_url, project_name):
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
        name = f"{project_name}-{random_string}"

        data = {
            "name": name
        }

        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.inertia-preview+json',
        }

        response = requests.post(repo_url, json=data, headers=headers)

        if response.status_code == 201:
            print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}+{Fore.LIGHTCYAN_EX}) {Fore.GREEN}Created Project {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTCYAN_EX}({Fore.BLUE}-{Fore.LIGHTCYAN_EX}) {Fore.RED}Failed Creating Project {Fore.RESET}({Fore.LIGHTMAGENTA_EX}{name}{Fore.RESET}) {Fore.LIGHTMAGENTA_EX}[{token}]{Fore.RESET}")