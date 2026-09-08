from customtkinter import * 
import user




class LoginWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador Senhas")
        self.geometry("400x300") 
        self.resizable(width=False, height=False)
        self.loginFrame()
        self.registerFrame()
        self.currentUser = None


    def loginFrame(self):
        self.loginFrame = Frame(self)
        self.loginFrame.pack(fill=BOTH, expand=True)

        self.login = self.loginFrame.entry(placeholder_text="login")
        self.login.place(relx=1, x=-200,y=80, anchor=CENTER)
        self.password = self.loginFrame.entry(placeholder_text="senha", show="*")
        self.password.place(relx=1, x=-200, y=110, anchor=CENTER)

        loginButton = self.loginFrame.button(text="entrar", width=100,command=lambda:userTemporary(self))
        loginButton.place(relx=1, x=-200, y=145, anchor=CENTER)
        self.loginFrame.label(text="Não tem cadastro?").place(relx=1, x=-200, y=190, anchor=CENTER)

        signUpButton = self.loginFrame.button(text="cadastrar", width=100, command=lambda:self.loginFrame.changeFrame(self.registerFrame))
        signUpButton.place(relx=1, x=-200, y=215, anchor=CENTER)

        self.errorLogin = self.loginFrame.label(text_color="#FF2D2D")

        def userTemporary(self):

            try:
                self.currentUser = user.UserLoggedIn.authenticateUser((self.login.get()).strip(), self.password.get())
                if self.currentUser:
                    if self.currentUser.data:
                        self.changeWindow()
                else:
                    self.errorLogin.configure(text="Senha e/ou login errado(s)")
                    self.errorLogin.place(relx=1, x=-200, y=50, anchor=CENTER)
                    self.loginFrame.after(1000, self.hideErrorLogin)

            except Exception as e:  
                print(f"error userTemporary : {e}")        




    def registerFrame(self):
        self.registerFrame = Frame(self)
        self.registerFrame.label(text="Seu login").place(relx=1, x=-320, y=80, anchor=CENTER)

        self.loginRegister = self.registerFrame.entry(placeholder_text="login")
        self.loginRegister.place(relx=1, x=-200,y=80, anchor=CENTER)

        self.passwordRegister = self.registerFrame.entry(placeholder_text="senha", show="*")
        self.passwordRegister.place(relx=1, x=-200, y=115, anchor=CENTER)

        self.registerFrame.label(text="Sua senha").place(relx=1, x=-320, y=115, anchor=CENTER)

        self.passwordRegister2 = self.registerFrame.entry(placeholder_text="senha", show="*")
        self.passwordRegister2.place(relx=1, x=-200, y=145, anchor=CENTER)

        self.registerFrame.label(text="Confirme ").place(relx=1, x=-320, y=145, anchor=CENTER)

        registerButton = self.registerFrame.button(text="cadastrar", width=100, command=lambda:self.register())
        registerButton.place(relx=1, x=-200, y=200, anchor=CENTER)

        self.errorRegister = self.registerFrame.label(text_color="#FF2D2D")

    def register(self):
        user1 = None 
        if (self.loginRegister.get()).strip() and self.passwordRegister.get() and self.passwordRegister2.get():
            user1 = user.CreateUser((self.loginRegister.get()).strip(), self.passwordRegister.get(), self.passwordRegister2.get())        

            if isinstance(user1, user.db.sql.IntegrityError):
                self.errorRegister.configure(text="Usuario já usado")
                self.errorRegister.place(relx=1, x=-200, y=20, anchor=CENTER)
                self.registerFrame.after(1000, self.hideErrorRegister)

            else:
                self.registerFrame.changeFrame(self.loginFrame)

                
        else:
            self.errorRegister.configure(text="Senhas não identicas")
            self.errorRegister.place(relx=1, x=-200, y=20, anchor=CENTER)
            self.registerFrame.after(1000, self.hideErrorRegister)

           
        

    def changeWindow(self):
        self.withdraw()
        homeWindow = HomeWindow(self)
        homeWindow.mainloop()

    def hideErrorLogin(self): 
        if self.loginFrame.winfo_exists():
            self.errorLogin.place_forget()

    def hideErrorRegister(self): 
        if self.registerFrame.winfo_exists():
            self.errorRegister.place_forget()
            
class HomeWindow(CTkToplevel):
    def __init__(self, previous):
        super().__init__()
        self.previous = previous 
        self.title("Tela Inicial | Gerenciador Senhas")
        self.geometry("800x600")
        self.maxsize(800,600) 

        self.protocol("WM_DELETE_WINDOW", self.closeApp)
        self.table()


    def closeApp(self):
        self.previous.destroy()

    def table(self):
        if loginWindow.currentUser:
            data = loginWindow.currentUser.data
            for row in data:
                for col in row:
                    print(col)
        else: 
            print("falhou")
        

        

        
class Frame(CTkFrame):

    def __init__(self, master, **atbs):
        super().__init__(master, **atbs)

    def button(self, **atbs):
        return CTkButton(self, corner_radius=10, fg_color="#9D0CFD", border_width=1, border_color="#9D0CFD", **atbs)

    def entry(self, **atbs):
        return CTkEntry(self, corner_radius=10, fg_color="transparent", border_width=1, **atbs)

    def label(self, **atbs):
        return CTkLabel(self, **atbs)
    
    def changeFrame(self, frameIn):
        self.pack_forget()
        frameIn.pack(fill=BOTH, expand=TRUE)


class FrameScroll(CTkScrollableFrame):
    def __init__():




 
    


    
if __name__ == "__main__": 
    # JANELA LOGIN|PRINCIPAL
    loginWindow = LoginWindow()



    loginWindow.mainloop()







