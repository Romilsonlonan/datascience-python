"""
O que são expressões Lambda no Python? As funções Lambda são chamadas de funções anônimas, mas o
que são elas? Nada mais são do que funções que o usuário não precisa definir, ou seja, não vai 
precisar escrever a função e depois utilizá-la dentro do código.
"""

a = [1, 2, 3, 4] 
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]

print(list(map(lambda x,y,z:x+y+z, a,b,c )))