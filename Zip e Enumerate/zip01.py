"""
FUNÇÃO ZIP

Esta função retorna uma lista de tuplas, onde a i-ésima tupla contém o i-ésimo 
elemento de cada um dos argumentos.
"""

# Criando duas listas 

x = [1, 2, 3]
y = [4, 5, 6]

# Unindo as listas. Em python 3 retorna interator 
print(list(zip(x, y)))

# Perceba que zip retorna uma lista de tuplas.
#print(list(zip('ABCD', 'xy')))