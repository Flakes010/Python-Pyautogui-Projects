import pyautogui as gui
import time


time.sleep(3)
for i in range(5):
    gui.doubleClick(1053, 497, button='left')
    time.sleep(0.5)
    gui.scroll(-1080)
