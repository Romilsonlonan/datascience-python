# Criando uma lista estados com o operador index 

"""
index() A função index() retorna o index de determinado elemento. 
Se você procurar por um item que não existe um erro será lançado. 
Por tanto, se o seu objetivo é saber se um item pertence a lista 
utilize o operador de teste de inlclusão in .
"""

estados = ["Brasília", "São Paulo", "Rio de Janeiro", "Minas-Gerais" ]
estados.extend(["Bahia", "Mato Grosso do Sul"])
#estados.index( 'Rio de Janeiro')

print(estados.index("Rio de Janeiro"))
