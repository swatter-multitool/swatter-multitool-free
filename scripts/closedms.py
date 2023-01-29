from scripts.settings import *

class closedirectmessages:
    def __init__(self):
        proxyfile = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files!", ".")), title="Please chose your Proxy List!")
        proxies = cycle(open(proxyfile, "r").read().splitlines())
        xyz_config = json.load(open("config.json", "r", encoding="utf-8"))
        
        self.proxy = "http://" + next(proxies) if xyz_config["proxy"] == True else None
        self.session = httpx.Client(proxies=self.proxy)
        self.version = cycle(['v10', 'v9'])

    def closedms(self):
        close_dm_request = self.session.get(f"https://canary.discord.com/api/v8/users/@me/channels", headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}).json()
        for channel in close_dm_request:
            print(f"{Fore.LIGHTCYAN_EX}[{Fore.GREEN}SUCCESS{Fore.LIGHTCYAN_EX}][{Fore.LIGHTWHITE_EX}{zeit}{Fore.LIGHTCYAN_EX}] » [{Fore.LIGHTWHITE_EX}GC{Fore.LIGHTCYAN_EX}] {Fore.LIGHTWHITE_EX}Groupchat: {Fore.LIGHTCYAN_EX}{channel['id']} {Fore.LIGHTWHITE_EX}left")
            requests.delete(f"https://canary.discord.com/api/v8/channels/{channel['id']}", headers={"authorization": token, "user-agent": "Samsung Fridge/6.9"})
            
    def menu(self):
        t = threading.Thread(target=self.closedms)
        t.start()
        while threading.active_count() >= threads:
            t.join()
                
        time.sleep(1.5)
        self.menu()