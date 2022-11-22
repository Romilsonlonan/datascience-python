import csv

with open('dataset/salario.csv','w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55,93,76))
    writer.writerow((62,14,86))


with open('dataset/salario.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)    