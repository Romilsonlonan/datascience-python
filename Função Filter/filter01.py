"""
A função filter() fornece uma forma de filtrar valores que muitas vezes pode ser mais eficiente 
do que uma compreensão de lista, especialmente quando começamos a trabalhar com conjuntos de 
dados maiores
"""

def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

filter(verificaPar, lista)
# <filter at 0x110a8feb8>
# As funçãos Map() e a Função Filter() retornan iterator e tem que ser convertidas para lista

print(list(filter(verificaPar, lista)))