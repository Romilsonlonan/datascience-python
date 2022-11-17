"""
Dicionários também são mutáveis. Como vimos antes, com listas, isso significa que o dicionário pode
ser modificado pela referência a uma associação no lado esquerdo de um comando de atribuição. No 
exemplo anterior, em vez de excluir a entrada para peras, poderíamos ter definido o inventário para 0.
"""

inventario = {'kiwis': 430, 'bananas': 312, 'laranjas': 525, 'peras': 217}
	
inventario['peras'] = 0

print(inventario)