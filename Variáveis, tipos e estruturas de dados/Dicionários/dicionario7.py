"""
O comando "del" remove um par chave-valor de um dicionário. Por exemplo, o seguinte 
dicionário contém os nomes de várias frutas e o número de cada fruta em estoque. 
Se alguém compra todas as peras, podemos remover a entrada do dicionário.
"""

inventario = {'kiwis': 430, 'bananas': 312, 'laranjas': 525, 'peras': 217}
del inventario['peras']

print(inventario)