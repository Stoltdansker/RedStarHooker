import time, os, fade, requests, colorama, ctypes, platform, socket, requests
from pystyle import Colors, Colorate, Center
from datetime import datetime
from colorama import Fore, Back




logo = f"""
                                                       , - ~ ~ ~ - ,
                                                   , '               ' ,
                                                 ,                       ,
                                                ,      █ █ █▀█ █ █▀▄      ,
                                               ,       ▀▄▀ █▄█ █ █▄▀       ,
                                               ,                           ,
                                               ,                           ,
                                                ,                         ,
                                                 ,                       ,
                                                   ,                  , '
                                                     ' - , _ _ _ ,  '
"""

logoc = f"""
                                                       , - ~ ~ ~ - ,
                                                   , '               ' ,
                                                 ,                       ,
                                                ,      █ █ █▀█ █ █▀▄      ,
                                               ,       ▀▄▀ █▄█ █ █▄▀       ,
                                               ,                           ,
                                               ,                           ,
                                                ,                         ,
                                                 ,                       ,
                                                   ,                  , '
                                                     ' - , _ _ _ ,  '
                                                 ╔═════╦════════════════╗
                                                ╔╣ [1] ║  Send Message  ╠╗
                                                ║║ [2] ║ Delete Webhook ║║
                                                ║║ [3] ║ Rename Webhook ║║
                                                ║║ [4] ║  Spam Webhook  ║║
                                                ║║ [5] ║     Discord    ║║
                                                ╚╣ [6] ║     Log Out    ╠╝
                                                 ╚╦════╩═══════════════╦╝
                                                  ║ feds.lol/Spermklat ║
                                                  ╚╦══════════════════╦╝
                                                   ╚══════════════════╝"""

def clear():
    if os.name == 'posix': # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt': # Windows
        os.system('cls')
    else:
        print("Unsupported operating system")
        raise SystemExit
    
def pause(text: str = None):
    if text: print(text)
    if os.name == 'posix': # Unix/Linux/MacOS
        os.system('read -n 1 -s -r -p ""')
    elif os.name == 'nt': # Windows
        os.system('pause >nul')
    else:
        print("Unsupported operating system")
        raise SystemExit

logofade = fade.pinkred(logo)
logocfade = fade.pinkred(logoc)



def randomshit():
    webhook_name = webhook["name"]
    titletext = f"Void Webhook | Logged into: {webhook_name} | Made by: Spermklat"
    clear()
    print(logocfade)
    ctypes.windll.kernel32.SetConsoleTitleW(titletext)

webhook = {}

def sendmessage(url):
    print(logofade)
    msg = input(f"{Colors.pink}╔═[{webhook_name}@Message] \n╚══> {Colors.white}")
    try:
        response = requests.post(url, json={"content": msg})
        response.raise_for_status()
        print(f"{Fore.GREEN}[ + ] {Fore.WHITE}Message sent.")
    except requests.exceptions.HTTPError as errh:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Request Exception: {err}")

def deletehook(url):
    print(logofade)
    try:
        response = requests.delete(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        print(f"{Fore.GREEN}[ + ]{Fore.WHITE} Webhook deleted")
        time.sleep(2)
    except requests.exceptions.HTTPError as errh:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Request Exception: {err}")

def renamehook(url):
    print(logofade)
    name = input(f"╔═[{webhook_name}@Name] \n╚══> ")
    try:
        response = requests.patch(url, json={"name": name})
        response.raise_for_status()
        print(f"{Fore.GREEN}[ + ]{Fore.WHITE} Webhook name changed.")
    except requests.exceptions.HTTPError as errh:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Request Exception: {err}")

def spamhook(url):
    print(logofade)
    msg = input(f"{Colors.pink}╔═[{webhook_name}@Message] \n╚══> {Colors.white}")
    timeout = float(input(f"{Colors.pink}╔═[{webhook_name}@Timeout] \n╚══> {Colors.white}"))
    try:
        while True:
            response = requests.post(url, json={"content": msg})
            response.raise_for_status()
            print(f"{Fore.GREEN}[ + ]{Fore.WHITE} {msg} sent.")
            time.sleep(timeout)
    except requests.exceptions.HTTPError as errh:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"{Fore.RED}[ - ]{Fore.WHITE} Request Exception: {err}")


while True:
    clear()
    while True:
        try:
            
            os.system("title ")
            print(logofade)
            url = input(f"{Colors.pink}╔═[User@Webhook] \n╚══> {Colors.white}")
            response = requests.get(url)
            if response.status_code == 200:
                webhook = response.json()
                break
            else:
                print(f"\n{Fore.RED}[ - ]{Back.RESET}{Fore.RESET} Invalid Webhook: {response.status_code}")
                time.sleep(3)    
                clear()
                break
        except Exception as e:
            if isinstance(e, KeyboardInterrupt):
                raise SystemExit
            print(f"\n{Fore.RED}[ - ]{Back.RESET}{Fore.RESET} Invalid Webhook")
            time.sleep(3)
            clear()
            break
    
    while True:
        randomshit()
        webhook_name = webhook["name"]
        ch = int(input(f"{Colors.pink}╔═[{webhook_name}@Choose] \n╚══> {Colors.white}"))
        if ch == 1:
            clear()
            sendmessage(url)
            pause("Press any key to return to menu...")
        elif ch == 2:
            clear()
            deletehook(url)
            break
        elif ch == 3:
            clear()
            renamehook(url)
            pause("Press any key to return to menu...")
        elif ch == 4:
            clear()
            spamhook(url)
            pause("Press any key to return to menu...")
        elif ch == 5:
            os.system("start \"\" https://discord.gg/Cas8Fj3P8t")
            pause("\nPress any key to return to menu...")
        elif ch == 6:
            os.system("title Logging out...")
            time.sleep(1.5)
            break
