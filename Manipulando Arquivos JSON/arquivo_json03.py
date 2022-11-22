# Criando um arquivo JSON
import pandas as pd
import json
import csv

dict = {'nome': 'Romilson Luis',
        'linguagem': 'Python',
        'similar': ['c', 'Modula-3', 'lisp'],
        'users': 10000000 
       }

with open('arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict))

with open('arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print (data)
print (data['nome'])
