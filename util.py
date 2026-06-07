import sqlite3
import os
import string
import random
import tkinter as tk 

caminho = os.path.join(os.getcwd(), "senhas.db")
caracteres = string.ascii_letters + string.digits + string.punctuation 
conexao = sqlite3.connect(caminho)
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS senhas(
    site TEXT NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NOT NULL)''')





def gerar_senha(tamanho):
    senha = []
    for i in range(tamanho + 1):
        senha.append(random.choice(caracteres))
    print(''.join(senha))

def guardar_informacoes(site, login, senha):  
    cursor.execute('''INSERT INTO senhas VALUES(?, ?, ?)''', (site, login, senha))

def entrada(janela):
    entrada = tk.Entry(janela)
    entrada.pack()
    return entrada.get()








