"""
read() O método em Python é usado para ler no máximo n bytes do arquivo associado ao 
descritor de arquivo fornecido. Se o fim do arquivo for alcançado durante a leitura 
de bytes do descritor de arquivo fornecido, o os. read() método retornará um objeto 
de bytes vazios para todos os bytes restantes para serem lidos.
"""

arq1 = open("arquivo1.txt", "r")
print(arq1.read(21))