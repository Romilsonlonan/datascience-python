"""
Com a finalidade de escrever programas úteis, quase sempre temos a necessidade de verificar 
condições e alterar o comportamento do programa de acordo com os resultados das condições. 
Comandos de seleção, algumas vezes também denominados de comandos condicionais nos dá essa 
habilidade. A forma mais simples de seleção é o comando if. Ele é algumas vezes denominado 
de seleção binária uma vez que admite dois possíveis caminhos de execução.
"""

x = 15

if x % 2 == 0:
    print(x, "e' par")
else:
    print(x, "e' impar")