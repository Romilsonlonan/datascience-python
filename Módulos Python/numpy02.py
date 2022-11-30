import numpy as np

# Criando uma matriz
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
print(matriz.shape)

# Criando uma matriz 2x3 apenas com o numero "1"
matriz1 = np.ones((2,3))
print(matriz1)

# Criando uma matriz a partir de uma lista de listas 
lista = [[13, 81, 22], [0, 34, 59], [21, 48, 94]]

matriz2 = np.matrix(lista)
print(matriz2)

type(matriz2)
print(type(matriz2))

# formato da matriz
np.shape(matriz2)
print(np.shape(matriz2))

matriz2.size
print(matriz2.size)

print(matriz2.dtype)

matriz2.itemsize
print(matriz2.itemsize)

matriz2.nbytes
print(matriz2.nbytes)

print(matriz2[1, 2])

matriz2[1, 0] = 100
print(matriz2)

x = np.array([1,2]) # Numpy decide o tipo dos dados 
y = np.array([1.0, 2.0]) # Numpy decide o tipo dos dados
z = np.array([1, 2], dtype=np.float64) #Forçamos um tipo de dado em particular
print(x.dtype, y.dtype, z.dtype)

matriz3 = np.array([[24, 76], [35, 89]], dtype=float)
print(matriz3)
print(matriz3.itemsize)
print(matriz3.nbytes)












                  