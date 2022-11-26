class Livro():
    def __init__(self, titulo, autor, paginas):
        print("Livro criado")
        self.titulo = titulo
        self.autor = autor 
        self.paginas = paginas 

    # __str__ retorna um texto
        """
__      str__ é um método especial, como __init__ , usado para retornar uma representação de string 
        de um objeto. Quando escrevo uma nova classe, quase sempre começo escrevendo __init__ , o 
        que facilita a instanciação de objetos, e __str__ , que é útil para a depuração.
        """
    def __str__(self):
        return "Título: %s, autor: %s, páginas: %s " \
            %(self.titulo, self.autor, self.paginas)

    def __len__(self):
        return self.paginas

    def len(self):
        return print("Páginas do livro com métodos comum: ", self.paginas)


livro1 = Livro("Os Lusíadas", "Luis de Camões", 8816)

# Métodos especiais 
print(livro1)
str(livro1)

len(livro1)
print(len(livro1))

livro1.len()
print(livro1.len())

# Ao executar a função del para remover um atributo, o Python executa:
# livro1.__delattr__("paginas")
del livro1.paginas

hasattr(livro1, "páginas")
print(hasattr(livro1, "páginas"))