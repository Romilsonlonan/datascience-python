"""
tell() método retorna a posição atual do objeto de arquivo. Este método não aceita parâmetros 
e retorna um valor inteiro. Inicialmente, o ponteiro do arquivo aponta para o início do arquivo 
(se não for aberto no modo anexar). Portanto, o valor inicial de tell() é zero.
"""

arq1 = open("arquivo1.txt", "r")
print(arq1.tell())