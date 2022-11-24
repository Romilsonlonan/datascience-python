# Criando 2 dicionaŕios 

d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

# Zip vai unir as chaves 
list(zip(d1, d2))

# Zip pode unir os valores (itens)
list(zip(d1, d2.values()))

def trocaValores(d1, d2):
    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val
    return dicTemp

print(trocaValores(d1, d2))        


