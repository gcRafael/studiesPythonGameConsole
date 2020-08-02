def jogar():
    print("*********************************")
    print("*Bem vindo a calculadora mestra!*")
    print("*********************************")
    N1 = int(input('DIGITE UM NUMERO'))
    N2 = int(input('DIGITE OUTRO NUMERO'))


    s  = N1 + N2
    m  = N1 * N2
    d  = N1 / N2
    di = N1 // N2
    po = N1 ** N2

    print('A soma é {} \nA multiplicação é {} \nA divisão {}'.format(s, m, d))

    #Aplicação de .format para apontamento do {}
    #Comando \n para drop de linha sem precisar de outro print
    #Comando end=' ' no final para quebrar a ultima linha para cima
    print('A divisão inteira é {} \nA potencia é {}'.format(di, po))
if(__name__ == "__main__"):
    jogar()