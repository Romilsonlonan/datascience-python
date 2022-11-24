"""
Reduce() Esta função aplica uma operação em todos os elementos da lista reduzindo a apenas um 
elemento. 
"""

from functools import reduce
from IPython.display import Image
Image('arquivos/reduce.png')

lista = [47, 11, 42, 13]

def soma(a,b):
    x = a + b
    return x

reduce(soma, lista)

print(reduce(soma, lista))