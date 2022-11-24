"""
A função enumerate() retorna uma tupla de dois elementos a cada iteração: um número 
sequencial e um item da sequência correspondente. lista, não geram novas listas.
"""

# Criando uma lista 

seq = ['a', 'b', 'c']

for indice, valor in enumerate(seq):
    if indice >=2:
        break
    else:
        print(valor)
    
