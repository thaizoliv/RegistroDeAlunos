import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            tel TEXT NOT NULL,
                            sexo TEXT NOT NULL,
                            data_nascimento TEXT NOT NULL,
                            endereco TEXT NOT NULL,  
                            curso TEXT NOT NULL,
                            picture TEXT NOT NULL) ''')
        
    def register_student(self,estudantes):
        self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)", 
                       (estudantes))
        self.conn.commit()

        #mostrar mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro com sucesso')

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        for i in dados:
            print(f'ID:{i[0]} | Nome: {i[1]} | E-mail: {i[2]} | Tel: {i[3]} | Sexo: {i[4]} | Data de Nascimento: {i[5]} | Endereco: {i[6]} | Curso: {i[7]} | Imagem: {i[8]} ')

    def search_student(self,id):
        self.c.execute("SELECT * FROM estudantes WHERE id=? , (id) ")
        dados = self.c.fetchone()

        print(f'ID:{dados[0]} | Nome: {dados[1]} | E-mail: {dados[2]} | Tel: {dados[3]} | Sexo: {dados[4]} | Data de Nascimento: {dados[5]} | Endereco: {dados[6]} | Curso: {dados[7]} | Imagem: {dados[8]} ') 


    