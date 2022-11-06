from cgitb import text
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import mysql.connector
cnxn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='biblioteca')
cursor = cnxn.cursor()
class Janelas():
    def __init__(self, base):
        self.janela = base
        self.frame = Frame(self.janela)
        self.frame.pack()
        self.frame2 = Frame(self.janela)
        self.frame2.pack()
    def destroy(self):
        self.frame2.destroy()
        self.frame2 = Frame(self.janela)
        self.frame2.pack()
        self.frame3.destroy()
        self.frame3 = Frame(self.janela)
        self.frame3.pack()
    def menu(self):
        texto_apresentação = Label(self.frame, text="Bem-vindo a biblioteca do Luiza Marinho")
        texto_apresentação.grid(column=0, row=0, padx=100, pady=20)
        botão = Button(self.frame, text='controle de livros', command=inicio.livros)
        botão.grid(column=0, row=1, pady=10)
        botão2 = Button(self.frame, text='controle de alunos', command=inicio.alunos)
        botão2.grid(column=0, row=3, pady=10)
        botão3 = Button(self.frame, text='sistema de emprestimos', command=inicio.emprestimos)
        botão3.grid(column=0, row=4, pady=10)
    def livros(self):
        self.frame.destroy()
        livros.livros()
    def alunos(self):
        self.frame.destroy()
        alunos.alunos()
    def emprestimos(self):
        pass
class Livros():
    def __init__(self,base):
        self.janela = base
        self.frame = Frame(self.janela)
        self.frame.pack()
        self.frame2 = Frame(self.janela)
        self.frame2.pack()
        self.frame3 = Frame(self.janela)
        self.frame3.pack()
    def destroy(self):
        self.frame2.destroy()
        self.frame2 = Frame(self.janela)
        self.frame2.pack()
        self.frame3.destroy()
        self.frame3 = Frame(self.janela)
        self.frame3.pack()
    def livros(self):
        self.frame.destroy()
        self.frame = Frame(self.janela)
        self.frame.pack()
        janela_livros = Frame(self.frame)
        janela_livros.pack()
        texto_apresentação = Label(janela_livros, text="CONTROLE DE LIVROS")
        texto_apresentação.grid(columnspan=4, row=0, padx=100, pady=20)
        botão = Button(janela_livros, text='Cadastrar novo livro', command=livros.cad_livro)
        botão.grid(column=0, row=1, pady=10)
        botão2 = Button(janela_livros, text='Pesquisar um livro', command=livros.pesquisar_livros)
        botão2.grid(column=1, row=1, pady=10)
        botão3 = Button(janela_livros, text='Exibir todos os livros cadastrados atualmente', command=livros.exibir_livros)
        botão3.grid(column=2, row=1, pady=10)
        botão4 = Button(janela_livros,text='Retirar livro do cadastro', command=livros.retirar_livro)
        botão4.grid(column=3, row=1, pady=10)
    def cad_livro(self):
    #itens janela
        livros.destroy()
        textoD = Label(self.frame2, text='NOVO CADASTRO')
        textoD.grid(columnspan=2, row=0)
        texto1 = Label(self.frame2, text='Nome')
        texto1.grid(column=0,row=1,pady=10)
        nome = Entry(self.frame2, width=40)
        nome.grid(column=1, row=1, pady=10)
        texto2 = Label(self.frame2, text='Autor')
        texto2.grid(column=0,row=2,pady=10)
        texto3 = Label(self.frame2, text='Gênero')
        texto3.grid(column=0,row=3,pady=10)
        texto4 = Label(self.frame2, text='Quantidade de Livros')
        texto4.grid(column=0,row=4,pady=10)
        texto5 = Label(self.frame2, text='Prateleira do Livro')
        texto5.grid(column=0,row=5,pady=10)
        texto6 = Label(self.frame2, text='Código')
        texto6.grid(column=0,row=6,pady=10)
        autor = Entry(self.frame2, width=40)
        autor.grid(column=1, row=2, pady=10)
        genero = Entry(self.frame2, width=40)
        genero.grid(column=1, row=3, pady=10)
        quantidade = Entry(self.frame2, width=40)
        quantidade.grid(column=1, row=4, pady=10)
        prateleira = Entry(self.frame2, width=40)
        prateleira.grid(column=1, row=5, pady=10)
        codigo = Entry(self.frame2, width=40)
        codigo.grid(column=1, row=6, pady=10)
        botão1 = Button(self.frame2, text='Enviar', command=lambda:livros.enviar_banco(nome.get(), autor.get(), genero.get(), quantidade.get(), prateleira.get(), codigo.get()))
        botão1.grid(columnspan=2, row=7, pady=10)
    def enviar_banco(self,nome,autor,genero,quantidade,prateleira,codigo):
        cursor.execute(f"""INSERT INTO livros
        VALUES ('{nome}','{autor}','{genero}',{quantidade},'{prateleira}',{codigo})""")
        cnxn.commit()
        livros.cad_livro()
    def exibir_livros(self):
        livros.destroy()
        #função
        cursor.execute("SELECT * FROM livros WHERE quantidade>0;") 
        rs = cursor.fetchall()
        Column,Row = 0,0
        scroll_bar = Scrollbar(self.frame2, orient=VERTICAL)
        scroll_bar.grid(row=0, column=1, sticky='ns')
        canvas = Canvas(self.frame2, yscrollcommand = scroll_bar.set)
        canvas.grid(row=0, column=0, sticky="news")
        scroll_bar.config( command = canvas.yview )
        internal_frame = Frame(canvas)
        canvas.create_window((0, 0), window=internal_frame, anchor='nw')
        canvas.config(scrollregion=canvas.bbox("all"))
        for i in rs:
          livros_exibir = Label(internal_frame, text=f'Titulo: {i[0]}\nAutor: {i[1]}\nGênero: {i[2]}\nQuantia de livros: {i[3]}\n\n')
          livros_exibir.grid(column=Column, row=Row, padx=10)
          Column += 1
          if Column == 3:
            Column = 0
            Row += 1
    def pesquisar_livros(self):
        #itens janela
        livros.destroy()
        textoD = Label(self.frame2, text='Pesquisar um livro')
        textoD.pack(side=TOP, anchor=N)
        caixa_P = Entry(self.frame2, width=30)
        caixa_P.pack(anchor=CENTER)
        botão = Button(self.frame2, text='pesquisar', command=lambda: livros.pesquisa(caixa_P.get(), livro))
        botão.pack(anchor=CENTER)
        livro = Label(self.frame2, text='')
        livro.pack(anchor=CENTER)
    def pesquisa(self, nome, livro):
     cursor.execute(f"SELECT * FROM livros WHERE titulo='{nome}';") 
     row = cursor.fetchall() 
     cad = 0
     for i in row:
        livro['text'] = f"Titulo: {i[0]}\nAutor: {i[1]}\nGênero: {i[2]}\nQuantia de livros: {i[3]}\n\n"
        cad = 1
     if cad == 0:
         livro['text'] = 'livro não encontrado'
    def retirar_livro(self):
    #itens janela
        livros.destroy()
        textoD = Label(self.frame2, text='codigo do livro')
        textoD.pack(side=TOP, anchor=N)
        caixa_P = Entry(self.frame2, width=30)
        caixa_P.pack()
        botão = Button(self.frame2, text='pesquisar', command=lambda: livros.pesquisa_dell(caixa_P.get()))
        botão.pack()      
    def pesquisa_dell(self,nome):
        self.frame3.destroy()
        self.frame3 = Frame(self.janela)
        self.frame3.pack()
        livro = Label(self.frame3, text='')
        livro.pack()
        cursor.execute(f"SELECT * FROM livros WHERE titulo='{nome}';")  
        row = cursor.fetchall() 
        if row == []:
            livro['text'] = 'livro não encontrado'
        else:
            for i in row: 
             livro['text'] = f'Titulo: {i[0]}\nAutor: {i[1]}\nGênero: {i[2]}\nQuantia de livros: {i[3]}'
             quantia_existente = i[3]
             frame2 = Frame(self.frame3)
             frame2.pack(anchor=CENTER)
             confirmação = Label(frame2, text='Quantos exemplares deseja retirar?')
             confirmação.pack(anchor=CENTER)
             quantidade = Spinbox(frame2, width=30, from_=0, to=quantia_existente,increment=1)
             quantidade.pack()
             botão= Button(frame2, text='confirmar', command=lambda: livros.deletar(nome, quantidade.get()))
             botão.pack() 
    def deletar(self,livro,quantidade):
        cursor.execute(f'UPDATE livros SET quantidade=quantidade-{quantidade} WHERE titulo="{livro}"')
        cnxn.commit()
        livros.retirar_livro()
class Alunos():
    def __init__(self,base):
        self.janela = base
        self.frame = Frame(self.janela)
        self.frame.pack()
        self.frame2 = Frame(self.janela)
        self.frame2.pack()
        self.frame3 = Frame(self.janela)
        self.frame3.pack()
    def alunos(self):
        self.frame.destroy()
        self.frame = Frame(self.janela)
        self.frame.pack()
        destaque = Label(self.frame, text="Controle dos alunos")
        destaque.grid(columnspan=4, row=0, padx=100, pady=20)
        cadastro = Button(self.frame, text="Cadastro de Aluno", command=alunos.cadastro)
        cadastro.grid(column=0, row=1, pady=10)
        pesquisa = Button(self.frame, text="Pesquisar cadastro", command=alunos.pesquisa)
        pesquisa.grid(column=1, row=1, pady=10)
        exibir = Button(self.frame, text="Exibir cadastros", command=alunos.exibir)
        exibir.grid(column=2, row=1, pady=10)
        retirar = Button(self.frame, text="Retirar cadastro", command=alunos.retirar)
        retirar.grid(column=3, row=1, pady=10)
    def destroy(self):
        self.frame2.destroy()
        self.frame2 = Frame(self.janela)
        self.frame2.pack()
        self.frame3.destroy()
        self.frame3 = Frame(self.janela)
        self.frame3.pack()
    def cadastro(self):
        alunos.destroy()
        destaque = Label(self.frame2,text="Novo cadastro de aluno")
        destaque.grid(columnspan=2, row=0)
        name_t = Label(self.frame2, text="Nome:")
        name_t.grid(column=0, row=1)
        name = Entry(self.frame2)
        name.grid(column=1, row=1)
        user_t = Label(self.frame2, text="Login:")
        user_t.grid(column=0, row=2)
        user = Entry(self.frame2)
        user.grid(column=1, row=2)
        password_t = Label(self.frame2, text="Senha:")
        password_t.grid(column=0, row=3)
        password = Entry(self.frame2)
        password.grid(column=1, row=3)
        confirmation_t = Label(self.frame2, text="Confirmar senha:")
        confirmation_t.grid(column=0, row=4)
        confirmation = Entry(self.frame2)
        confirmation.grid(column=1,row=4)
        submmit = Button(self.frame2, text="Enviar", command=lambda: alunos.cad_aluno(name.get(), user.get(), password.get(), confirmation.get()))
        submmit.grid(columnspan=2, row= 5)
    def cad_aluno(self, name, user, password, confirmation):
        print(name, user, password, confirmation)
    def pesquisa(self):
        pass
    def exibir(self):
        pass
    def retirar(self):
        pass

base = Tk()
base.title('Biblioteca')
base.geometry('800x500')
inicio = Janelas(base)
livros = Livros(base)
alunos = Alunos(base)
inicio.menu()
base.mainloop()