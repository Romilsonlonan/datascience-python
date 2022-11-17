"""
O operador "GET" pode ser muito útil pois acessar uma chave inexistente em um dicionário provoca
um erro de execução. O método "get" nos permite acessar o valor associado a uma chave, similar 
ao operador []. A diferença importante é que get não irá causar um erro de execução se a chave 
não está presente. Ao invés disso, retorna "None". Existe uma variação de get que permite o 
retorno de um valor alternativo quando a chave não está presente.
"""

mydict = {"gato":12, "cachorro":6, "elefante":23, "urso":20}

resposta = mydict.get("gato")//mydict.get("cachorro")

print (resposta)

# response 2 -> get retorna o valor associado com uma dada chave, assim o programa divide 12 por 6.

