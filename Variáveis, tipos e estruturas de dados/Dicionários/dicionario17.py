"""
O for é utilizado para percorrer ou iterar sobre uma sequência de 
dados (seja esse uma lista, uma tupla, uma string), executando um 
conjunto de instruções em cada item. Como você já sabe, o Python 
utiliza identação para separar blocos de código: nos loops utilizando 
for não é diferente

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Utilizamos o comando if para verificar uma expressão e executar um bloco 
de código caso a condição definida seja verdadeira. É importante dizer que 
a instrução if pode ser utilizada sozinha, ou seja, apenas para executar 
algo se a condição for verdadeira.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

O operador in verifica se o operando a sua esquerda, está contido na lista a 
sua direita, da mesma forma que o operador not in que verifica o contrário. 
Estes, são 2 operadores nativo para verificar se um determinado objeto está 
contido numa lista. A palavra in, do Inglês, significa, "contido em".
"""

total = 0
meu_dicionario = {"gato":12, "cachorro":6, "elefante":23, "urso":20}
for akey in meu_dicionario:
    if len(akey) > 3:
        total = total + meu_dicionario[akey]
    print(total)

# O laço for itera sobre as chaves. Ele soma os valores das chaves que tem comprimento maior que 3.