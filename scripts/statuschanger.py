from scripts.settings import *


def statusch():
    print(Colorate.Horizontal(Colors.rainbow, f"{zeit} » Proxy » Choose your File"))
    time.sleep(1)
    proxyfile = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files!", ".")), title="Please chose your Proxy List!")
    proxies = cycle(open(proxyfile, "r").read().splitlines())
    print("")
    print("")

    xyz_config = json.load(open("config.json", "r", encoding="utf-8"))


    proxy = "http://" + next(proxies) if xyz_config["proxy"] == True else None
    session = httpx.Client(proxies=proxy)
    version = cycle(['v10', 'v9'])

    statue_number = int(input(Colorate.Horizontal(Colors.yellow_to_green, f"{zeit} » Status changing » number » ", 1)))
    times = int(3)

    statues = []

    headers = {'Authorization': token, 'Content-Type': 'application/json'}

    if statue_number >= 1 and statue_number <= 9999:
        for loop in range(0, statue_number):
            print(Colorate.Horizontal(Colors.cyan_to_green, f"Custom Status » {loop+1}", 1))
            choice = str(input(Colorate.Horizontal(Colors.cyan_to_blue, f"Message » ", 1)))
            statues.append(choice)
    else:
        input(f"Get back to menu")

    while True:
        for i in range(len(statues)):
            CustomStatus = {"custom_status": {"text": statues[i]}}
            try:
                session.patch(f"https://discord.com/api/{next(version)}/users/@me/settings", headers=headers, json=CustomStatus)
                print(f"{Fore.LIGHTCYAN_EX}[{Fore.GREEN}SUCCESS{Fore.LIGHTCYAN_EX}][{Fore.LIGHTWHITE_EX}{zeit}{Fore.LIGHTCYAN_EX}] » [{Fore.LIGHTWHITE_EX}EZ{Fore.LIGHTCYAN_EX}] {Fore.LIGHTWHITE_EX}Status: {Fore.LIGHTCYAN_EX}{statues[i]} {Fore.LIGHTWHITE_EX}changed")
                i += 1
                setTitle(f"{zeit} » Status » changed {i}")
                time.sleep(times)
            except Exception as e:
                print(f"{Fore.LIGHTCYAN_EX}[{Fore.RED}FAILED{Fore.LIGHTCYAN_EX}][{Fore.LIGHTWHITE_EX}{zeit}{Fore.LIGHTCYAN_EX}] » [{Fore.LIGHTWHITE_EX}GG{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Status: {Fore.LIGHTCYAN_EX}{statues[i]} {Fore.LIGHTRED_EX}error")
                time.sleep(times)
