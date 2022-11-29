import sqlite3
import random
import datetime
import matplotlib.pyplot as plt
from sqlite3 import connect

#import os
#os.remove('dsa.db') if os.path.exists('dsa.db') else None

# Criando uma conexão 
conn = sqlite3.connect('dsa.db')

type(conn)
print(type(conn))

# Criando um cursor 
cur = conn.cursor

type(cur)
print(type(cur))


# Função para criar uma tabela 
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
    'prod_name TEXT, valor REAL)')

#type(create_table())
print(type(create_table()))

# Função para inserir uma linha 
def data_insert():
    cur.execute("INSERT INTO produtos VALUES(now 'Teclado', 130 )")
    conn.commit()
    cur.close()
    conn.close()

#type(data_insert())
#print(type(data_insert()))

# Usando variáveis para inserir dados 
#def data_insert_var():
#    new_date = datetime.datetime.now()
#    new_prod_name = 'Monitor'
#    new_valor = random.randrange(50, 100)
#    cur.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?, ?)", 
#        (new_date, new_prod_name, new_valor))

#    conn.commit()

#type(data_insert_var())
#print(type(data_insert_var()))

# leitura de dados 
#def leitura_todos_dados():
#    curn.execute("SELECT *FROM PRODUTOS")
#    for linha in c.fetchall():
#        print(linha)

#type(leitura_todos_dados())
#print(type(leitura_todos_dados()))


# leitura de registro específicos
#def leitura_registros():
#    cur.execute("SELECT * FROM PRODUTOS WHERE VALOR > 60.0")
#    for linha in c.fetchall():
#        print(linha)

#type(leitura_registros())
#print(type(leitura_registros()))


# Leitura de colunas específicos
#def leitura_colunas():
#    cur.excute("SELECT * FROM PRODUTOS")
#    for linha in c.fetchall():
#        print(linha[3])

# Update 
#def atualiza_dados():
#    cur.execute("UPDATE produtos SET valor = 70.00 WHERE valor > 80.0")
#    conn.commit

#Delete
#def remove_dados():
#    cur.execute("DELETE FROM produtos WHERE valor = 62.0")
#    conn.commit


# Gerar gráficos com os dados com o banco de dados 
#def dados_grafico():
#    cur.execute("SELECT id, valor FROM produtos")
#    ids = []
#    valores = []
#    dados = c.fetchall()
#    for linha in dados:
#        ids.append(linha[0])
#        valores.append(linha[0])
#    plt.bar(ids, valores)
#    plt.show()

#    dados_grafico() 
#print(dados_grafico())




