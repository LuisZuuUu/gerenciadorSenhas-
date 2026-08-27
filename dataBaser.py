import sqlite3 as sql 

conn = sql.connect("Database.db")
cursor = conn.cursor()



try:
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS LoginsManager(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL)""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LoginsApp (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app TEXT NOT NULL, 
        login TEXT NOT NULL UNIQUE, 
        password TEXT NOT NULL,
        relationfk INTEGER NOT NULL, 
        FOREIGN KEY(relationfk) REFERENCES LoginsManager(id) ON DELETE CASCADE)""")

    conn.commit()
    print("Conectado ao banco de dados")
except:
    print("Erro ao conectar ou criar banco de dados")
