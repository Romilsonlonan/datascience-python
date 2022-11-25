"""
FUNÇÃO ZIP

Esta função retorna uma lista de tuplas, onde a i-ésima tupla contém o i-ésimo 
elemento de cada um dos argumentos.
"""

# Criando duas listas 

a = [1, 2, 3]
b = [4, 5, 6, 7, 8]

#Perceba que zip retorna uma lista de tuplas.
print(list(zip(a,b)))