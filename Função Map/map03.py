# Criando duas funções 

# Função 1 --> Recebe uma temperatura como parâmentro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return((float(9)/5)*T + 32)

# Função 1 --> Recebe uma temperatura como parâmentro e retorna a temperatura em Celsius
def celsius(T):
    return ((float(9)/5)*T + 32)

# Criando uma lista
temperaturas = [0, 22.5, 40, 100]

# Aplicando a função a cada elemento da lista de temperaturas.
# Em python3, "a função map() retorna um interator" (<map at 0x111c28320>)
#map(fahrenheit, temperaturas)

# A função map() retornando a lista de temperaturas convertidas em Fahrenheit  
#list(map(fahrenheit, temperaturas))

print(list(map(fahrenheit, temperaturas)))