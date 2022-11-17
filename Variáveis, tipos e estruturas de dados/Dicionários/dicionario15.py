"""
O get() é um método usado para pegar o valor de uma dada chave em um dicionário se 
a chave estiver no dicionário, caso ela não exista, o método retorna None ou o valor 
padrão passado por parâmetro.
"""

# get retorna o valor associado com uma dada chave, assim o programa divide 12 por 6.

meu_dicionario = {"gato":12, "cachorro":6, "elefante":23, "urso":20}
if 'cachorro' in meu_dicionario:
    print(meu_dicionario['cachorro'])
else: 
    print("não temos o cachorro em meu dicionário")

#meu_dicionario = {"gato":12, "cachorro":6, "elefante":23, "urso":20}
#if 'leão' in meu_dicionario:
#    print(meu_dicionario['cachorro'])
#else: 
#    print("não temos o cachorro em meu dicionário")

# response: não temos o cachorro em meu dicionário    
    

