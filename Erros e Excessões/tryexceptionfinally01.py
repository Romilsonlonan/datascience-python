# Utilizando try, exceptions e finally 

def askint():
    try:
        val = int((input("Digite um número: ")))
    except UnboundLocalError:
        print("Você não digitou um número!")    
    finally:
        print("Obrigado!")
    print(val)    
print(askint())


