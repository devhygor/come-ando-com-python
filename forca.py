import random
import unidecode

def jogar():

    mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_corretas = inicializa_letras_corretas(palavra_secreta)
    
    if "-" in palavra_secreta:
        chute = "-"
        marca_chute_correto(chute, letras_corretas, palavra_secreta)
        qtd_caractere = letras_corretas.count('-')
        print(f"É uma fruta com {len(palavra_secreta)-qtd_caractere} letras \n")
    else:
        print(f"É uma fruta com {len(palavra_secreta)} letras \n")
        
    
         
    print(f"{letras_corretas}\n")

    enforcou = False
    acertou = False
    erros = 0
    letras_errada = []
    
    while(not enforcou and not acertou):
        
        chute = pede_chute()
        
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_corretas, palavra_secreta)
        else:
            erros += 1
            letras_errada.append(chute)
            desenha_forca(erros, letras_errada)
            
        enforcou = erros == 7
        acertou = "_" not in letras_corretas
        print(f"{letras_corretas}\n")

        
    if (acertou):
        mostra_mensagem_ganhador()
    else:
        mostra_mensagem_perdedor(palavra_secreta)
    print("Fim de Jogo")
    
def mensagem_abertura():
    print()
    print()
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print()
    
def carrega_palavra_secreta():
    
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = (linha.strip())
        palavras.append(linha)
    
    arquivo.close()
    
    posicao = random.randrange(0, len(palavras))
    palavra_secreta = unidecode.unidecode(palavras[posicao].upper())
    
    return palavra_secreta

def inicializa_letras_corretas(palavra):
        
    return ["_" for letra in palavra]

def pede_chute():
    chute = input('Qual letra? ')
    print()
    chute = chute.strip().upper()
    
    return chute
    
def marca_chute_correto(chute, letras_corretas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_corretas[index] = letra
        index += 1
        
def mostra_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def mostra_mensagem_perdedor(palavra_secreta):    
    print("Não foi desta vez \n GAME OVER")
    print("A palavra era {}".format(palavra_secreta))
    print("        _______________         ")
    print("       /               \       ")
    print("      /                 \      ")
    print("   /\/                   \/\  ")
    print("   \ |   XXXX     XXXX   | /   ")
    print("    \|   XXXX     XXXX   |/     ")
    print("     |   XXX       XXX   |      ")
    print("     |                   |      ")
    print("     \__      XXX      __/     ")
    print("       |\     XXX     /|       ")
    print("       | |           | |        ")
    print("       | I I I I I I I |        ")
    print("       |  I I I I I I  |        ")
    print("       \_             _/       ")
    print("         \_         _/         ")
    print("           \_______/           ")
    
def desenha_forca(erros, letras_errada):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    print(f"Você já usou as letras {letras_errada}\n")
    print(f"você ainda tem {7-erros} tentativas\n")

if (__name__=="__main__"):
    jogar()