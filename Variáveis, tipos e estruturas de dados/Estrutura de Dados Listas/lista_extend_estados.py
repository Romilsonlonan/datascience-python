# Criando uma lista estado com o operador extends 

"""
extend: Adiciona itens de uma estrutura iterável, por exemplo, 
se enviarmos um objeto puro, ele não sabe como adicionar, porém, 
se enviarmos esse mesmo objeto dentro de uma lista, ele varrerá 
a lista e adicionará esse objeto e, caso exista outros, os demais 
dentro da lista.
"""

estados = ["Brasília", "São Paulo", "Rio de Janeiro", "Minas-Gerais" ]
estados.extend(["Bahia", "Mato Grosso do Sul"])

print(estados)