import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")


numero_secreto = random.randrange(1, 101) # função para gerar um numero aleatorio entre 1 e 100
total_tentativas = 0
pontos = 1000

print("Qual nivel de dificuldade?")
print("(1) Facil (2) Médio (3) Dificil")

nivel = int(input("Escolha o Nivel: "))

if (nivel == 1):
    total_tentativas = 10 
elif (nivel == 2):
    total_tentativas = 6
else:
    total_tentativas = 3

for rodada in range (1, total_tentativas + 1):
    print(f"Tentativa {rodada} de {total_tentativas}")
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou " , chute)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print(f"Parabéns! Você acertou e fez {pontos} pontos")
        break # se acertar ira parar o laço, finalizando o jogo
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo")