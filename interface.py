from customtkinter import * 
import dataBaser 


set_appearance_mode("system")

class Window(CTk):
    def __init__(self, geometry=str, title=str):
        super().__init__()
        self.geometry = geometry
        self.title = str 

class Frame(CTkFrame):
    def __init__(self, window):
        super().__init__(window)

    def widget(self, type, **atbs):
        return type(self, **atbs)

loginWindow= Window("400x300", "Teste")


 

loginWindow.mainloop()
