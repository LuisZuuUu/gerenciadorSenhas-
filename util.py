import sqlite3
import os
import string
import tkinter as tk
from time import sleep
from random import choice


# CLASSE FRAME
class Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def funcao(self, widget, **opcoes):
        return widget(self, **opcoes)


# VARIAVEIS E FUNCOES ESTATICAS
usuarios = {}
caminho = os.path.join(os.getcwd(), "senhas.db")
caracteres = string.ascii_letters + string.digits + string.punctuation
conexao = sqlite3.connect(caminho)
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS senhas(
    site TEXT NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios(
    login_app TEXT NOT NULL,
    senha_app TEXT NOT NULL)
''')

def gerarSenha(tamanho):
    senha = ''.join(choice(caracteres) for _ in range(tamanho))
    return senha


def guardarInformacoes(site, login, senha):
    cursor.execute(
        '''INSERT INTO senhas (site, login, senha) VALUES(?, ?, ?)''',
        (site, login, senha)
    )


def validarLogin(nome, senha):
    if nome in usuarios:
        if usuarios[nome] == senha:
            print('Login feito com sucesso')
        else:
            print('Senha errada')
    else:
        print('Usuário não existe')
    


def cadastrarUsuario(nome, senha):
    if nome in usuarios:
        labelUsuario.config(text='Usuario já existe')
        return
    if not nome:
        print('Nome vazio')
        return 
    if not senha:
        print('Senha vazia')
        return False

    if senha and nome:
        botao1.destroy()
        botao2.pack_forget()
        

        linhaConfirmacao.pack()
        labelSenha.config(text='Confirmar senha')

        if not senha2.winfo_ismapped():    
            senha2.pack()
    
    if senha2.get() == senha:
        cursor.execute('''INSERT INTO usuarios (login_app, senha_app) VALUES (?, ?)''', nome, senha)
        conexao.commit()

    
    botao2.config(command=lambda: telaInicial.pack_forget())
    botao2.pack()



    

    


# CODIGO PRINCIPAL
if __name__ == '__main__':
    lambda: (guardarInformacoes('oi', 'tchau', 'ate'))
    conexao.commit()
    conexao.close()

    janela = tk.Tk()
    janela.title("Gerenciador de Senhas")
    janela.geometry("300x200")

    # TELA INICIAL
    telaInicial = Frame(janela)
    telaInicial.pack()
    linhaConfirmacao = Frame(telaInicial)
    senha2 = linhaConfirmacao.funcao(
            tk.Entry,
            show="*"
        )
    labelUsuario = telaInicial.funcao(
        tk.Label,
        text='Usuario',
        font=('Arial', 15)
    )
    labelUsuario.pack()

    usuario = telaInicial.funcao(tk.Entry)
    usuario.pack()

    labelSenha = telaInicial.funcao(
        tk.Label,
        text='Senha',
        font=('Arial', 15)
    )
    labelSenha.pack()

    senha = telaInicial.funcao(
        tk.Entry,
        show="*"
    )
    senha.pack()


    botao1 = telaInicial.funcao(
        tk.Button,
        text='Login',
        command=lambda: validarLogin(
            usuario.get(),
            senha.get()
        )
    )
    botao1.pack()

    botao2 = telaInicial.funcao(
        tk.Button,
        text='Cadastro',
        command=lambda: cadastrarUsuario(
            usuario.get(),
            senha.get()
        )
    )
    botao2.pack()
    lambda: (guardarInformacoes('oi', 'tchau', 'ate'))
    

    janela.mainloop()