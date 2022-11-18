"""
Estruturas Codicionais Aninhadas são várias condições em cascatas, ou seja, um IF dentro de outro IF. 
Uma outra estrutura de aninhamento é como pode-se notar abaixo. Incrementando o nosso exemplo, agora 
teremos que exibir uma mensagem caso o valor seja igual a Zero.
"""

soma = 0

if soma > 0:
     print ("Maior que Zero.")
elif soma == 0:
     print ("Igual a Zero.")
else:
     print ("Menor que Zero.")