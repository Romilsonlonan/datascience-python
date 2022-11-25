class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def listFunc(self):
        print("O nome do funcionário é: " + self.nome + " e o salário é R$" + str(self.salario))

# instânciar um objeto do tipo funcionários
# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Func1 = Funcionarios("Obama", 20000)

# Usando o método da classe
print(Func1.listFunc())

print("****Usando atributos****")

print(hasattr(Func1, "nome"))

print(hasattr(Func1, "salario"))

print(setattr(Func1, "salario", 4500))

print(hasattr(Func1, "salario"))