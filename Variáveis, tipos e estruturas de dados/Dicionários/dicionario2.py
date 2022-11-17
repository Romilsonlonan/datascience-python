"""
Se for necessário excluir um determinado item do dicionário, 
basta usarmos o método pop(), que irá receber a key de deletar
 o item com a chave indicada.
"""

my_dict = {"a": 1, "b": 2}
x = my_dict.pop("a")
print(x)

print(my_dict)
