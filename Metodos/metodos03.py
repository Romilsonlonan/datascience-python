"""
copy_list() Retorna uma cópia superficial de uma lista. Uma cópia superficial significa que 
se modificarmos qualquer um dos elementos da lista aninhada, as alterações serão refletidas 
na lista, pois apontam para a mesma referência. 
"""

first_list = []
copy_list = []

first_list.append(1)
first_list.append(2)
first_list.append(3)
first_list.append(4)
first_list.append(5)

copy_list = first_list.copy()

print("Original list ",first_list)
print("Copied list ",copy_list)
