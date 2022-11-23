"""
O Python random é um módulo que faz parte da linguagem Python e é utilizado para gerar 
números pseudo-aleatórios. Também podemos selecionar os elementos de uma lista de forma 
aleatória ou exibir o seu resultado embaralhado.

O método sample() é definido no módulo aleatório do Python. É usado para obter uma lista
de comprimento aleatório de elementos únicos. Podemos fornecer o comprimento da lista 
final e ela selecionará alguns elementos aleatórios da sequência ou conjunto fornecido. 
Observe que os elementos da lista fornecida não precisam ser exclusivos. Se contiver 
algum elemento duplicado, o resultado final poderá selecionar duplicatas. Neste post, 
aprenderemos como o método sample funciona com diferentes exemplos.
"""

import random
dataTuple = (1, 2, 3, 'four', 'five' , 6)
print(random.sample(dataTuple,2))