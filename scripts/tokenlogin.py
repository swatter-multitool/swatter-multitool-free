from scripts.settings import *
from selenium import webdriver, common

def TokenLogin(token):
    j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
    script = """
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """ % (token)
    type_ = getDriver()

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Chrome(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            input()

    else:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Coudln\'t find a suitable driver to automatically login')
        input()

    driver.get("https://discordapp.com/login")
    driver.execute_script(script)