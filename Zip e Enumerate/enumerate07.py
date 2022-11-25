"""
A função enumerate() retorna uma tupla de dois elementos a cada iteração: um número 
sequencial e um item da sequência correspondente. lista, não geram novas listas.
"""

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

# retorna um objeto iterável, aplicar para list
print (enumerate(seasons))
# <enumerate object at 0x7f0bc054c5c0>

print (list(enumerate(seasons)))



