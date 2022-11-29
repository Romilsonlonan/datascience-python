import numpy as np    

#np.__version__      
#print(np.__version__)                                                                                                                                                                                     

#help(np.array)
#print(help(np.array))

# Array criado a partir de uma lista:
vetor1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(vetor1)

# Um objeto do tipo ndarray é um recipiente multidimencional de intens do mesmo tipo e tamanho   
type(vetor1)
print(type(vetor1))

# Usando métodos do array numpy 
vetor1.cumsum()
print(vetor1.cumsum())

# Criando uma lista. Perceba como as listas e arrays são objetos diferentes, com diferentes propriedades 
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]

type(lst)
print(type(lst))

vetor1[0]
print(vetor1)

vetor1[0] = 100
print(vetor1)

# Não é possível incluir elemento de outro tipo 
# vetor1[0] = 'Novo Elemento'

# Verificando o formato do array 
print(vetor1.shape)