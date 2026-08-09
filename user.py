import sqlite3 as sql

conn = sql.connect("senhas.db")
cursor = conn.cursor()

class CriarUsuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha 

        cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (login, senha))
        conn.commit()

class UsuarioLogado:
    def __init__(self, login, senha, id):
        self.login = login 
        self.senha = senha
        self.id = id

    def deletarUsuario(self, login, senha):
        if [login, senha] == [self.login, self.senha]:
            cursor.execute("DELETE FROM usuarios WHERE ")

