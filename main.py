import pyautogui
import pandas as pd
import time

email = "testemail@gmail.com"
password = "iamtestingthiscode"
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

table = pd.read_csv("produtos.csv")

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

for i in table.index:

    pyautogui.click(x=676, y=257)

    pyautogui.write(str(table.loc[i, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[i, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[i, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[i, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[i, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[i, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(table.loc[i , "obs"]):
        pyautogui.write(str(table.loc[i, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

    time.sleep(1)

