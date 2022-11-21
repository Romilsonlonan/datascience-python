"""
Em Python, a seek() função é usada para alterar a posição do identificador de arquivo 
para uma determinada posição. O identificador de arquivo é como um cursor, que define 
de onde os dados devem ser lidos ou gravados no arquivo.
"""

arq1 = open("arquivo1.txt", "r")
print(arq1.seek(0,0))