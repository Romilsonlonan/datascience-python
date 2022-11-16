# Criando uma lista cidades com o operador insert 

"""
o método insert (list insert python) insere um item numa 
posição específica dentro da lista. Na hora de colocar os 
argumentos você coloca o número do índice que o item será 
inserido e em seguida o valor a ser adicionado.
"""

cidades = ["Brasília", "São Paulo", "Rio de Janeiro", "Minas-Gerais" ]
cidades.extend(["Bahia", "Mato Grosso do Sul"])
cidades.insert(0, 'Amazonas(Adicionado a lista cidades)')

print(cidades)
