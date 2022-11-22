"""
Para criar arquivos (e, consequentemente, abrí-los), utilizamos o método open() . Este método 
irá abrir o arquivo que passarmos como parâmetro com um determinado modo de uso (que também 
será passado como parâmetro). Passamos o nome do arquivo e sua extensão, além do modo que 
queremos utilizar o arquivo.
"""

arq1 = open("arquivo1.txt", "a")
arq1.write("Ficou show!!!")
# chamando o método write para acrescentar conteúdo 
print(arq1.read())