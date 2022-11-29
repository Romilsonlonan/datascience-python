import sqlite3
import random
import time
import datetime
#import os

#os.remove('SDC_Academy.db') if os.path.exists('SDC_Academy.db') else None


# Criando uma conexão 
conn = sqlite3.connect('SDC_Academy.db')

# Criando um cursor 
cur = conn.cursor()

# Função para criar uma tabela 
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS Programador(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
        'funcionario_name TEXT, programador_name TEXT, valor_salarial  REAL)')

# Função para inserir um linha 
def data_insert():
#    c.execute("INSERT INTO Programador VALUES(002, '2022-11-30 08:00:20', 'Pedro', 'Supervidor Técnico', 'R$8000')")
#    c.execute("INSERT INTO Programador VALUES(003, '2022-11-30 08:00:20', 'Guilherme', 'Lider Técnico', 'R$6000')")
    cur.execute("INSERT INTO Programador VALUES(004, '2022-11-30 08:00:20', 'Romilson Luis', 'Analista de Dados', 'R$4000')")
    conn.commit()
    cur.close()
    conn.close()

# Criar tabelas 
create_table()            

# inserir dados 
data_insert()

def data_insert_var():
    new_date = datetime.datetime.now()
    new_funcionarios_name = 'Romilson'
    new_programadores_name = 'Analista de dados'
    new_valor = random.randrange('R$4000')
    c.execute("INSERT INTO Programador(date, fucionario_name, programador_name, valor_salarial) '\
        VALUES (?, ?, ?, ?)", (new_date, new_funcionarios_name, new_programadores_name, new_valor))

conn.commit()

# Gerando valores e inserindo na tabela 
for i in range(10):
    data_insert_var()
    time.sleep(1)


cur.close()
conn.close()



