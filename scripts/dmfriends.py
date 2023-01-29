from scripts.settings import *

def massdmfriends():
    msgall = input(Colorate.Horizontal(Colors.cyan_to_blue, "Message » ", 1))

    massdmclient = discord.Client()

    class MassDM():
        @massdmclient.event
        async def on_connect():
            for user in massdmclient.user.friends:
                try:
                    await user.send(str(msgall))
                    textfarbe(f"* [Successfully] sent message to » [{user.name}]")
                except:
                    print(Colorate.Horizontal(Colors.rainbow, f"* [Failed] sent message to » [{user.name}]", 1))
                    
        @massdmclient.event
        async def on_ready():
            threads = 50
            for i in range(threads):
                thread = Thread(target=MassDM().on_connect).start()
                threads.append(thread)

        def Startup(self):
            massdmclient.run(token, bot=False)


    MassDM().Startup()