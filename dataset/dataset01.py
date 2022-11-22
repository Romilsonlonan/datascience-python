fileName = input("Digite o nome do seu arquivo:  ")

fileName = fileName + ".txt"

arq1 = open(fileName, "w")

arq1.write("Incluindo texto no arquivo criado")

arq1.close()

arq1 = open(fileName, "r")

print(arq1.read())

arq1.close()