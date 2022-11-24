# Criando duas funções

from re import T

# Função 1 --> Recebe uma temperatura como parâmentro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return((float(9)/5)*T + 32)

# Função 2 --> Recebe uma temperatura como parâmentro e retorna a temperatura em Celsius
def celsius(T):
    return ((float(9)/5)*T + 32)

# Criando uma lista
temperaturas = [0, 22.5, 40, 100]

# Usando um loop for para imprimir o resultado da funçao map()
for temp in map(fahrenheit, temperaturas):

    print(temp)