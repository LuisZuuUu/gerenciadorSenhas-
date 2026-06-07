import tkinter as tk 
import util

janela = tk.Tk()
janela.title("Gerenciador de Senhas")
janela.geometry("500x400")

tk.Label(janela, text='Escolha uma opção', font=('Arial', 15)).pack()


tk.Button(janela, text='Gerar senha', command=util.gerar_senha).pack()



janela.mainloop()