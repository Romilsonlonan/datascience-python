# A sintaxe para acessar um elemento de uma lista é a mesma usada para acessar um 
# caractere de um string. Nós usamos o operador de indexação ( [] – não confundir 
# com a lista vazia). A expressão dentro dos colchetes especifica o índice. Lembrar 
# que o índice do primeiro elemento é 0. Qualquer expressão que tenha como resultado
# um número inteiro pode ser usada como índice e como com strings, índices negativos 
# indicarão elementos da direita para a esquerda ao invés de da esquerda para a direita.

numeros = [17, 123, 87, 34, 66, 8398, 44]
print(numeros[2])
print(numeros[9-8])
print(numeros[-2])
print(numeros[len(numeros)-1])