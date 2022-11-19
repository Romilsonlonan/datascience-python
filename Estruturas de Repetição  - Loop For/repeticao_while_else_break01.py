"""
Se dentro da repetição for executado um break, 
o loop será encerrado sem executar o conjunto 
da cláusula else.
"""

x = 0
while x < 10:
    print(x)
    x += 1
    if x == 6:
        print("x é igual a 6")
        break
else:
    print("fim while")