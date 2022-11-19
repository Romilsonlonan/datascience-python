# CONTANDO O NUMERO DE COLUNAS 

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
primeira_linha = lst[0]
count = 0
for column in primeira_linha:
    count = count + 1

print(count)
