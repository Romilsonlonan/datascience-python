# Criando uma array 
import numpy as np
import matplotlib.pyplot as plt

A = np.array([15, 23, 63, 94, 75])
print(A)

#Em estatística a média é o valor que aponta  para onde mais se concentram os dados de uma distribuição. 
np.mean(A)
print(np.mean(A))

# O desvio padrão mostra o quanto de variação ou "dispersão" existe em ralação à média (ou valor esperado)
# Um baixo desvio padrão indica que os dados tendem a estar próximos da média.
# Um desvio padrão alto indica que os dados estão espalhados por uma gama de valores.
np.std(A)
print(np.std(A))

# Variança de uma variável aleatória é uma medida da sua dispersão estatistica, indicando "o quão longe"
# em geral os seus valores se encontram do valor esperado 
np.var(A)
print(np.var(A))


# Criando um outro array usando a função arange
d = np.arange(1, 10)
print(d)

# Pode ser utilizado para cálculo de frequência 
np.sum(d)
print(np.sum(d))

# Retorna o produto dos elementos desse meu array
np.prod(d)
print(np.prod(d))

# Soma acumulada dos elementos 
np.cumsum(d)
print(np.cumsum(d))

a = np.random.randn(400, 2)
m = a.mean(0)
print (m, m.shape)

plt.plot(a[:,0], a[:,1], 'o', markersize=5, alpha=0.50)
plt.plot(m[0], m[1], 'ro', markersize=10)
plt.show()


