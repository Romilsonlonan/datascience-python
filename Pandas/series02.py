from pandas import Series
import pandas as pd

pd.__version__
print(pd.__version__)

# Criando uma série sem especificar os índices 
Obj = Series([67, 78, -56, 13])
print(Obj)

print(type(Obj))
print(Obj.values)
print(Obj.index)

Obj2 = Series([67, 78, -56, 13], index = ['a', 'b', 'c', 'd'])
print(Obj2)
print(Obj2.values)
print(Obj2.index)

Obj2['b']
print(Obj2['b'])

'd' in Obj2
print('d' in Obj2)

