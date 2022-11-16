# Da mesma forma que ocorre com strings, a função len retorna o comprimento de uma lista 
# (o número de elementos na lista). Entretanto, como listas podem conter itens que são listas, 
# é importante notar que len somente retorna o comprimento da lista mais externa. Em outras 
# palavras, sublistas de uma lista são consideradas como sendo um elemento simples quando 
# contamos o comprimento da lista.

uma_lista =  ["ola", 2.0, 5, [10, 20]]
print(len(uma_lista))
print(len(['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]))
