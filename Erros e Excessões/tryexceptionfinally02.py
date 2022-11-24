# Tratamento de excessão quando ao teclar enter e concluir uma operação e dá erro por motivo de 
# de que o sistema operacional entende outro tipo de comando (ctrl + barra + n) que é a mesma
# coisa de enter

def askint():
    try:
        val = int(input("Digite um número: "))
    except:
        print("Você não digitou um número!")
        val = int(input("Tente novamente. Digite um número: "))    
    finally:
        print("Obrigado!")
    print(val)    
print(askint())