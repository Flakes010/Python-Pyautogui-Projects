import time
import pyautogui as gui

time.sleep(4)
textfile = open('message.txt')
for i in textfile:
    gui.typewrite(i)
    gui.press('enter')
