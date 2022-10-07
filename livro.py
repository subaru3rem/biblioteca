from ast import Lambda
from cProfile import label
from cgitb import text
from logging import root
from msilib import Table
from struct import pack
from tkinter.tix import COLUMN
from tkinter.scrolledtext import ScrolledText
from turtle import right
from tkinter import *
import mysql.connector
cnxn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='biblioteca')
cursor = cnxn.cursor()
def cad_livro():
    #itens janela
    janela_cadLivro = Frame()
    janela_cadLivro.pack()
    textoD = Label(janela_cadLivro, text='NOVO CADASTRO')
    textoD.grid(columnspan=2, row=0)
    texto1 = Label(janela_cadLivro, text='Nome')
    texto1.grid(column=0,row=1,pady=10)
    nome = Entry(janela_cadLivro, width=40)
    nome.grid(column=1, row=1, pady=10)
    texto2 = Label(janela_cadLivro, text='Autor')
    texto2.grid(column=0,row=2,pady=10)
    texto3 = Label(janela_cadLivro, text='Gênero')
    texto3.grid(column=0,row=3,pady=10)
    texto4 = Label(janela_cadLivro, text='Quantidade de Livros')
    texto4.grid(column=0,row=4,pady=10)
    texto5 = Label(janela_cadLivro, text='Prateleira do Livro')
    texto5.grid(column=0,row=5,pady=10)
    texto6 = Label(janela_cadLivro, text='Código')
    texto6.grid(column=0,row=6,pady=10)
    autor = Entry(janela_cadLivro, width=40)
    autor.grid(column=1, row=2, pady=10)
    genero = Entry(janela_cadLivro, width=40)
    genero.grid(column=1, row=3, pady=10)
    quantidade = Entry(janela_cadLivro, width=40)
    quantidade.grid(column=1, row=4, pady=10)
    prateleira = Entry(janela_cadLivro, width=40)
    prateleira.grid(column=1, row=5, pady=10)
    codigo = Entry(janela_cadLivro, width=40)
    codigo.grid(column=1, row=6, pady=10)
    botão1 = Button(janela_cadLivro, text='Enviar', command= lambda: enviar_banco(nome.get(), autor.get(),genero.get(),quantidade.get(),prateleira.get(),codigo.get()))
    botão1.grid(columnspan=2, row=7, pady=10)
    #função
    def enviar_banco(nome,autor,genero,quantidade,prateleira,codigo):
     cursor.execute(f"""INSERT INTO livros
     VALUES ('{nome}','{autor}','{genero}',{quantidade},'{prateleira}',{codigo})""")
     cnxn.commit()
     text = Label(janela_cadLivro, text='item adicionado')
     text.grid(columnspan=2, row=8)
     janela_cadLivro.destroy()
def exibir_livros():
    #itens janela
    janela_exibir = Frame()
    janela_exibir.pack() 
    livros_exibir = ScrolledText(janela_exibir, width=50,  height=10)
    livros_exibir.pack(side=LEFT, anchor=N, padx=10, pady=10, ipadx=10, ipady=5)
    
    #função
    cursor.execute("SELECT * FROM livros WHERE quantidade>0;") 
    rs = cursor.fetchall()
    cad = 0 
    for i in rs:
        if cad == 0:
            livros_exibir.insert(END, f'Titulo: {i[0]}\nAutor: {i[1]}\nGênero: {i[2]}\nQuantia de livros: {i[3]}\n\n')  
    livros_exibir["state"] = "disabled"
    janela_exibir.mainloop()
def pesquisar_livros():
    #itens janela
    janela_pesquisa = Tk()
    janela_pesquisa.title('Pesquisar Livro')
    janela_pesquisa.geometry('500x500')
    textoD = Label(janela_pesquisa, text='Pesquisar um livro')
    textoD.pack(side=TOP, anchor=N)
    caixa_P = Entry(janela_pesquisa, width=30)
    caixa_P.pack(anchor=CENTER)
    botão = Button(janela_pesquisa, text='pesquisar', command=lambda: pesquisa(caixa_P.get()))
    botão.pack(anchor=CENTER)
    livro = Label(janela_pesquisa, text='')
    livro.pack(anchor=CENTER)

    #função
    def pesquisa(nome):
     cursor.execute(f"SELECT * FROM livros WHERE titulo='{nome}';") 
     row = cursor.fetchall() 
     cad = 0
     for i in row:
            livro['text'] = livro['text'] + f"Titulo: {i[0]}\nAutor: {i[1]}\nGênero: {i[2]}\nQuantia de livros: {i[3]}\n\n"
            cad = 1
     if cad == 0:
         livro['text'] = 'livro n encontrado'

    janela_pesquisa.mainloop()
def retirar_livro():
    #itens janela
    dell = Tk()
    dell.title('Exluir Livro')
    frame = Frame(dell)
    dell.geometry('500x200')
    textoD = Label(dell, text='codigo do livro')
    textoD.pack(side=TOP, anchor=N)
    frame.pack(anchor=CENTER)
    caixa_P = Entry(frame, width=30)
    caixa_P.pack()
    botão = Button(frame, text='pesquisar', command=lambda: pesquisa_dell(caixa_P.get()))
    botão.pack()
    livro = Listbox(frame)
    livro.pack()
    
    #função
    def deletar(livro,quantidade):
        cursor.execute(f'UPDATE livros SET quantidade=quantidade-{quantidade} WHERE titulo="{livro}"')
        cnxn.commit()
        frame.destroy()
    def pesquisa_dell(nome):
        cursor.execute(f"SELECT * FROM livros WHERE titulo='{nome}';")  
        row = cursor.fetchall() 
        cad = 0
        for i in row: 
            livro.insert(1,f'Titulo: {i[0]}',f'Autor: {i[1]}',f'Gênero: {i[2]}',f'Quantia de livros: {i[3]}')
            cad = 1 
            quantia_existente = i[3] 
        if cad == 0:
         livro['text'] = 'livro n encontrado'
        
        #itens janela
        frame2 = Frame(frame)
        frame2.pack(anchor=CENTER)
        confirmação = Label(frame, text='Quantos exemplares deseja retirar?')
        confirmação.pack(anchor=CENTER)
        quantidade = Spinbox(frame2, width=30, from_=0, to=quantia_existente,increment=1)
        quantidade.pack()
        botão= Button(frame2, text='confirmar', command=lambda: deletar(nome, quantidade.get()))
        botão.pack()  
    

    dell.mainloop()
    