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

        self.loginRegister = self.registerFrame.entry(placeholder_text="login")
        self.loginRegister.place(relx=1, x=-200,y=80, anchor=CENTER)

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
        self.homeWindow = HomeWindow(self)
        self.homeWindow.mainloop()

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
        self.geometry("600x800")
        self.resizable(width=True, height=False)
        self.lastRow = 0 
        self.protocol("WM_DELETE_WINDOW", self.closeApp)
        self.table()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


    def closeApp(self):
        self.previous.destroy()

    def table(self):
        if loginWindow.currentUser:
            data = loginWindow.currentUser.getData(loginWindow.currentUser.id)
            self.frameScroll = CTkScrollableFrame(self)
            self.frameScroll.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            self.frameScroll.columnconfigure(0, weight=1)
       
            header = ("PLATAFORMA", "LOGIN", "SENHA")
            self.frameTable = Frame(self.frameScroll)
            self.frameTable.grid(row=0, column=0, sticky="ew")

            for col in range(3):
                self.frameTable.columnconfigure(col, weight=1)

            for col, title in enumerate(header):
                text = CTkLabel(self.frameTable, text=title, font=("Arial", 10, "bold"), border_width=1)
                text.grid(row=0, column=col, sticky="nsew", ipady=5)
            self.lastRow += 1

            if loginWindow.currentUser.data: 
                for enumRow, row in enumerate(data):
                    frameOption = Frame(self.frameTable, width=15, height=20 ,fg_color="transparent")
                    frameOption.grid(row=(enumRow+1),column=4, pady=5)

                    for enumCol, col in enumerate(row):
                        if enumCol == 0:
                            text = CTkLabel(self.frameTable, text=col, font=("Arial", 15), border_width=1)

                        elif enumCol in (1, 2):
                            text = CTkButton(self.frameTable, text=col, font=("Arial", 15), border_width=1, fg_color="transparent", command=lambda c=col: self.copy(c))
                            if enumCol == 2:
                                colHide = "*" * len(col)
                                text.configure(text=colHide)
                                btnHide = CTkButton(frameOption, text="show", width=10, height=10, fg_color="transparent", border_width=1, border_color="#9D0CFD")
                                btnHide.configure(command=lambda t=text, c=col, b=btnHide:self.hide(t,c,b))
                                btnHide.grid(row=0, column=0, pady=3)
                                btnDel = CTkButton(frameOption, text="del", width=10, height=10, fg_color="transparent", border_width=1, border_color="#9D0CFD")
                                btnDel.configure(command=lambda d=data[enumRow]: self.delete(d))
                                btnDel.grid(row=1, column=0, pady=3)
                                
                        text.grid(row=self.lastRow, column=enumCol, sticky="nsew", ipady=5)

                    self.lastRow += 1
            self.btnAdd = CTkButton(self.frameScroll, text="+", font=("Arial", 20, "bold"), width=30, height=30, fg_color="transparent", border_width=1, border_color="#9D0CFD")
            self.btnAdd.configure(command=self.createData)
            self.btnAdd.grid(row=self.lastRow, column=0, sticky="w", pady=5)

        else: 
            print("falhou")

    def hide(self, widget, col, btn):
        
        if btn.cget("text") == "hide":
            colHide = "*" * len(col)
            widget.configure(text=colHide, font=("Arial", 10, "bold"))
            btn.configure(text="show")
        elif btn.cget("text") == "show": 
            widget.configure(text=col)
            btn.configure(text="hide")

    def copy(self, col):
        self.clipboard_clear()
        self.clipboard_append(col)
        self.update()

        self.notice = CTkLabel(self, text="Texto copiado com sucesso ", fg_color="silver", text_color="#9D0CFD")
        self.notice.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.after(1500, self.notice.place_forget)

    def delete(self, row):
        boxConfirmation = CTkInputDialog(text="Confirme a senha para deletar", title="Confirmação")
        if boxConfirmation.get_input() == row[2]:
            loginWindow.currentUser.deleteData(row)
            self.updateData()

    def updateData(self):
        self.lastRow = 0
        self.frameScroll.destroy()
        self.table()

    def createData(self):
        self.lastRow +=1
        self.btnAdd.grid_forget()
        app = CTkEntry(self.frameTable, placeholder_text="Plataforma")
        app.grid(row=self.lastRow, column=0)
        login = CTkEntry(self.frameTable, placeholder_text="Login")
        login.grid(row=self.lastRow, column=1)
        password = CTkEntry(self.frameTable, placeholder_text="Senha")
        password.grid(row=self.lastRow, column=2)
        self.lastRow += 1
        self.btnAdd.configure(command=lambda:addData())
        self.btnAdd.grid(row=self.lastRow, column=0)

        def addData():
            try:
                appg = app.get()
                loging = login.get() 
                passwordg = password.get()
                row =(appg.strip().captalize(), loging.strip(), passwordg)
                valid = loginWindow.currentUser.addData(row)
                if valid:
                    self.updateData()
            except:
                print(f"error create data")
        
    

        
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


if __name__ == "__main__": 

    loginWindow = LoginWindow()
    loginWindow.mainloop()