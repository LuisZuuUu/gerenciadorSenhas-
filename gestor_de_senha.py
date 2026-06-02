from openpyxl import Workbook, load_workbook
import os
import string
import random
import tkinter as tk 

caminho = os.path.join(os.getcwd(), "senhas.xlsx")

wb = Workbook()
ws = wb.active
ws.title = "senhas"

caracteres = string.ascii_letters + string.digits + string.punctuation

if not os.path.isfile('senhas.xlsx'):
    wb.save(caminho)


def gerar_senha(tamanho):
    senha = []
    for i in range(tamanho + 1):
        senha.append(random.choice(caracteres))
    return senha

numero = int(input('alo'))

print(gerar_senha(numero))


    

janela = tk.Tk()




janela.mainloop()






