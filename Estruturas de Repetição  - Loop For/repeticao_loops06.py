# Operando valores de uma lista com o loop for 

"""
double: armazena números com ponto flutuante, com precisão dupla, 
ou seja normalmente possui o dobro da capacidade de uma variável 
do tipo float.
"""

listaB = [32, 53, 85, 10, 15, 17, 19]
soma = 0 

for i in listaB:
    # Variável local double_i
    double_i = i * 2
    soma += double_i
    # A variável soma é adicionado na variável double_i e o resultado será gravado na variável soma

print(soma)