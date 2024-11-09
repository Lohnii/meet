import tkinter as tk

#https://www.pythonprogressivo.net/2018/11/Botao-Checagem-Checkbutton-Classe-GUI.html

root = tk.Tk()

frameCima = tk.Frame(root)
frameCima.pack()

label = tk.Label(frameCima,text='Opções: ')
label.pack(anchor='w')

#abrir link
abrirLinkVar = tk.IntVar()
abrirLinkVar.set(0)
abrirLink = tk.Checkbutton(frameCima, text='Abrir link do meet automaticamente?',variable=abrirLinkVar)
abrirLink.pack(side='left')

def criar_textboxes():
    textboxes = []  # Lista para armazenar as caixas de texto
    for i in range(7):  # Criando 7 caixas de texto
        labelText = tk.Label(root, text='Link: ')
        labelText.pack(anchor='w', pady=5)  # Alinha o label à esquerda com um pouco de espaço
        textbox = tk.Entry(root, width=30)  # Cada Entry tem 30 caracteres de largura
        textbox.pack(pady=5)  # Adiciona a caixa de texto com um pequeno espaço vertical
        textboxes.append(textbox)  # Armazena a referência da caixa de texto na lista
    return textboxes

# Função para salvar os dados em um arquivo de texto
def salvar_dados():
    with open("dados.txt", "w") as file:  # Abre o arquivo para escrever
        for i, box in enumerate(textboxes):
            file.write(f"Texto da Caixa {i+1}: {box.get()}\n")  # Salva o texto de cada caixa de texto
    print("Dados salvos com sucesso!")

# Criando as 7 caixas de texto
textboxes = criar_textboxes()

# Adicionando um botão para salvar os dados
button = tk.Button(root, text="Salvar", command=salvar_dados)
button.pack(pady=20)





root.mainloop()