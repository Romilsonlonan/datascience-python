
# Criando a classe Livro com parâmentro no "método construtor" 

class Livro():
    def __init__(self, titulo, isbn):
        # o __init__ é um método construtor.
        """
        Um método é uma função que “pertence” a um objeto instância. (Em Python, o termo 
        método não é aplicado exclusivamente a instâncias de classes definidas pelo usuário:
        """
        self.titulo = titulo
        self.isbn = isbn 
        print("Construtor chamado pra criar um objeto desta classe")

    def imprime(self, titulo, isbn):
        print("Este é o livro %s e ISBN %d" %(titulo,isbn ))  

# Criando o objeto Livro2 que é uma instância da classe Livro 
Livro2 = Livro("A menina que roubava livros", 77886611)

# Atributo do objeto Livro2
Livro2.titulo

# Método do objeto Livro2
Livro2.imprime("A menina que roubava livros", 77886611)

