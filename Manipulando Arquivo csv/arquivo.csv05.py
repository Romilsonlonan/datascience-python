"""
sep='separador' – Especifica como os objetos serão separados, se houver mais do que um. O padrão 
é um espaço em branco. end='caractere' – Especifica o caractere que é impresso no final da linha. 
O padrão é \n, uma quebra de linha.

função sum() em Python

A soma dos números na lista é necessária em todos os lugares. Python fornece uma função embutida
sum() que resume os números da lista. Sintaxe: sum (iterable, start) iterable: iterable pode ser 
qualquer lista, tuplas ou dicionários, mas o mais importante, devem ser números.
"""

from sys import displayhook
import pandas as pd 
import csv

tabela = pd.read_csv("dataset/salario.csv", sep=",")
displayhook(tabela)

print(tabela['terceira'].sum())