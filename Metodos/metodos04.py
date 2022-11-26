# Criando uma classe chamada Círculo 

class Circulo():

    #O valor do pi é constante
    pi = 3.14

    # Quando um objeto desta classe for criado, este método 
    # será executado e o valor default do raio será 5.
    def __init__(self, raio = 5):
        self.raio = raio

    # Esse método calcula a área. Self utiliza os atributos deste mesmo objeto 
    def area(self):
        return(self.raio * self.raio) * Circulo.pi

    # Método para gerar um novo raio 
    def setRaio(self, novo_raio):
        self.raio = novo_raio 

    # Método para obter o raio do círculo
    def get_Raio(self):
        return self.raio 

#Criando o objeto circ Uma isntancia da classe Circulo()
circ = Circulo()

# Executando um método da classe Circulo
print(circ.getRaio())

circ1 = Circulo(7)

print('O raio é: ', circ.getRaio())

print('A area igual a: ', circ.area())

print(circ.getRaio(3))

print('Novo raio é igual a: ', circ.getRaio())





