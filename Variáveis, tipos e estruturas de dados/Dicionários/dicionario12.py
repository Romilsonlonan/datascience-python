"""
os tuplas são muitas vezes úteis para obter tanto a chave quanto o valor ao mesmo tempo, 
enquanto você está iterando no laço. Os dois laços fazer a mesma coisa. Os operadores in 
e not in podem testar se uma chave está no dicionário:
"""

inventario = {'maçãs': 430, 'bananas': 312, 'laranjas': 525, 'pêras': 217}
print('maçãs' in inventario)
print('cerejas' in inventario)

if 'bananas' in inventario:
     print(inventario['bananas'])
else:
     print("Não temos bananas")