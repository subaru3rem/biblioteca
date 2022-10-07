from cProfile import label
from codeop import CommandCompiler
from distutils.cmd import Command
from tkinter.tix import COLUMN
from livro import *
from tkinter import *
cad = ""
def janela_livros():
    janela_inicio.destroy()
    janela_livros = Frame()
    janela_livros.pack()
    texto_apresentação = Label(janela_livros, text="CONTROLE DE LIVROS")
    texto_apresentação.grid(columnspan=4, row=0, padx=100, pady=20)
    botão = Button(janela_livros, text='Cadastrar novo livro', command=cad_livro)
    botão.grid(column=0, row=1, pady=10)
    botão2 = Button(janela_livros, text='Pesquisar um livro', command=pesquisar_livros)
    botão2.grid(column=1, row=1, pady=10)
    botão3 = Button(janela_livros, text='Exibir todos os livros cadastrados atualmente', command=exibir_livros)
    botão3.grid(column=2, row=1, pady=10)
    botão4 = Button(janela_livros,text='Retirar livro do cadastro', command=retirar_livro)
    botão4.grid(column=3, row=1, pady=10)
    janela_livros.mainloop()

def janela_alunos():
    #jp
    pass
def emprestimos():
    #jp
    pass

janela_principal = Tk()
janela_principal.title('Biblioteca')
janela_inicio = Frame(janela_principal)
janela_inicio.pack()

texto_apresentação = Label(janela_inicio, text="Bem-vindo a biblioteca do Luiza Marinho")
texto_apresentação.grid(column=0, row=0, padx=100, pady=20)

botão = Button(janela_inicio, text='controle de livros', command=janela_livros)
botão.grid(column=0, row=1, pady=10)
botão2 = Button(janela_inicio, text='controle de alunos', command=janela_alunos)
botão2.grid(column=0, row=3, pady=10)
botão3 = Button(janela_inicio, text='sistema de emprestimos', command=emprestimos)
botão3.grid(column=0, row=4, pady=10)

janela_principal.mainloop() 

