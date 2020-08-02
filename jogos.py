import advinhacao
import namorado
import forca

def escolha_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Matematica (2) Adivinhação (3) Forca")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Matematica")
        namorado.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        advinhacao.jogar()
    elif (jogo == 3):
        print("Jogando Forca")
        forca.jogar()


if (__name__ == "__main__"):
    escolha_jogo()