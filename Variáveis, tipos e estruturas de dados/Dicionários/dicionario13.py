"""
Este operador pode ser muito útil pois acessar uma chave inexistente em um dicionário provoca
um erro de execução. O método "get" nos permite acessar o valor associado a uma chave, similar 
ao operador []. A diferença importante é que get não irá causar um erro de execução se a chave 
não está presente. Ao invés disso, retorna "None". Existe uma variação de get que permite o 
retorno de um valor alternativo quando a chave não está presente.
"""

inventario = {'maçãs': 430, 'bananas': 312, 'laranjas': 525, 'pêras': 217}

print(inventario.get("maçãs"))
print(inventario.get("cerejas"))

print(inventario.get("cerejas",0))
