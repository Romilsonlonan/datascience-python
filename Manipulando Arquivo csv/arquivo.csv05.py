from sys import displayhook
import pandas as pd 
import csv

tabela = pd.read_csv("dataset/salario.csv", sep=",")
displayhook(tabela)