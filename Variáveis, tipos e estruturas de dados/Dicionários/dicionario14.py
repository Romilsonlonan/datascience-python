"""
O método sort() permite que você organize um dicionário em ordem ascendente ou descendente. Ele 
recebe argumentos somente nomeados: key e reverse . reverse determina se a lista é ordenada 
em ordem ascendente ou descendente. key é uma função que gera um valor intermediário para 
cada elemento.
"""

mydict = {"gato":12, "cachorro":6, "elefante":23, "urso":20}
keylist = list(mydict.keys())

keylist.sort()

print(keylist[3])