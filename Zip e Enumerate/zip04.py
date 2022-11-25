"""
FUNÇÃO ZIP

Esta função retorna uma lista de tuplas, onde a i-ésima tupla contém o i-ésimo 
elemento de cada um dos argumentos.
"""

# Criando 2 dicionaŕios 

d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

# Zip vai unir as chaves 
list(zip(d1, d2))

# Zip pode unir os valores (itens)
list(zip(d1, d2.values()))

print(list(zip(d1, d2)))
print(list(zip(d1, d2.values())))