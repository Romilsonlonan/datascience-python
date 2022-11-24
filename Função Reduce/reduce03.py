from functools import reduce

lst = [47, 11, 42, 13] 

# Podemos atribuir a expressão lambda a uma variável  
max_find2 = lambda a,b: a if(a > b) else b

type (max_find2)

# reduzindo a lista até o valor máximo, através da função criada com a expressão lambda   
print(reduce(max_find2, lst))