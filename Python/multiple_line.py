import pyautogui
import time

time.sleep(4) # Time in second before taking action

# Beginning of the loop
count = 0

while count <= 5: # Number of lines to display 
    pyautogui.typewrite("enter your message here" + str (count))
    pyautogui.press("enter")
    count += 1
