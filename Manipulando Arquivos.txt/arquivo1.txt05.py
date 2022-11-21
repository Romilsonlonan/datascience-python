# Método para leitura write "w"

"""
método write() retorna o número de caracteres escrito. Se quisermos escrever várias 
linhas de uma vez, podemos usar o método writelines() , que leva uma lista de strings. 
Cada string representa uma linha a ser adicionada ao arquivo
"""

arq1 = open("arquivo1.txt05", "w")
print(arq1.write("Testando a Gravação do Arquivo Python"))