print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

total_de_tentativas = 0

rodada = 1

while (total_de_tentativas <= 3):
        print("Tentativa", rodada, "de", total_de_tentativas)

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Parabéns, você acertou")
else:
    if (maior):
        print("Você digitou um número maior que o número secreto")
    elif (menor):
        print("Você digitou um número menor que o núnmero secreto")

total_de_tentativas = total_de_tentativas +1;

print("Fim do jogo")