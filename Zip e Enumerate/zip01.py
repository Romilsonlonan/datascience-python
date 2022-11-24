# Criando duas listas 

x = [1, 2, 3]
y = [4, 5, 6]

# Unindo as listas. Em python 3 retorna interator 
print(list(zip(x, y)))

# Perceba que zip retorna uma lista de tuplas.
#print(list(zip('ABCD', 'xy')))