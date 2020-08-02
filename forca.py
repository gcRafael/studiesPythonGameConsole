import random

def jogar():
    imprime_mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas

        if (acertou):
            imprime_mensagem_vencedor()
        else:
            imprime_mensagem_perdedor()


def imprime_mensagem_de_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    print("Jogando...")
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posição = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posição] = letra
        posição += 1
        return


def imprime_mensagem_vencedor():
    print("Você Ganhou")
    return


def imprime_mensagem_perdedor():
    print("Você Perdeu")
    return


if (__name__ == "__main__"):
    jogar()

# comando open("palavras.txt", "w") arquivo, função/modo
# comando close para fechar o arquivo
# uma lista de sequencia com (**tuple**) é um tupple, que é uma lista imutável
# uma lista de sequencias com [**list**] é mutavel
# é possível ler arquivos especificos em uma unica linha de codigo para listas ex: conteudo pai[0] conteudo filho[1]
# palavras = []
# palavras.append("banana")
# palavras.append("abacaxi")
# nova = tuple(palavras)
# outra = list(nova)
# False e True sempre MAIÚSCULO
# False e True são classe bool
# len(variavel) retorna a extenção de caracteres da lista
# a função find encontra a PRIMEIRA aparição
# enquanto não enforcou e não acertou:
