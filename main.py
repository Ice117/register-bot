import pyautogui
import pandas as pd
import time

email = "testemail@gmail.com"
password = "iamtestingthiscode"
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.press("tab")
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(password)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

pyautogui.press("tab")