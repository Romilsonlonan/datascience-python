"""
O que são expressões Lambda no Python? As funções Lambda são chamadas de funções anônimas, mas o
que são elas? Nada mais são do que funções que o usuário não precisa definir, ou seja, não vai 
precisar escrever a função e depois utilizá-la dentro do código.
"""

# Criando uma lista
temperaturas = [0, 22.5, 40, 100]

# Aplicando a função a cada elemento da lista de temperaturas.
# Em python3, "a função map() retorna um interator" (<map at 0x111c28320>)
map(lambda x: (5.0/9)*(x - 32),temperaturas)

# A função map() retornando a lista de temperaturas convertidas em Fahrenheit  
list(map(lambda x: (5.0/9)*(x-32), temperaturas))

print ((list(map(lambda x: (5.0/9)*(x-32), temperaturas))))