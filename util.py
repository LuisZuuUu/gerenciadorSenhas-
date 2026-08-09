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


#class Usuario():
#    def __init__(self, usuario, senha):
#        cursor.execute(
#        '''INSERT INTO usuarios (login_app, senha_app) VALUES(?, ?)''',
#        (usuario, senha)
#   )
#        conexao.commit()
    
#    def modificarUsuario():


# VARIAVEIS E FUNCOES ESTATICAS
caminho = os.path.join(os.getcwd(), "senhas.db")
caracteres = string.ascii_letters + string.digits + string.punctuation
conexao = sqlite3.connect(caminho)
cursor = conexao.cursor() 
janela = tk.Tk()
janela.title("Gerenciador de Senhas")
janela.geometry("350x200")
janela.maxsize(350, 200)
cursor.execute(f'''SELECT * from senhas WHERE senha = "juju"''')
tels = cursor.fetchall()
print(tels)
cursor.execute('''
CREATE TABLE IF NOT EXISTS senhas(
    id 
    site TEXT NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NOT NULL,
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios(
    id PRIMARY KEY AUTOINCREMENT, 
    login_app TEXT NOT NULL,
    senha_app TEXT NOT NULL)
''')

def gerarSenha(tamanho):
    senha = ''.join(choice(caracteres) for _ in range(tamanho))
    return senha

def botaoVoltar(frame, frame_sai, frame_entra):
    botaoSair = tk.Button(frame, text='<', command=lambda: trocar_frame(frame_sai, frame_entra), height=1, width=2)
    botaoSair.place(relx=.05, rely=.1)

def guardarInformacoes(site, login, senha):
    cursor.execute(
        '''INSERT INTO senhas (site, login, senha) VALUES(?, ?, ?)''',
        (site, login, senha)
    )


def validarLogin(nome, senha):  
    cursor.execute(f"SELECT * FROM usuarios WHERE login_app = '{nome}'")
    usuario = cursor.fetchone()
    if usuario:
        if usuario[0] == nome and usuario[1] == senha:
            print(0)
            trocar_frame(telaLogin, telaPrincipal)
        elif usuario[0] == nome and usuario[1] != senha:
                texto = telaLogin.funcao(tk.Label, text='Senha nao corresponde!', font=('Arial', 10))
                texto.pack()
                texto.after(600, lambda: texto.destroy())
    else:
        texto = telaLogin.funcao(tk.Label, text='Usuario não existe', font=('Arial', 10))
        texto.pack()
        texto.after(600, lambda: texto.destroy())
    

def trocar_frame(frame_sai, frame_entra):
    if frame_entra == 'telaPrincial':
        frame_sai.place_forget()
        frame_entra.grid()
    elif frame_sai == 'telaPrincial':
        frame_sai.grid.forget()
        frame_entra.place(relwidth=1, relheight=1)
    else:
        frame_sai.place_forget()
        frame_entra.place(relwidth=1, relheight=1)
    

def cadastrarUsuario(nome, senha, senha2):
    if nome and senha: 
        if senha == senha2:
            botao_cadastro.config(command=salvarInfoUsuario(nome, senha))
            trocar_frame(telaCadastro, telaLogin)
        else: 
            texto = telaCadastro.funcao(tk.Label, text='Senhas são diferentes', font=('Arial', 8))
            texto.pack()
            texto.after(500, lambda: texto.pack_forget())
    elif nome and not senha:
        texto = telaCadastro.funcao(tk.Label, text='Senha ta vazia', font=('Arial', 8))
        texto.pack()
        texto.after(500, lambda: texto.pack_forget())
    else: 
        texto = telaCadastro.funcao(tk.Label, text='Nome ta vazio', font=('Arial', 8))
        texto.pack()
        texto.after(500, lambda: texto.pack_forget())
    

def salvarInfoUsuario(nome, senha):
    cursor.execute(
        '''INSERT INTO usuarios (login_app, senha_app) VALUES(?, ?)''',
        (nome, senha)
    )
    conexao.commit()

# TELAS 
telaInicial = Frame(janela)
telaInicial.config(bg='grey')
telaLogin = Frame(janela)
telaLogin.config(bg='grey')
telaCadastro = Frame(janela)
telaCadastro.config(bg='grey')
telaPrincipal = Frame(janela)
telaPrincipal.config(bg='grey')


# TELA INICIAL 
bota_login = telaInicial.funcao(tk.Button, text='Login', bg='lightblue', command=lambda: trocar_frame(telaInicial, telaLogin)).place(relx=.5, rely=.1, anchor='center')
bota_cadastro = telaInicial.funcao(tk.Button, text='Cadastro', bg='lightblue', command= lambda: trocar_frame(telaInicial, telaCadastro)).place(relx=.5, rely=.25, anchor='center') 
# ================================= #


# TELA LOGIN 
telaLogin.funcao(tk.Label, text='Login', font=('Arial', 13), bg='grey', foreground='white').place(relx=.5, rely=.1, anchor='center')
entry_login = telaLogin.funcao(tk.Entry)
entry_login.place(relx=.5, rely=0.23, anchor='center')
telaLogin.funcao(tk.Label, text='Senha', font=('Arial', 13), bg='grey', foreground='white').place(relx=.5, rely=.36, anchor='center')
entry_senha = telaLogin.funcao(tk.Entry, show='*')
entry_senha.place(relx=.5, rely=.49, anchor='center')
botao_valida_login = telaLogin.funcao(tk.Button, text="Entrar", bg='lightblue', command=lambda:validarLogin(entry_login.get().strip(), entry_senha.get()))
botao_valida_login.place(relx=.5, rely=.62, anchor='center')
botaoSairLogin = botaoVoltar(telaLogin, telaLogin, telaInicial)
# ================================= #

# TELA CADASTRO 
telaCadastro.funcao(tk.Label, text='Login', font=('Arial', 13), bg="grey", foreground='white').place(relx=.5, rely=.1, anchor='center')
entry_cadastro_login = telaCadastro.funcao(tk.Entry)
entry_cadastro_login.place(relx=.5, rely=.23, anchor='center')
telaCadastro.funcao(tk.Label, text='Senha', font=('Arial', 13), bg="grey", foreground='white').place(relx=.5, rely=.36, anchor='center')
entry_cadastro_senha = telaCadastro.funcao(tk.Entry, show='*')
entry_cadastro_senha2 = telaCadastro.funcao(tk.Entry, show='*')
entry_cadastro_senha.place(relx=.5, rely=.49, anchor='center')
entry_cadastro_senha2.place(relx=.5, rely=.60, anchor='center')
telaCadastro.funcao(tk.Label, text='Confirmar senha', font=('Arial', 7), bg="grey").place(relx=.2, rely=.60, anchor='center')
botao_cadastro = telaCadastro.funcao(tk.Button, text='Cadastrar', bg='lightblue', command=lambda: cadastrarUsuario(entry_cadastro_login.get().strip(), entry_cadastro_senha.get(), entry_cadastro_senha2.get().strip()))
botao_cadastro.place(relx=.5, rely=.77, anchor='center')
botaoSairCadastro = botaoVoltar(telaCadastro, telaCadastro, telaInicial)


# TELA PRINCIPAL 
def criarTabela(usuario):
    cursor.execute(f'''SELECT * from senhas WHERE login = {usuario}''')

# CODIGO PRINCIPAL
if __name__ == '__main__':

    telaInicial.place(relwidth=1, relheight=1)
    

    janela.mainloop()