arq1 = open("arquivo1.txt", "r")
print(arq1.read())

with open("arquivo1.txt", "r",) as arquivo1:
    arq1 = arquivo1.read()
    print(arq1)

