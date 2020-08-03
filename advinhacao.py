import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Adivinhação!")
    print("Tente adivinhar o número secreto!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual dificuldade deseja?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(0, total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Digite um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você Acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("seu numero foi maior que o numero secreto")
            elif(menor):
                print("seu numero foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        print("Você errou")
    print("Fim de jogo")
if(__name__ == "__main__"):
    jogar()

# import abra uma biblioteca que não seja builtin, exemplo random
# or é ou de outra opção
# continue faz retornar ao for vinculado após imprimir a mensagem com a proxima interação
# break quebra o laço de if, else, elif, while, for
# While cria uma condição para a execução do código
# for cria uma condição para a execução do código in
# range diz qual a ordenação que aparecerá
# If = Primeira possibilidade, Elif = Outra possibilidade listada, Else = Qualquer outra
# .format para acessar os comandos contidos no {}