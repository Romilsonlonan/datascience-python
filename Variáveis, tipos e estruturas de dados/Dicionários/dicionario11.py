"""
O método keys retorna o que o Python 3 chama de vista (view) das chaves. 
Podemos iterar sobre a vista ou transformar a vista em uma lista usando 
a função list de conversão.
"""

inventario = {'maçãs': 430, 'bananas': 312, 'laranjas': 525, 'pêras': 217}

for akey in inventario.keys(): # a ordem em que obtemos as chaves não está definida
    print("Tem chave", akey, "qual mapeia para valor", inventario[akey])

ks = list(inventario.keys())
print(ks)

for k in inventario:
    print("Peguei a chave", k)