"""
A função enumerate() retorna uma tupla de dois elementos a cada iteração: um número 
sequencial e um item da sequência correspondente. lista, não geram novas listas.
"""

lista = ["p", "y", "t", "h", "o", "n"]

for item in lista:
    print(item)


for key, value in enumerate(["p", "y", "t", "h", "o", "n"]):
    print(key, value)
