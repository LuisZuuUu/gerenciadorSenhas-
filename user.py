import dataBaser as db 
from argon2 import PasswordHasher

ph = PasswordHasher()


def CreateUser(login, password):
    hash = ph.hash(password)
    db.cursor.execute("INSERT INTO LoginsManager (login, password) VALUES (?, ?)", (login, hash))
    db.conn.commit()

class UserLoggedIn:
    def __init__(self, id, login, password, status):
        self.id = id
        self.login = login 
        self.password = password
        self.authenticate = status

    @classmethod
    def authenticateUser(cls, login, password):
        try:
            db.cusor.execute("SELECT * FROM LoginManager WHERE login = ?", (login))
            userData = db.cursor.fetchone()

            if userData:
                dbId, dbLogin, dbPassword = userData

                if ph.verify(dbPassword, password):
                    print("Usuario conectado")
                    return cls(id=dbId, login=dbLogin, password=dbPassword, status=True) 
        
        except Exception as e:
            print(f"Error: {e}") 
            return None
         
    def deleteUser(self, password):
        try:
            db.cursor.execute("SELECT password FROM LoginsManager WHERE id = ?", (self.id))
            data = db.cursor.fetchone()
            hash = data[0]

            if ph.verify(hash, password):
                db.cursor.execute("DELETE FROM LoginsManager WHERE id = ?", (self.id))
                return True 
            else:
                print("erro")
                return False 
            
        except Exception as e:
            print(f"Erro: {e}")

    def data(self):
        try:
           db.cursor.execute("SELECT * FROM LoginsApp WHERE id = ?", (self.id))
           data = db.cursor.fetchall()
           return data 
        except Exception as e:
            print(f"Erro: {e}")

    
        



