import csv
import random
from sqlite3 import connect
import sqlite3
from tkinter.font import names

import sqlite3
import random
import time
import datetime
#import os

#os.remove('SDC_Academy1.db') if os.path.exists('SDC_Academy1.db') else None

# Criando uma conexão 
conn = sqlite3.connect('SDC_Academy1.db')

# Criando um cursor 
c = conn.cursor()

# Função para criar uma tabela 
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Programador(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
    'funcionario_name TEXT, prog_name TEXT, valor_salarial REAL)')

# Função para inserir um linha 
def data_insert():
    c.execute("INSERT INTO Programador VALUES(002, '2022-11-30 08:00:20', 'Pedro', 'Supervidor Técnico', 'R$8000')")
    c.execute("INSERT INTO Programador VALUES(003, '2022-11-30 08:00:20', 'Guilherme', 'Lider Técnico', 'R$6000')")
    c.execute("INSERT INTO Programador VALUES(004, '2022-11-30 08:00:20', 'Romilson Luis', 'Analista de Dados', 'R$4000')")
    c.execute("INSERT INTO Programador VALUES(005, '2022-11-30 08:00:20', 'Ligia', 'Finance Analyst', 'R$4000')")
    c.execute("INSERT INTO Programador VALUES(006, '2022-11-30 08:00:20', 'Isaac Alves', 'Analista de Dados', 'R$4000')")
        
    conn.commit()
    c.close()
    conn.close()

# Criar tabelas 
create_table()            

# inserir dados 
data_insert()

# Usando as variáveis para inserir dados 
def data_insert_var():
    new_date = datetime.datetime.now()
    new_funcionario_name = 'Isaac_Alves'
    new_programador_name = 'Analista_de_Dados'
    new_valor = random.randrange('4000')
    c.execute("INSERT INTO Programador(date, fucionario_name, programador_name, valor_salarial) '\
        VALUES (?, ?, ?, ?)", (new_date, new_funcionario_name, new_programador_name, new_valor))

    conn.commit()

# Leitura de dados 
def leitura_todos_dados():
    c.execute("SELECT * FROM PROGRAMADOR")
    for linha in c.fetchall():
        print(linha)

# leitura de registros específicos
def leitura_registros():
    c.execute("SELECT * FROM PROGRAMADOR WHERE valor salarial > R$4000")
    for linha in c.fetchall():
        print(linha) 

# leitura de colunas específicos
def leitura_colunas():
    c.execute("SELECT * FROM PROGRAMADOR")
    for linha in c.fetchall():
        print(linha[3]) 

# Update
def atualiza_dados():
    c.execute("UPDATE produtos SET valor = R$4000 WHERE valor_salarial = R$5000")
    conn.commit

# Delete
def remove_dados():
    c.execute("DELETE FROM produtos WHERE valor = 4000")
    conn.commit()

print(atualiza_dados)

# Select todos os dados 
print(leitura_todos_dados)

# Leitura de registros específicos 
print(leitura_registros())

# Leitura de colunas específicas 
print(leitura_colunas())

#Encerrando a conexão 
c.close()
conn.close() 


