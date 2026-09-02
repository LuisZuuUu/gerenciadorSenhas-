from customtkinter import * 
import dataBaser 


class windowLogin(CTk):
    def __init__(self, title=str, geometry=str):
        super().__init__()
        self.title(title)
        self.geometry(geometry) 
        self.current = None
        self.frame = self.Frame(self)

class Frame(CTkFrame):
        
    current = False

    def __init__(self, master, **atbs):
        super().__init__(master, **atbs)


    def widget(self, widget, **atbs):
        return widget(self, **atbs)

    def changeFrame(self, frameIn=None, **atbs):
        if frameIn is not None:
            frameIn.grid(**atbs)
            self.grid_forget()
        else:
            self.grid(**atbs)

    
windowLogin = Window("Gerenciador Senhas", "400x200")
windowLogin.maxsize(400, 200)
windowLogin.resizable(width=False, height=False)

# TELA INICIAL 
frameLogin = Window.Frame(windowLogin)
frameLogin.grid()

frameLogin.widget(CTkLabel, text="Login", height=5, width=40).grid()
loginUser = frameLogin.widget(CTkEntry)
loginUser.grid()

windowLogin.mainloop()





loginWindow.mainloop()
