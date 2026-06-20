import pyautogui
from time import sleep
for i in range (0,3):
   pyautogui.write('Hello world!', interval=0.25)
   pyautogui.press('enter')
sleep(4)   