"""
Nesse código em específico estamos abrindo o arquivo em formato de leitura (por isso o “r”) 
e estamos utilizando o comando csv.reader que é para ler o arquivo desejado em formato csv 
e estamos inserindo qual o delimitador desse arquivo.
""" 
import csv

with open('dataset/salario.csv','r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabeçalho: " + str(linha))
        else:

            print("Valor: " + str(linha))
