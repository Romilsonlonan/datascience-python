# Reemove o arquivo com o banco de dados SQLlite (caso exista)
#import os
#os.remove("DataScience-Python.db") if os.path.exists("DataScience-Python.db") else None

# Importando os módulos de acesso ao SQLite
import sqlite3

# Cria uma conexão com o banco de dados.
# Se o banco de dados não existir, ele é criado neste momento 
con = sqlite3.connect("DataScience-Python.db")

# Tipo de conexão SQLite3
type(con)
print(type(con))

# Criando um cursor
# (Um cursor permite percorrer todos os registros em um conjunto de dados)
cur = con.cursor()

# Qual é o tipo(type) de banco de dados 
type(cur)
print(type(cur))

# cria uma instrução sql ou seja criando uma tabela com a linguagem SQL (Comando DDL(create table))
sql_create = 'create table cursos '\
'(id integer primary key, '\
'título varchar(100), '\
'categoria varchar(140))'

# Tipo de instrução criada str(String)
type(sql_create)
print(type(sql_create))

# Executando a instrução sql no cursor 
# chama a 'função execute' do 'objeto cur' e passa como 'parâmetro sql_create'  
#cur.execute(sql_create) 

# Criando outra sentença SQL para inserir registro
# insert into é uma instrução SQL, ou seja, instrução DML((Manilulação de linguagem) 
sql_insert = 'insert into cursos values (?, ?, ?)'

# Após o comando sql_insert informar os dados que serão inseridos
# também chamado de dataset. 
# Cada elemento da lista é uma tupla 
recset = [(1000, 'Ciência de Dados', 'Data Science'),
            (1001, 'Big Data Fundamentos', 'Big Data'),
            (1002, 'Python Fundamentos', 'Análise de Dados')]
    

# Inserindo os registros 
# fazendo um loop for 
for rec in recset:
    cur.execute(sql_insert, rec)

# Grava a transação 
con.commit()

# Criando outra setença SQL para selecionar registros
#sql_select = 'select * from cursos'

# Selecione todos os registros e recupera todos os registros   
#cur.execute(sql_select)
#dados = cur.fetchall()

# Listando o conteúdo do objeto dados 
#for linha in dados:
#    print('Curso Id: %d, Título: %s, Categoria: %s \n' % linha)

# Gerando outros registros 
#recset = [(1003, 'Gestão de Dados com MongoDB', 'Big Data'), 
#        (1004, 'R Fundamentos', 'Análise de Dados')]

# Inserindo outros registros
#for rec in recset:
#    cur.execute(sql_insert, rec)

# Gravando a transação 
#con.commit()

# Selecione todos os registros
#cur.execute('select * from cursos')

# Recupera os resultados 
#recset = cur.fetchall()

#for rec in recset:
#    print('Curso Id: %d, Título: %s, Categoria: %s \n' % rec)

# Fecha a conexão
#con.close()
