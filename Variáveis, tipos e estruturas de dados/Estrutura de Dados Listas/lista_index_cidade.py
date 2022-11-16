# Criando uma lista cidade com o operador index 

"""
extend: Adiciona itens de uma estrutura iterável, por exemplo, 
se enviarmos um objeto puro, ele não sabe como adicionar, porém, 
se enviarmos esse mesmo objeto dentro de uma lista, ele varrerá 
a lista e adicionará esse objeto e, caso exista outros, os demais 
dentro da lista.
"""

cidades = ["Brasília", "São Paulo", "Rio de Janeiro", "Minas-Gerais" ]
cidades.extend(["Bahia", "Mato Grosso do Sul"])
#cidades.index( 'Rio de Janeiro')

print(cidades.index("Rio de Janeiro"))
