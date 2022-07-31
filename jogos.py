import adivinhacao
import forca

def escolhe_jogo():
    print("*********************************")
    print("***Escolha um Jogo Para Jogar.***")
    print("*********************************")

    print("(1) Advinhação (2) Forca")

    jogo = int(input("Qual jogo você quer jogar? "))

    if (jogo == 1):
        adivinhacao.jogar()
    elif(jogo == 2):
        forca.jogar()

if (__name__=="__main__"):
    escolhe_jogo()