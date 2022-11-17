"""
Len () é uma função integrada ao Python que é utilizada para obter o número 
de itens em um determinado objeto, string, array, listas, entre outros. É um 
método bastante utilizado no desenvolvimento de programas.

Similarmente, um novo carregamento de bananas pode ser tratado assim:
"""

inventario = {'kiwis': 430, 'bananas': 312, 'laranjas': 525, 'peras': 217}
inventario['bananas'] = inventario['bananas'] + 200
	
	
numItems = len(inventario)
print(inventario)