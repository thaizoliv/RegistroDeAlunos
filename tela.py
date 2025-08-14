#importando bibliotecas
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date


#cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde


#criando janela
janela = Tk()
janela.title("")
janela.geometry('810x535')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

# criando frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)



# trabalhando com logo
global imagem, imagem_string, l_imagem

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Sistema de Registro de Alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5,y=0)


#criando os campos de entrada

l_nome = Label(frame_detalhes, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)    
l_nome.place(x=4, y=10)
e_nome = Entry(frame_detalhes, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)

l_email = Label(frame_detalhes, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)    
l_email.place(x=4, y=70)
e_email = Entry(frame_detalhes, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_detalhes, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)    
l_tel.place(x=4, y=130)
e_tel = Entry(frame_detalhes, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

l_sexo = Label(frame_detalhes, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)    
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_detalhes, width=7, font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=130, y=160)

l_data_nascimento = Label(frame_detalhes, text="Data de Nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)    
l_data_nascimento.place(x=220, y=10)
data_nascimento = DateEntry(frame_detalhes, width=18, justify = 'center',  background='darkblue', foreground='white', borderwidth=2, year=2025)
data_nascimento.place(x=224, y=40)

l_endereco = Label(frame_detalhes, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)    
l_endereco.place(x=220, y=70)
e_endereco = Entry(frame_detalhes, width=20, justify='left', relief='solid')
e_endereco.place(x=224, y=100 )

l_curso = Label(frame_detalhes, text="Curso *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)    
l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'), justify='center')
c_curso['values'] = ('Informática', 'Administração', 'Engenharia', 'Direito', 'Medicina', 'Arquitetura', 'Psicologia', 'Educação Física', 'Ciências Contábeis')
c_curso.place(x=224, y=160)




#FUNCAO PARA ESCOLHER IMAGEM

def escolher_imagem():
    global imagem, imagem_string, l_imagem
    
    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'Alterar Imagem'.upper()


botao_carregar = Button(frame_detalhes, command=escolher_imagem, text="Carregar Imagem".upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0, relief=RAISED)
botao_carregar.place(x=390, y=160)


#tabela de estudantes
def mostrar_alunos():

    #treeview
    list_header = ['Id', 'Nome', 'Email', 'Telefone', 'Sexo', 'Data', 'Endereço', 'Curso']

    #view all students
    df_list = []

    tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show='headings')

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(row=1, column=0, sticky='nsew')
    vsb.grid(row=1, column=1, sticky='ns')
    hsb.grid(row=2, column=0, sticky='ew')
    frame_tabela.grid_rowconfigure(1, weight=12)

    hd=["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h=[40, 150, 150, 70, 70, 70, 120, 100, 100]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        #ADJUST COLUMN 
        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)




        #chamar tabela
mostrar_alunos()



janela.mainloop()