"""
Como os dicionários são mutáveis, você precisa estar ciente de apelidos (ou aliasing, como vimos 
com listas). Sempre que duas variáveis se referem ao mesmo objeto no dicionário, a mudança de uma 
afeta a outra. Por exemplo, opposites é um dicionário que contém pares de opostos.

definição de aliasing:

Uma palavra sobre nomes e objetos. Objetos têm individualidade, e vários nomes (em diferentes escopos) 
podem ser vinculados a um mesmo objeto. Isso é chamado de “aliasing” em outras linguagens. (N.d.T. 
aliasing é, literalmente, “apelidar”: um mesmo objeto pode ter vários nomes.)
"""

opostos = {'para cima': 'para baixo', 'certo': 'errado', 'verdadeiro': 'falso'}
alias = opostos

print(alias is opostos)

alias['direita'] = 'esquerda'
print(opostos['direita'])