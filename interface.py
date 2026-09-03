from customtkinter import * 
import user

class Window(CTk):
    def __init__(self, title=str, geometry=str):
        super().__init__()
        self.title(title)
        self.geometry(geometry) 

class Frame(CTkFrame):

    def __init__(self, master, **atbs):
        super().__init__(master, **atbs)


    def button(self, **atbs):
        return CTkButton(self, corner_radius=10, fg_color="#9D0CFD", border_width=1, border_color="#9D0CFD", **atbs)

    def entry(self, **atbs):
        return CTkEntry(self, corner_radius=10, fg_color="transparent", border_width=1, **atbs)

    def label(self, **atbs):
        return CTkLabel(self, **atbs)



    


# TELA INICIAL

loginWindow = Window("Gerenciador Senhas", "400x300")
loginWindow.resizable(width=False, height=False)

frameLogin = Frame(loginWindow)
frameLogin.pack(fill=BOTH, expand=True)

login = frameLogin.entry(placeholder_text="login")
login.place(relx=1, x=-200,y=80, anchor=CENTER)
password = frameLogin.entry(placeholder_text="senha")
password.place(relx=1, x=-200, y=110, anchor=CENTER)

frameLogin.button(text="entrar", width=100,command=lambda:user.userTemporary(login.get(), password.get())).place(relx=1, x=-200, y=145, anchor=CENTER)
frameLogin.label(text="Não tem cadastro?").place(relx=1, x=-200, y=190, anchor=CENTER)
frameLogin.button(text="cadastrar", width=100).place(relx=1, x=-200, y=215, anchor=CENTER)







loginWindow.mainloop()







