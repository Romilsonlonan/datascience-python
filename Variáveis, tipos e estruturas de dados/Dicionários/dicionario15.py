"""
O operador "in" verifica se o operando a sua esquerda, está contido na lista a sua direita, 
da mesma forma que o operador not in que verifica o contrário. Estes, são 2 operadores 
nativo para verificar se um determinado objeto está contido numa lista. A palavra "in", do 
Inglês, significa, "contido em"
"""

meu_dicionario = {"gato":12, "cachorro":6, "elefante":23, "urso":20}
if 'cachorro' in meu_dicionario:
    print(meu_dicionario['cachorro'])
else: 
    print("não temos o cachorro em meu dicionário")

# response: 6 dog é uma chave no dicionário.    

#meu_dicionario = {"gato":12, "cachorro":6, "elefante":23, "urso":20}
#if 'leão' in meu_dicionario:
#    print(meu_dicionario['cachorro'])
#else: 
#    print("não temos o cachorro em meu dicionário")

# response: não temos o cachorro como uma chave no dicionário    
    

