"""
Segundo a documentação do Python há pelo menos dois tipos distintos de erros: erros de sintaxe 
e exceções. Os erros de sintaxe apontam para a linha de nosso script e, normalmente são fáceis 
de se corrigir, veja um exemplo abaixo. Neste erro eu esqueço de iniciar a string com o sinal 
de aspas ". Uma exceção é um objeto da classe Exception, ou de uma de suas subclasses. Ele 
permite armazenar informações sobre situações excepcionais que venham a ocorrer durante a 
execução de comandos dentro de algum método.
"""

# Erro de aspas

# print('Olá)

"""
File "/home/romilson/Projetos e Treinamentos/DataScience-Python/Erros e Excessões/erroexcessoes01.py", line 3
    print('Olá)
          ^
"""

# correto

print('Olá')
