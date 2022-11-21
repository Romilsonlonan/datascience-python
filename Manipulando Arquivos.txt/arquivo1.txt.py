"""
Para criar arquivos (e, consequentemente, abrí-los), utilizamos o método open(). Este 
método irá abrir o arquivo que passarmos como parâmetro com um determinado modo de uso 
(que também será passado como parâmetro). Passamos o nome do arquivo e sua extensão, 
além do modo que queremos utilizar o arquivo.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

read() O método em Python é usado para ler no máximo n bytes do arquivo associado ao 
descritor de arquivo fornecido. Se o fim do arquivo for alcançado durante a leitura 
de bytes do descritor de arquivo fornecido, o os. read() método retornará um objeto 
de bytes vazios para todos os bytes restantes para serem lidos.
"""

with open("arquivo1.txt", "r") as arquivo1:
    arq1 = arquivo1.read()
    print(arq1)