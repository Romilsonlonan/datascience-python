# Subtração de Matrizes

import numpy as np

A = np.array([[1,2,3],
            [4,5,6]])

B = np.array([[6,5,4],
            [3,2,1]])

# soma tradicional

subtracao = A - B
print(subtracao) 

# Subtracão usando numpy

subtracao = np.subtract(A,B)
print(subtracao)