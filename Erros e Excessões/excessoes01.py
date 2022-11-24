# Excessão

def numDiv (num1, num2):
    resultado = num1 / num2
    print(resultado)

print(numDiv(4,2))

#resultado 2.0 --> ok

print(numDiv(4,0)) # --> excessão
"""
 File "/home/romilson/Projetos e Treinamentos/DataScience-Python/Erros e Excessões/erroexcessoes02.py", line 4, in numDiv
    resultado = num1 / num2
ZeroDivisionError: division by zero
"""

# Python não sabe dividir um numero por 0 e por isso terá que ser tratado com os comandos Try, Exception e Finally
