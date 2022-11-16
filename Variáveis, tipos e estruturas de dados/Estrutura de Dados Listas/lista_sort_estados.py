# Criando uma lista estados com o operador sort 

"""
O método sort() permite que você organize uma lista em ordem 
ascendente ou descendente. Ele recebe argumentos somente nomeados:
key e reverse . reverse determina se a lista é ordenada em ordem 
ascendente ou descendente. key é uma função que gera um valor 
intermediário para cada elemento."""

estados = ["Brasília", "São Paulo", "Rio de Janeiro", "Minas-Gerais" ]
estados.extend(["Bahia", "Mato Grosso do Sul"])
estados.sort()

print(estados)
