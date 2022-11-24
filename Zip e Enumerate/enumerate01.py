"""
A função enumerate() retorna uma tupla de dois elementos a cada iteração: um número 
sequencial e um item da sequência correspondente. lista, não geram novas listas.
"""

# Criando uma lista 

seq = ['a', 'b', 'c']

# Ira retornar com Iterator com as demais funções zip, map e filter
# alterar o formato para list
print(enumerate(seq))

#retorna tuplas. Cada tupla retorna com o índice e o elemento 
print(list(enumerate(seq)))


