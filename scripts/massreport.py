from scripts.settings import *

def massrep():
    tkk = input(Colorate.Horizontal(Colors.purple_to_red, f"[Token] > "))

    class massreport:
        def __init__(self):
            self.GUILD_ID = str(input(Colorate.Horizontal(Colors.rainbow, f"[Guild ID] > ")))
            self.CHANNEL_ID = str(input(Colorate.Horizontal(Colors.cyan_to_green, f"[Channel ID] > ")))
            self.MESSAGE_ID = str(input(Colorate.Horizontal(Colors.cyan_to_blue, f"[Message ID] > ")))

            reportgründe = f'''
            [1 - Illegal content]
            [2 - Harassment]
            [3 - Spam or grabbing/phishing Links]
            [4 - Self-harm]
            [5 - NSFW Content]
            '''

            print(Colorate.Horizontal(Colors.blue_to_green, reportgründe))

            REASON = input(Colorate.Horizontal(Colors.cyan_to_green, f"Reason >> "))
            print("")

            if REASON == '1':
                self.REASON = 0
            elif REASON == '2':
                self.REASON = 1
            elif REASON == '3':
                self.REASON = 2
            elif REASON == '4':
                self.REASON = 3
            elif REASON == '5':
                self.REASON = 4
            else:
                print(f"""Wrong input""")

            self.sent = 0
            self.errors = 0

        def _reporter(self):
            report = requests.post(
                'https://discordapp.com/api/v8/report', json={
                    'channel_id': self.CHANNEL_ID,
                    'message_id': self.MESSAGE_ID,
                    'guild_id': self.GUILD_ID,
                    'reason': self.REASON
                }, headers={
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'sv-SE',
                    'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                    'Content-Type': 'application/json',
                    'Authorization': tkk
                }
            )
            if (status := report.status_code) == 201:
                self.sent += 1
                print(Colorate.Horizontal(Colors.cyan_to_green, f"[Successfully] reported! ><"))
            else:
                self.errors += 1
                print(Fore.LIGHTRED_EX + f"Error {Fore.LIGHTMAGENTA_EX}{report.text}")

        def _multi_threading(self):
            while True:
                if threading.active_count() <= 300:
                    time.sleep(1)
                    threading.Thread(target=self._reporter).start()


    mr = massreport()
    mr._multi_threading()