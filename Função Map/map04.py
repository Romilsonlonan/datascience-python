# Criando uma lista
temperaturas = [0, 22.5, 40, 100]

# Aplicando a função a cada elemento da lista de temperaturas.
# Em python3, "a função map() retorna um interator" (<map at 0x111c28320>)
map(lambda x: (5.0/9)*(x - 32),temperaturas)

# A função map() retornando a lista de temperaturas convertidas em Fahrenheit  
list(map(lambda x: (5.0/9)*(x-32), temperaturas))

print ((list(map(lambda x: (5.0/9)*(x-32), temperaturas))))