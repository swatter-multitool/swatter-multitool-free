from scripts.settings import *

def tokenformat():
    print(Colorate.Horizontal(Colors.blue_to_green, f"{zeit} » Token » Choose your File"))
    time.sleep(1)
    tokenfile = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files!", ".")), title="Please chose your Token List!")
    input_text = open(tokenfile, 'r').read().splitlines()

    tokens = []
    emailpass = []

    for entry in input_text:
        seperated = entry.split(':')
        if seperated != ['']:
            tokens.append(seperated[2])
            _sepered = entry.split(':')
            emailpass.append(f"{_sepered[0]}:{_sepered[1]}")

    with open('tokens_formated.txt', 'w+') as f:
        f.write("\n".join(tokens))
    
    with open('email_pass_formated.txt', 'w+') as f:
        f.write("\n".join(emailpass))