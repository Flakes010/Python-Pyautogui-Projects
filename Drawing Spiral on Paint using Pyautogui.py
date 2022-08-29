import pyautogui as gui
import time

distance = 700

time.sleep(3)
gui.mouseDown(600,200, button='left')

while distance > 0:
    gui.dragRel(distance, 0, button='left')
    distance -= 50
    gui.dragRel(0, distance, button='left')
    gui.dragRel(-distance, 0, button='left')
    distance -= 50
    gui.dragRel(0, -distance, button='left')
