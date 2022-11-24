# Criando 2 dicionaŕios 

d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

# Zip vai unir as chaves 
list(zip(d1, d2))

# Zip pode unir os valores (itens)
list(zip(d1, d2.values()))

print(list(zip(d1, d2)))
print(list(zip(d1, d2.values())))