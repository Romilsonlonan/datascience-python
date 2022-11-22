# Convertendo o dicionário para um objeto JSON

import json

dict = {'nome': 'Romilson Luis',
        'linguagem': 'Python',
        'similar': ['c', 'Modula-3', 'lisp'],
        'users': 10000000 
        }

json.dumps(dict)
print(dict)