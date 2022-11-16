# Unindo listas no Python
# Usando range para rodar o for. i é uma variável auxiliar que irá percorrer a posição 0, 1 e 2 da nossas listas. Range(3) 

lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000,20000,50000]
resultados=[]

for i in range(3):
   tupla=(lojas[i],vendas[i])
   resultados.append(tupla)
print(resultados)
[('Rio de Janeiro', 10000), ('São Paulo', 20000), ('Curitiba', 50000) ]

