# coding=utf-8
#pip install keyboard
import keyboard
import time


# keyboard.press_and_release('left')
# time.sleep(0.01)
# keyboard.press_and_release('c')
# time.sleep(2)
# keyboard.write('22222')

# def test(e):
#     print e
#
#
# keyboard.hook(test)
# keyboard.wait('=')
time.sleep(2)
keyboard.press_and_release('enter')

import win32gui
import keyboard
import time

k = win32gui.FindWindow(None, 'Foxmail')
win32gui.SetForegroundWindow(k)
keyboard.press_and_release('down')
time.sleep(0.5)
keyboard.press_and_release('down')
time.sleep(0.5)
keyboard.press_and_release('down')
time.sleep(0.5)
keyboard.press_and_release('down')
time.sleep(0.5)
keyboard.press_and_release('down')
time.sleep(0.5)
keyboard.press_and_release('down')
time.sleep(0.5)
keyboard.press_and_release('down')