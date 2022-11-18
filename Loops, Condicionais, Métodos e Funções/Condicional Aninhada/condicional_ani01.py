"""
Estrutura Condicional Aninhada. Estruturas Codicionais Aninhadas são várias condições em cascatas, 
ou seja, um IF dentro de outro IF. Uma outra estrutura de aninhamento é como pode-se notar abaixo. 
Incrementando o nosso exemplo, agora teremos que exibir uma mensagem caso o valor seja igual a Zero.
"""
x = 0 
y = 0

if x == y:
    print('x e y são iguais')
else:
    if x < y:
        print('x é menor que y')
    else:
        print('x é maior que y')