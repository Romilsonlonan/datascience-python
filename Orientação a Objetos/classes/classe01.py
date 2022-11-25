# Criando uma class chamada livro 

class Livro():
    # Este método vai inicializar cada objeto criado a partir desta classe 
    # O nome deste método é __init__
    # (self) é uma referência a cada atributo de um objeto criado a apartir desta classe 
    def __init__(self):
        # o __init__ é um método construtor.
        """
        Esse método é especial porque é, geralmente, o primeiro definido em toda classe. 
        O motivo de ser especial é que ele sempre é executado quando criamos uma instância 
        de um objeto. Automaticamente o Python invoca o __init__() quando você cria um objeto.

        Com a palavra-chave self conseguimos acessar os atributos e métodos de uma classe em 
        Python. Ela é responsável por vincular os atributos com os argumentos enviados para uma 
        função ou método. O python utiliza essa palavra pois não há a sintaxe @ ou this para 
        referenciar os atributos de instância.
        """
        # Atributos de cada objeto criado a partir desta classe.
        # O self indica que estes são atributos dos objetos 
        self.titulo = 'O monge e o executivo' # <--- recebendo os atributos
        self.isbn = 9988888   #<--- recebendo os atributos
        print("Construtor chamado para criar um objeto desta classe")

    #   Métodos são funções, que recebem como parâmetro atributos do objeto criado 
    def imprime(self):
        print("Foi criado o livro %s e ISBN %d" %(self.titulo, self.isbn))   

# criando uma instância de classe livro 
Livro1 = Livro()

# Tipo de Objeto Livro
type(Livro1) 

# Atributo(título) do objeto Livro1
Livro1.titulo

# Método do objeto livro1
Livro1.imprime()

