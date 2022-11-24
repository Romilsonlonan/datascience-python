#8 + 's'

"""
Traceback (most recent call last):
Traceback - rastrear) (última chamada mais recente):
  File(arquivo) "/home/romilson/Projetos e Treinamentos/DataScience-Python/Erros e Excessões/try_exception01.py", line 1, in <module>
    8 + 's'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
TypeError(Erro de Tipo(ou modelo(Type))): tipo(s) de operando não suportado(s) para +: 'int' e 'str'
"""

# Colocando o try(tentar) e except(exceto)

try:
    8 + 's'
except TypeError:
    print("Operação não permitida")

 