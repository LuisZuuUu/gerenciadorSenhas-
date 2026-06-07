import sqlite3 as sql
import os
import string
import random

caminho = os.path.join(os.getcwd(), "senhas.db")
caracteres = string.ascii_letters + string.digits + string.punctuation 
conexao = sql.connect(caminho)
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS senhas(
    site TEXT NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NOT NULL)''')




def gerar_senha(tamanho):
    senha = []
    for i in range(tamanho + 1):
        senha.append(random.choice(caracteres))
    return ''.join(senha)

def guardar_informacoes(site, login, senha):
    cursor.execute('''INSERT INTO senhas VALUES(?, ?, ?)''', (site, login, senha))









