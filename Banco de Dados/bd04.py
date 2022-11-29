import csv
import random
from sqlite3 import connect
import sqlite3
from tkinter.font import names


class PessoasDb(object):

    tb_name = 'pessoas'

    def __init__(self):
        self.db = connect('pessoas.db')
        self.tb_name

def criar_schema(self, schema_name='sql/pessoas_schema.sql'):
    print("Criando tabela %s ..." % self.tb_name)

    try:
        with open(schema_name, 'rt') as f:
            schema = f.read()
            self.db.cursor.executescript(schema)
    except sqlite3.Error:
        print("Aviso: A tabela %s já existe." % self.tb_name)
        return False

    print("Tabela %s criada com sucesso." % self.tb_name)

def inserir_de_csv(self, file_name='csv/cidades.csv'):
    try:
        c = csv.reader(
            open(file_name, 'rt'), delimiter=',')
        t = (c,)
        for t in c:
            self.db.cursor.execute("""
            INSERT INTO cidades (cidade, uf)
            VALUES (?,?)
            """, t)
        # gravando no bd
        self.db.commit_db()
        print("Dados importados do csv com sucesso.")
    except sqlite3.IntegrityError:
        print("Aviso: A cidade deve ser única.")
        return False 

def gen_cidade(self):
    ''' conta quantas cidades estão cadastradas e escolhe uma delas pelo id. '''
    sql = 'SELECT COUNT(*) FROM cidades'
    q = self.db.cursor.execute(sql)
    return q.fetchone()[0]

def inserir_randomico(self, repeat=10):
    lista = []
    for _ in range(repeat):
        fname = names.get_first_name()
        lname = names.get_last_name()
        email = fname[0].lower() + '.' + lname.lower() + '@email.com'
        cidade_id = random.randint(1, self.gen_cidade())
        lista.append((fname, lname, email, cidade_id))
    try:
        self.db.cursor.executemany("""
        INSERT INTO pessoas (nome, sobrenome, email, cidade_id)
        VALUES (?,?,?,?)
        """, lista)
        self.db.commit_db()
        print("Inserindo %s registros na tabela..." % repeat)
        print("Registros criados com sucesso.")
    except sqlite3.IntegrityError:
        print("Aviso: O email deve ser único.")
        return False

def ler_todas_pessoas(self):
    sql = 'SELECT * FROM pessoas INNER JOIN cidades ON pessoas.cidade_id = cidades.id'
    r = self.db.cursor.execute(sql)
    return r.fetchall()

def imprimir_todas_pessoas(self):
    lista = self.ler_todas_pessoas()
    for c in lista:
        print(c)

# myselect, imprime todos os nomes que começam com R
def meu_select(self, sql="SELECT * FROM pessoas WHERE nome LIKE 'R%' ORDER BY nome;"):
    r = self.db.cursor.execute(sql)
    self.db.commit_db()
    print('Nomes que começam com R:')
    for c in r.fetchall():
        print(c)

def table_list(self):
    # listando as tabelas do bd
    l = self.db.cursor.execute("""
    SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
    """)
    print('Tabelas:')
    for tabela in l.fetchall():
        print("%s" % (tabela))

def fechar_conexao(self):
    self.db.close_db()
    
                           