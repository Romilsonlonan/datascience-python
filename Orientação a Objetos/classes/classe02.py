# Criando uma classe 

class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Estudante1 = Estudantes("Pele", 12, 9.5 )

# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe 
print(Estudante1.nome) 

# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe 
print(Estudante1.idade)

# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe 
print(Estudante1.nota)


