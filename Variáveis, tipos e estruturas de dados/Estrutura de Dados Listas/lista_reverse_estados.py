# Criando uma lista estados com o operador reverse 

"""
A função reverse() inverte a ordem da lista mas sem ordena-la, ou seja, 
a ordem em que os elementos estão dispostos é indiferente, o que importa, 
é fazer com que o último seja o primeiro e vice-e-versa."""

estados = ["Brasília", "São Paulo", "Rio de Janeiro", "Minas-Gerais" ]
estados.extend(["Bahia", "Mato Grosso do Sul"])
estados.reverse()

print(estados)