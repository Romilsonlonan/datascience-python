# Divisão de Matrizes

import numpy as np

A = np.array([[1,2,3],
            [4,5,6]])

B = np.array([[6,5,4],
            [3,2,1]])

# Divisão de Matrizes "tradicional"

divisao = A / B
print(divisao) 

# soma usando numpy

divisao = np.divide(A,B)
print(divisao)