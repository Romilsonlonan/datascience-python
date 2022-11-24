precos = [1000, 15000, 1250, 2500]

def adicionar_imposto(preco):
    return preco * 1.1

precos_com_imposto = []

for preco in precos:
    precos_com_imposto.append(adicionar_imposto(preco))

print(precos_com_imposto)