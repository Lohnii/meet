import tkinter as tk

#https://www.pythonprogressivo.net/2018/11/Botao-Checagem-Checkbutton-Classe-GUI.html

root = tk.Tk()

frameCima = tk.Frame(root)
frameCima.pack()

label = tk.Label(frameCima,text='Opções: ')
label.pack(anchor='w')

abrirLinkVar = tk.IntVar()
abrirLinkVar.set(0)
abrirLink = tk.Checkbutton(frameCima, text='Abrir link do meet automaticamente?',variable=abrirLinkVar)

abrirLink.pack(side='left')

root.mainloop()