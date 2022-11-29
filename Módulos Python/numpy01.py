import numpy as np    

# A função arange cria um vetor contendo uma progressão aritmético a partir de um intervalo - start, stop, step
vetor2 = np.arange(0., 4.5, .5)
print(vetor2)

type(vetor2)
print(type(vetor2))

# Formato do array 
np.shape(vetor2)

print(np.shape(vetor2))
#(9,) --> objeto unidimencional  

# Chamando o atributo do objeto 
print(vetor2.dtype)

# Criando uma array
x = np.arange(1, 10, 0.25)
print(x)

# Criar uma arrays com a função zeros
print(np.zeros(10))

# Retorna 1 nas posições em diagonal e 0 no restante 
z = np.eye(3)
print(z)

# Os valores passados como parâmetros, formam uma diagonal 
d = np.diag(np.array([1, 2, 3, 4]))
print(d)

c = np.array([1+2j, 3+4j, 5+6*1j])
print(c)

# Array de valores booleanos
b = np.array([True, False, False, True])
print(b)

s = (['Python', 'R', 'Romilson'])
print(s)


# O método linspace (linearly spaced vector) retorna um numero de 
# valores igualmente distribuídos no intervarlo especificado 
np.linspace(0, 10)
print(np.linspace(0, 10))

print(np.linspace(0, 10, 15))

print(np.logspace(0, 5, 10))






