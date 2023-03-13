import os
import sys

def install():
    os.system('pip install colorama requests')
    
try:
    import colorama, requests
except:
    req = input("[+] Do you want to install requirements?[Y/n]: ")
    
    if req == 'Y' or req == 'y':
        install()
    elif req == 'N' or req == 'n':
        sys.exit()

from requests import get
from colorama import Fore

GREEN = Fore.LIGHTGREEN_EX
RED = Fore.RED
WHITE = Fore.WHITE
CYAN = Fore.CYAN
RESET = Fore.RESET

banner = f'''{CYAN}
 _       __     __    ______
| |     / /__  / /_  / ____/___  _____________  _____
| | /| / / _ \/ __ \/ /_  / __ \/ ___/ ___/ _ \/ ___/
| |/ |/ /  __/ /_/ / __/ / /_/ / /  / /__/  __/ /
|__/|__/\___/_.___/_/    \____/_/   \___/\___/_/
{WHITE}                                 Author: Saminium01
'''
print(banner)

try:
    domain = sys.argv[1]
except:
    print(f"{WHITE} \n\t Usage: python WebForcer.py www.example.com\n")
    sys.exit()
    
url_file = open('wordlist.txt')

print("Status Code         URL")
print("-" * 60)

for url in url_file:
    try:
        url = url.strip("\n")
        full_address = domain + "/" + url
        response = get('http://' + full_address)
        code = response.status_code
        print(f"{WHITE} {code}                 http://{full_address}")
    
    except requests.ConnectionError:
        print(f"{RED}\n [ERROR] Check Your Internet Connection or Domain \n")
        print(RESET)
        sys.exit()
    
    except KeyboardInterrupt:
        print(f"{RED}\n [ERROR] Process Interrupted \n")
        print(RESET)
        sys.exit()
    
print(RESET)
sys.exit()