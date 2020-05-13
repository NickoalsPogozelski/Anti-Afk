import pyautogui as py  
import keyboard as key
import time 

py.FAILSAFE = False

while True:
    time.sleep(30)
    py.dragTo(0,0,2)

    if key.is_pressed('esc'):
        break

