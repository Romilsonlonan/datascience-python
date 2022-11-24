"""
Segundo a documentação do Python há pelo menos dois tipos distintos de erros: erros de sintaxe 
e exceções. Os erros de sintaxe apontam para a linha de nosso script e, normalmente são fáceis 
de se corrigir, veja um exemplo abaixo. Neste erro eu esqueço de iniciar a string com o sinal 
de aspas ". Uma exceção é um objeto da classe Exception, ou de uma de suas subclasses. Ele 
permite armazenar informações sobre situações excepcionais que venham a ocorrer durante a 
execução de comandos dentro de algum método.
"""

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
