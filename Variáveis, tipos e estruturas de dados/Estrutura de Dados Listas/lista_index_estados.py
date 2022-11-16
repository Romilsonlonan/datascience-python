# Criando uma lista cidade com o operador index 

"""
index() A função index() retorna o index de determinado elemento. 
Se você procurar por um item que não existe um erro será lançado. 
Por tanto, se o seu objetivo é saber se um item pertence a lista 
utilize o operador de teste de inlclusão in .
"""

cidades = ["Brasília", "São Paulo", "Rio de Janeiro", "Minas-Gerais" ]
cidades.extend(["Bahia", "Mato Grosso do Sul"])
#cidades.index( 'Rio de Janeiro')

print(cidades.index("Rio de Janeiro"))
