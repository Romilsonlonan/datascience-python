def askint():
    while True:
        try:
            val = int(input("Digite um numero: "))
        except:
            print("Voce não digitou o número!")
            continue
        else:   
            print("Obrigado por digitar um numero!")
            break
        finally:
            print("Fim da execução")
        print(val)
print(askint())