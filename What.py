
import tkinter as tk
from tkinter import messagebox
import pyautogui
import time

pyautogui.PAUSE = 0.5

# Função para exibir mensagem informativa usando Tkinter
def exibir_mensagem_tkinter(titulo, mensagem):
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Exibe a mensagem usando a caixa de diálogo Tkinter
    messagebox.showinfo(titulo, mensagem)
    
exibir_mensagem_tkinter("Passo a Passo","O código vai começar. Não utilize nada do computador até o código finalizar!")
# Abrir o Google no computador

pyautogui.press('winleft')
pyautogui.write('google chrome')
pyautogui.press('enter')

# Entra no outlok

time.sleep(4)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(4)



