# Criando a classe cachorro 
class Cachorro():
    def __init__(self, raca):# <-- parâmetro raça
        # o __init__ é um método construtor.    
        self.raca = raca
        print("Construtor chamado para criar  um objeto desta classe")

# Criando um objeto(objeto Rex é um cãozinho) a partir da classe cachorro 
# 1 instância
Rex = Cachorro(raça='Labrador')

# Criando um objeto(objeto Rex é um cãozinho) a partir da classe cachorro
# 2 instância
Golias = Cachorro(raça='Huskie')

# Atributo da classe cachorro, utilizado pelo objeto criado 
print(Rex.raca)

# Atributo da classe cachorro, utilizado pelo objeto criado 
print(Golias.raca)

