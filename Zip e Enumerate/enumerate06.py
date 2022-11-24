"""
A função enumerate() retorna uma tupla de dois elementos a cada iteração: um número 
sequencial e um item da sequência correspondente. lista, não geram novas listas.
"""

# Criando uma lista 

lista = ['Marketing', 'Tecnologia', 'Business']

for i, item in enumerate(range(10)):
    print(i, item)