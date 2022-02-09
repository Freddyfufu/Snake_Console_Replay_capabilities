import threading
import time

import keyboard

eingabe = None

def getDirectionFromUser():
    done = False
    def go():
        global eingabe
        while not done:
            if keyboard.is_pressed('s'):
                eingabe = 's'
            elif keyboard.is_pressed("w"):
                eingabe= "w"
            elif keyboard.is_pressed("a"):
                eingabe = "a"
            elif keyboard.is_pressed("d"):
                eingabe = "d"

    t = threading.Thread(target=go)
    t.start()
    time.sleep(0.1)
    done = True
    return eingabe
