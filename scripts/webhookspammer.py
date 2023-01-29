from scripts.settings import *

def whspammer():
    session = requests.Session()
    web = input(Colorate.Horizontal(Colors.purple_to_blue, f"{zeit} » Webhook » "))
    spam = input(Colorate.Horizontal(Colors.purple_to_red, f"{zeit} » Message » "))

    rando=[f"albaner#8002", "Swatter Tool"]

    avatars = cycle(["https://media.discordapp.net/attachments/1059643853046554697/1060478546885214279/tool_design.png", "https://cdn.discordapp.com/attachments/1059643853046554697/1060480692556931122/IMG_6554.png"])
    print("")
    print("")
    print(Colorate.Horizontal(Colors.red_to_blue, f"{zeit} » Proxy » Choose your List"))
    time.sleep(1)
    proxyfile = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files!", ".")), title="Please chose your Proxy List!")
    try:
        with open(proxyfile, 'r') as lol:
            proxieees = lol.readlines()
            for x in proxieees:
                proxies = x.rstrip()
    except:
        pass

    def ehook(webhook):
        proxy = cycle(proxies)
        einfo={
            'username': random.choice(rando),
            'content': spam,
            "avatar_url": next(avatars)
        }
        
        r = session.post(webhook, json=einfo, proxies={"http": 'http://' + next(proxy)})

        if r.status_code == 204:
            print(Colorate.Horizontal(Colors.cyan_to_green, f"{zeit} » Webhook » {spam} sent"))
        else:
            print(Colorate.Horizontal(Colors.red_to_blue, f"{zeit} » Webhook » {spam} can't sent"))

    while True:
        threading.Thread(target=ehook, args=(web,)).start()