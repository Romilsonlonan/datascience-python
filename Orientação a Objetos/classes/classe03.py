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

# O objete func1 tem atributo nome?
print(hasattr(Func1, "nome"))

# O objeto func1 tem atributo salário?
print(hasattr(Func1, "salario"))

# a partir do objeto func1 verifique o salário e defina a ele o novo valor de atributo
print(setattr(Func1, "salario", 4500))

# obtenha esse atributo a partir do objeto 
print(getattr(Func1, "salario"))

# delete o objeto 
print(delattr(Func1, "salario"))

# verifique ou não se exite o objeto
print(hasattr(Func1, "nome"))


