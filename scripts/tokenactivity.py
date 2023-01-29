from scripts.settings import *

import json, random, sys, re, threading, time, httpx, os, websocket, fade
from concurrent.futures import ThreadPoolExecutor
def online(token, game, type, status):
    ws = websocket.WebSocket()

    if status == "1":
        status = 'online'
    elif status == "2":
        status = 'dnd'
    elif status == "3":
        status = 'idle'

    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
    hello = json.loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    if type == "1":
        gamejson = {"name": game,"type": 0}
    elif type == '2':
        gamejson = {"name": game,"type": 1}
    elif type == "4":
        gamejson = {"name": game,"type": 2}
    elif type == "3":
        gamejson = {"name": game,"type": 3}

    auth = {"op": 2,"d": {"token": token,"properties": {"$os": sys.platform,"$browser": "RTB","$device": f"{sys.platform} Device"},"presence": {"game": gamejson,"status": status,"since": 0,"afk": False}},"s": None,"t": None}
    ws.send(json.dumps(auth))
    ack = {"op": 1,"d": None}
    while True:
        time.sleep(heartbeat_interval / 1000)
        try:
            ws.send(json.dumps(ack))
        except Exception as e:
            break
def tokenonline():
    type = input(Colorate.Horizontal(Colors.green_to_blue, f"[TYPE]{zeit} » [1] Playing | [2] Streaming | [3] Watching | [4] Listening » "))
    game = input(Colorate.Horizontal(Colors.blue_to_cyan, f"[STATUS]{zeit} » Custom Status » "))
    status = input(Colorate.Horizontal(Colors.red_to_purple, f"[IDLE]{zeit} » Which IDLE » [1] online | [2] dnd | [3]idle » "))
    executor = ThreadPoolExecutor(max_workers=1000)
    tokenfile = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files!", ".")), title="Please chose your Token List!")
    while True:
        for token in open(tokenfile, "r+").readlines():
            threading.Thread(target=lambda : online(token.replace("\n",""), game, type, status)).start()

        print(Colorate.Horizontal(Colors.rainbow, f"* Tokens all Online :)"))
        input("")