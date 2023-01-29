from scripts.settings import *
from scripts.closedms import *
from scripts.tokenchecker import *
from scripts.tokenlogin import *
from scripts.statuschanger import *
from scripts.servercloner import *
from scripts.webhookspammer import *
from scripts.dmfriends import *
from scripts.tokenactivity import *
from scripts.massban import *
from scripts.massreport import *
from scripts.cleardm import *
from scripts.tokenformatter import *


if not os.path.exists(getTempDir()+"\\colors"):
    setTheme('bluered')

if not os.path.exists(getTempDir()+"\\design"):
    setDesign('ghost')

def main():
    setTitle(f"🆂🆆🅰🆃🆃🅴🆁 | ᴹᵁᴸᵀᴵ ᵀᴼᴼᴸ | {developer}")
    os.system("cls")
    if getTheme() == "blue":
        banner('blue')
    elif getTheme() == "blueblack":
        banner('blueblack')
    elif getTheme() == "bluecyan":
        banner('bluecyan')
    elif getTheme() == "bluegreen":
        banner('bluegreen')
    elif getTheme() == "bluepurple":
        banner('bluepurple')
    elif getTheme() == "bluered":
        banner('bluered')
    elif getTheme() == "bluewhite":
        banner('bluewhite')
    elif getTheme() == "blackblue":
        banner('blackblue')
    elif getTheme() == "blackgreen":
        banner('blackgreen')
    elif getTheme() == "blackred":
        banner('blackred')
    elif getTheme() == "blackwhite":
        banner('blackwhite')
    elif getTheme() == "red":
        banner('red')
    elif getTheme() == "redblack":
        banner('redblack')
    elif getTheme() == "redblue":
        banner('redblue')
    elif getTheme() == "redgreen":
        banner('redgreen')
    elif getTheme() == "redpurple":
        banner('redpurple')
    elif getTheme() == "redwhite":
        banner('redwhite')
    elif getTheme() == "redyellow":
        banner('redyellow')
    elif getTheme() == "purpleblue":
        banner('purpleblue')
    elif getTheme() == "purplered":
        banner('purplered')
    elif getTheme() == "rainbow":
        banner('rainbow')
    elif getTheme() == "yellowgreen":
        banner('yellowgreen')
    elif getTheme() == "green":
        banner('green')
    elif getTheme() == "greenblue":
        banner('greenblue')
    elif getTheme() == "greencyan":
        banner('greencyan')
    elif getTheme() == "greenred":
        banner('greenred')
    elif getTheme() == "greenwhite":
        banner('greenwhite')
    elif getTheme() == "greenyellow":
        banner('greenyellow')
    elif getTheme() == "greenblack":
        banner('greenblack')
    elif getTheme() == "cyanblue":
        banner('cyanblue')
    elif getTheme() == "cyangreen":
        banner('cyangreen')
    elif getTheme() == "yellowred":
        banner('yellowred')
    elif getTheme() == "8":
        banner('reset')

    print("")
    inputclass()

def inputclass():
    if getTheme() == "blue":
        choice = input(Fore.BLUE + f"                                                 ╚═[User]══$» ")
    elif getTheme() == "blueblack":
        choice = input(Colorate.Horizontal(Colors.blue_to_black, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "bluecyan":
        choice = input(Colorate.Horizontal(Colors.blue_to_cyan, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "bluegreen":
        choice = input(Colorate.Horizontal(Colors.blue_to_green, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "bluepurple":
        choice = input(Colorate.Horizontal(Colors.blue_to_purple, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "bluered":
        choice = input(Colorate.Horizontal(Colors.blue_to_red, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "bluewhite":
        choice = input(Colorate.Horizontal(Colors.blue_to_white, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "blackblue":
        choice = input(Colorate.Horizontal(Colors.black_to_blue, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "blackgreen":
        choice = input(Colorate.Horizontal(Colors.black_to_green, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "blackred":
        choice = input(Colorate.Horizontal(Colors.black_to_red, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "blackwhite":
        choice = input(Colorate.Horizontal(Colors.black_to_white, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "red":
        choice = input(Fore.RED + f"                                                 ╚═[User]══$» ")
    elif getTheme() == "redblack":
        choice = input(Colorate.Horizontal(Colors.red_to_black, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "redblue":
        choice = input(Colorate.Horizontal(Colors.red_to_blue, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "redgreen":
        choice = input(Colorate.Horizontal(Colors.red_to_green, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "redpurple":
        choice = input(Colorate.Horizontal(Colors.red_to_purple, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "redwhite":
        choice = input(Colorate.Horizontal(Colors.red_to_white, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "redyellow":
        choice = input(Colorate.Horizontal(Colors.red_to_yellow, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "purpleblue":
        choice = input(Colorate.Horizontal(Colors.purple_to_blue, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "purplered":
        choice = input(Colorate.Horizontal(Colors.purple_to_red, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "rainbow":
        choice = input(Colorate.Horizontal(Colors.rainbow, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "yellowgreen":
        choice = input(Colorate.Horizontal(Colors.yellow_to_green, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "green":
        choice = input(Fore.GREEN + f"                                                 ╚═[User]══$» ")
    elif getTheme() == "greenblue":
        choice = input(Colorate.Horizontal(Colors.green_to_blue, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "greencyan":
        choice = input(Colorate.Horizontal(Colors.green_to_cyan, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "greenred":
        choice = input(Colorate.Horizontal(Colors.green_to_red, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "greenwhite":
        choice = input(Colorate.Horizontal(Colors.green_to_white, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "greenyellow":
        choice = input(Colorate.Horizontal(Colors.green_to_yellow, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "greenblack":
        choice = input(Colorate.Horizontal(Colors.green_to_black, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "cyanblue":
        choice = input(Colorate.Horizontal(Colors.cyan_to_blue, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "cyangreen":
        choice = input(Colorate.Horizontal(Colors.cyan_to_green, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "yellowred":
        choice = input(Colorate.Horizontal(Colors.yellow_to_red, f"""                                                 ╚═[User]══$» """, 1))
    elif getTheme() == "8":
        choice = input(Fore.RESET + f"                 ╚═[User]══$» ")
        

    if choice == "help":
        banner = f'''
                    accbackup » will save your account
                    accnuker » will destroy a acc and perma ban it 
                    botnuker » fastest bot on cord. (Proxy/Thread) support
                    cleardm » will clear all your dms
                    closedms » will close your dms
                    dmfriends » will dm your friends
                    massban » selfbot massban
                    massreport » will ban a (Server/Acc)
                    servercloner » will copy a server with perms
                    statuschanger » will change your status
                    token-activity » makes your tokens look real
                    token-checker » checks tokens
                    token-formatter » email:pw:token to token & email:pw in 2 files saved
                    wh-spammer » will spam and kill a webhook(brings server to lag)
                    tokenlogin » will log in any tokens (bypass 2fa)

                    Token-Generator » Fast Token Generator lock rating (20/100)%
        '''

        if getTheme() == "blue":
            textfarbe(banner)
        elif getTheme() == "blueblack":
            textfarbe(banner)
        elif getTheme() == "bluecyan":
            textfarbe(banner)
        elif getTheme() == "bluegreen":
            textfarbe(banner)
        elif getTheme() == "bluepurple":
            textfarbe(banner)
        elif getTheme() == "bluered":
            textfarbe(banner)
        elif getTheme() == "bluewhite":
            textfarbe(banner)
        elif getTheme() == "blackblue":
            textfarbe(banner)
        elif getTheme() == "blackgreen":
            textfarbe(banner)
        elif getTheme() == "blackred":
            textfarbe(banner)
        elif getTheme() == "blackwhite":
            textfarbe(banner)
        elif getTheme() == "red":
            textfarbe(banner)
        elif getTheme() == "redblack":
            textfarbe(banner)
        elif getTheme() == "redblue":
            textfarbe(banner)
        elif getTheme() == "redgreen":
            textfarbe(banner)
        elif getTheme() == "redpurple":
            textfarbe(banner)
        elif getTheme() == "redwhite":
            textfarbe(banner)
        elif getTheme() == "redyellow":
            textfarbe(banner)
        elif getTheme() == "purpleblue":
            textfarbe(banner)
        elif getTheme() == "purplered":
            textfarbe(banner)
        elif getTheme() == "rainbow":
            textfarbe(banner)
        elif getTheme() == "yellowgreen":
            textfarbe(banner)
        elif getTheme() == "green":
            textfarbe(banner)
        elif getTheme() == "greenblue":
            textfarbe(banner)
        elif getTheme() == "greencyan":
            textfarbe(banner)
        elif getTheme() == "greenred":
            textfarbe(banner)
        elif getTheme() == "greenwhite":
            textfarbe(banner)
        elif getTheme() == "greenyellow":
            textfarbe(banner)
        elif getTheme() == "greenblack":
            textfarbe(banner)
        elif getTheme() == "cyanblue":
            textfarbe(banner)
        elif getTheme() == "cyangreen":
            textfarbe(banner)
        elif getTheme() == "yellowred":
            textfarbe(banner)
        elif getTheme() == "8":
            textfarbe(banner)

        inputclass()

    elif choice == "closedms":
        print("")
        closedirectmessages().menu()
    
    elif choice == "accbackup":
        print("Coming Soon")

    elif choice == "token-activity":
        print("")
        tokenonline()

    elif choice == "wh-spammer":
        print("")
        whspammer()

    elif choice == "statuschanger":
        print("")
        statusch()

    elif choice == "cleardm":
        print("")
        cleardms()

    elif choice == "dmfriends":
        print("")
        massdmfriends()

    elif choice == "botnuker":
        print("Coming Soon")

    elif choice == "accnuker":
        print("")
        accnuke()
    
    elif choice == "servercloner":
        svc()

    elif choice == "token-checker":
        tokenchecker()
    
    elif choice == "tokenlogin":
        icytoken = input(Colorate.Horizontal(Colors.rainbow, f"{zeit} » Token to login » "))
        TokenLogin(token=icytoken)
    
    elif choice == "token-format":
        print("")
        tokenformat()
    
    elif choice == "massreport":
        print("")
        massrep()

    elif choice == "massban":
        print("")
        massban()

    elif choice == "design":
        print()
        print(Colorate.Horizontal(Colors.cyan_to_green, f"{zeit} » Design » "))
        print("")
        design = input(Colorate.Horizontal(Colors.green_to_cyan, f"» ", 1))
        with open(getTempDir()+"\\design", 'w'): pass
        with open(getTempDir()+"\\design", 'w') as f:
            f.write(design)
        main()
        
    elif choice == "color":
        colorsection = f'''    
[a] blue              [l] red               [x] green        
[b] blue_to_black     [m] red_to_black      [y] green_to_blue
[c] blue_to_cyan      [n] red_to_blue       [z] green_to_cyan       
[d] blue_to_green     [o] red_to_green      [1] green_to_red        
[e] blue_to_purple    [p] red_to_purple     [2] green_to_white  
[f] blue_to_red       [q] red_to_white      [3] green_to_yellow       
[g] blue_to_white     [r] red_to_yellow     [4] green_to_black   
[h] black_to_blue     [s] purple_to_blue    [5] cyan_to_blue  
[i] black_to_green    [t] purple_to_red     [6] cyan_to_green           
[j] black_to_red      [v] rainbow           [7] yellow_to_red  
[k] black_to_white    [w] yellow_to_green   [8] reset 

        '''

        print(Colorate.Horizontal(Colors.green_to_blue, colorsection, 1))
        
        themechoice = input(f'{Fore.GREEN}[{Fore.CYAN}»{Fore.GREEN}] {Fore.RESET}theme: {Fore.RED}')
        if themechoice == "a":
            setTheme('blue')
        elif themechoice == "b":
            setTheme('blueblack')
        elif themechoice == "c":
            setTheme('bluecyan')
        elif themechoice == "d":
            setTheme('bluegreen')
        elif themechoice == "e":
            setTheme('bluepurple')
        elif themechoice == "f":
            setTheme('bluered')
        elif themechoice == "g":
            setTheme('bluewhite')
        elif themechoice == "h":
            setTheme('blackblue')
        elif themechoice == "i":
            setTheme('blackgreen')
        elif themechoice == "j":
            setTheme('blackred')
        elif themechoice == "k":
            setTheme('blackwhite')
        elif themechoice == "l":
            setTheme('red')
        elif themechoice == "m":
            setTheme('redblack')
        elif themechoice == "n":
            setTheme('redblue')
        elif themechoice == "o":
            setTheme('redgreen')
        elif themechoice == "p":
            setTheme('redpurple')
        elif themechoice == "q":
            setTheme('redwhite')
        elif themechoice == "r":
            setTheme('redyellow')
        elif themechoice == "s":
            setTheme('purpleblue')
        elif themechoice == "t":
            setTheme('purplered')
        elif themechoice == "v":
            setTheme('rainbow')
        elif themechoice == "w":
            setTheme('yellowgreen')
        elif themechoice == "x":
            setTheme('green')
        elif themechoice == "y":
            setTheme('greenblue')
        elif themechoice == "z":
            setTheme('greencyan')
        elif themechoice == "1":
            setTheme('greenred')
        elif themechoice == "2":
            setTheme('greenwhite')
        elif themechoice == "3":
            setTheme('greenyellow')
        elif themechoice == "4":
            setTheme('greenblack')
        elif themechoice == "5":
            setTheme('cyanblue')
        elif themechoice == "6":
            setTheme('cyangreen')
        elif themechoice == "7":
            setTheme('yellowred')
        elif themechoice == "8":
            setTheme('reset')
        else:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Theme')
            sleep(1.5)
            main()
        sleep(0.5)
        main()

    else:
        main()

main()
