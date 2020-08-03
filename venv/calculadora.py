def jogar():
    print("*********************************")
    print("*Bem vindo a calculadora mestra!*")
    print("*Escolha dois números e descubra*")
    print("*possibilidades aritiméticas com*")
    print("*a combinação entre os números!!*")
    print("*********************************")
    N1 = int(input('Escolha um número'))
    N2 = int(input('Escolha mais um número'))


    s  = N1 + N2
    m  = N1 * N2
    d  = N1 / N2
    di = N1 // N2
    po = N1 ** N2

    print('A soma é {} \nA multiplicação é {} \nA divisão {}'.format(s, m, d))


    print('A divisão inteira é {} \nA potencia é {}'.format(di, po))
if(__name__ == "__main__"):
    jogar()

#Aplicação de .format para apontamento do {}
#Comando \n para drop de linha sem precisar de outro print
#Comando end=' ' no final para quebrar a ultima linha para cima