# Fazendo Slicing (fatiamento) em arrays

import numpy as np
import matplotlib.pyplot as plt

#Slicing
a = np.diag(np.arange(3))
print(a)

a[1, 1]
print(a[1,1])

a[1]
print(a[1])

b = np.arange(10)
print(b)

# [Start:end:step]
b[2:9:3]
print(b[2:9:3])

# Comparação 
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
a == b
print(a == b)

np.array_equal(a, b)
print(a.max())
print(a.min())

# Somando os elementos da array 
np.array([1, 2, 3]) + 1.5
print(np.array([1,2,3]) + 1.5)

b = np.around(a)
print(b)

B = np.array([1, 2, 3, 4])
print(B)

# Copiando uma array
C = B.flatten()
print(C)

# Criando uma array
v = np.array([1, 2, 3])

# Adicionando uma dimensão ao array
v[:, np.newaxis], v[:,np.newaxis].shape, v[np.newaxis,:].shape
print(v[:, np.newaxis], v[:,np.newaxis].shape, v[np.newaxis,:].shape)

# Repetindo os elementos de um array
print(np.repeat(v, 3))

# # Repetindo os elementos de um array
print(np.tile(v, 3))

# Criando um array 
w = np.array([5, 6])

# Concatenando
np.concatenate((v, w), axis=0) 
print(np.concatenate((v, w), axis=0))

# Copiando arrays
r = np.copy(v)
print(r)



