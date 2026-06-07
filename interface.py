import tkinter as tk 
import util

janela = tk.Tk()
janela.title("Gerenciador de Senhas")
janela.geometry("500x400")


# TELA INICIAL 

tela_inicial = tk.Frame(janela)
tela_inicial.pack()

tk.Label(tela_inicial, text='Escolha uma opção', font=('Arial', 15)).pack()


tk.Button(tela_inicial, text='' 
'').pack()



janela.mainloop()