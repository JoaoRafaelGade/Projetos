import pyautogui
import time

pyautogui.PAUSE = 0.4

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1.5)

pyautogui.click(x=677, y=411)
pyautogui.write("emailgenerico@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhagenerica123")
pyautogui.click(x=1009, y=581)

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:

    pyautogui.click(x=674, y=291)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    pyautogui.scroll(5000)


