# Unindo listas no Python
# Para unir duas listas podemos simplesmente utilizar o símbolo de +

lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000,20000,50000]
resultados=[]

for i in range(3):
   tupla=(lojas[i],vendas[i])
   resultados.append(tupla)
print(resultados)
[('Rio de Janeiro', 10000), ('São Paulo', 20000), ('Curitiba', 50000) ]

