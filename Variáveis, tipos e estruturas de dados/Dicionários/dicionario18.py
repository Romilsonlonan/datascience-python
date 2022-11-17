"""
Como os dicionários são mutáveis, você precisa estar ciente de apelidos (ou aliasing, como vimos 
com listas). Sempre que duas variáveis se referem ao mesmo objeto no dicionário, a mudança de uma 
afeta a outra. Por exemplo, opposites é um dicionário que contém pares de opostos.
"""

opostos = {'para cima': 'para baixo', 'certo': 'errado', 'verdadeiro': 'falso'}
alias = opostos

print(alias is opostos)

alias['direita'] = 'esquerda'
print(opostos['direita'])