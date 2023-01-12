import pyautogui
import time

time.sleep(4) # Time in second before to take action

# Beginning of loop
count = 0

while count <= 500: # Number of lines to display 
    pyautogui.typewrite("enter your message here" + str (count))
    pyautogui.press("enter")
    count += 1
