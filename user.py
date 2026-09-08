import dataBaser as db 
from argon2 import PasswordHasher

ph = PasswordHasher()

def CreateUser(login, password, password2):
    
    try:
        if password == password2:
            hash = ph.hash(password)
            db.cursor.execute("INSERT INTO LoginsManager (login, password) VALUES (?, ?)", (login, hash))
            db.conn.commit()
            return True
        else:
            return None 
    except Exception as e:
        print(f"error: {e}")
        return e

class UserLoggedIn:
    def __init__(self, id, login, password, status=False):
        self.id = id
        self.login = login 
        self.password = password
        self.authenticate = status
        self.data = self.getData(self.id) 

    @classmethod
    def authenticateUser(cls, login, password):
        try:
            db.cursor.execute("SELECT * FROM LoginsManager WHERE login = ?", (login,))
            userData = db.cursor.fetchone()

            if userData:
                dbId, dbLogin, dbPassword = userData

                if ph.verify(dbPassword, password):
                    print("Usuario conectado")
                    return cls(id=dbId, login=dbLogin, password=dbPassword, status=True) 
                else:
                    return None 
            else:
                return None 
        
        except Exception as e:
            print(f"Error AUTENTICATHE USER : {e}") 
            return None
         
    def deleteUser(self, password):
        try:
            db.cursor.execute("SELECT password FROM LoginsManager WHERE id = ?", (self.id))
            data = db.cursor.fetchone()
            hash = data[0]

            if ph.verify(hash, password):
                self.data = db.cursor.execute("DELETE FROM LoginsManager WHERE id = ?", (self.id))
                return True 
            else:
                print("erro")
                return False 
            
        except Exception as e:
            print(f"Erro: {e}")

    def getData(self, id):
        try:
           db.cursor.execute("SELECT app, login, password FROM LoginsApp WHERE id = ?", (id,))
           return db.cursor.fetchall() 
        except Exception as e:
            print(f"Erro: {e}")


