from pandas import DataFrame
import pandas as pd

data = {'Estado': ['Santa Catarina', 'Paraná', 'Goias', 'Bahia', 'Minas Gerais'], 
        'Ano': [2002, 2003, 2004, 2005,2006],
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)
print(frame)

type(frame)
print(type(frame))

DataFrame(data, columns= ['Ano', 'Estado', 'População'])

# Criando outro dataframe com os mesmos dados anteriores mas adicionando uma coluna 
frame2 = DataFrame(data, columns= ['Ano', 'Estado', 'População', 'Débito'],
                   index = ['um', 'dois', 'três', 'quatro', 'cinco'])

print(frame2)

frame2['Estado']
print(frame2['Estado'])
print(frame2['Ano'])
print(type(frame2))
print(type)
print(frame2.index)
print(frame2.columns)
print(frame2.values)
print(frame2.dtypes)
print(frame2.Ano)
print(frame2['Ano'])

# Imprimindo posições
print(frame2[:2])

# Importando o Numpy
import numpy as np 

# Usando o numpy para alimentar uma das colunas do dataframe 
frame2['Debito'] = np.arange(5.)
print(frame2)
frame2['Estado']
print(frame2['Estado'])
print(frame2['Ano'])
print(type(frame2))
print(type)
print(frame2.index)
print(frame2.columns)
print(frame2.values)
print(frame2.dtypes)
print(frame2.Ano)
print(frame2['Ano'])

# Resumo do Dataframe
frame2.describe()
print(frame2.describe())

frame2.loc['quatro']
print(frame2.loc['quatro'])

frame2.iloc[2]
print(frame2.iloc[2])

# Criando um dicionário 
web_stats = {'Dias':[1, 2, 3, 4, 5, 6, 7],
              'Visitantes': [45, 23, 67, 78, 23, 12, 14],
              'Taxas': [11, 22, 33, 44, 55, 66, 77]}

df = pd.DataFrame(web_stats)
print(df)

# Visualizando uma coluna index com objetivo de analisar 
print(df.set_index('Dias'))

# A função mostra as linhas originais do DataFrame  )
print(df.head())


