from pandas import Series
import pandas as pd

# Criando uma 'série' de dados passando um 'dicionário' como parâmetro 
dict = {'Futebol':5200, 'Tenis': 698, 'Voleibol':1550}
Obj3 = Series(dict)
Obj3 
print(Obj3)

print(type(Obj3))

# Criando uma "lista"
esportes = ['Futebol', 'Tenis', 'Natação', 'Basquetebol']

# Criando uma serie e usando uma lista como índice
Obj4 = Series(dict, index=esportes)
print(Obj4)
print(Obj4.values)
print(Obj4.index)
print(type(Obj4))


print(pd.isnull(Obj4))
pd.isnull(Obj4)

pd.notnull(Obj4)
print(pd.notnull(Obj4))

print(Obj3 + Obj4)

# Alterando o nome do índice e do objeto (Series) do pandas
Obj4.name = 'população'
Obj4.index.name = 'esporte'
print(Obj4)