"""
A função enumerate() retorna uma tupla de dois elementos a cada iteração: um número 
sequencial e um item da sequência correspondente. lista, não geram novas listas.
"""

# Criando uma lista 

lista = ['Marketing', 'Tecnologia', 'Business']

for i, item in enumerate('Isso é uma string!!!'):
    print(i, item)