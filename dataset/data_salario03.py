import pandas as pd 

file_name = "dataset/salario.csv"

df = pd.read_csv(file_name)

df.head() 

print(df)