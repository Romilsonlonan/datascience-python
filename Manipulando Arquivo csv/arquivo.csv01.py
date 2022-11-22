# Gravando o arquivo com a função writer e fazendo a leitura com a função redear 
import pandas as pd
import csv

with open('dataset/salario.csv','w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55,93,76))
    writer.writerow((62,14,86))


with open('dataset/salario.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print('Número de colunas:', len(x))
        print(x)

