# CONTANDO OS ITENS DE UMA LISTA 

"""
Python List count() é uma função embutida em Python que retorna a contagem de quantas 
vezes um determinado objeto ocorre em uma List . A função count() é usada para contar 
os elementos de uma lista e também de uma string. Parâmetros: O objeto são as coisas 
cuja contagem deve ser retornada.
"""

lista = [5, 6, 10, 13,17]
count = 0
for item in lista:
    count += 1

print(count) 