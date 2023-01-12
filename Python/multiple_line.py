import pyautogui
import time

time.sleep(4)
count = 0

while count <= 500:
    pyautogui.typewrite("enter your message here" + str (count))
    pyautogui.press("enter")
    count += 1
