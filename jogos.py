import forca 
import adv


def escolhe_jogo():

    print("**********************************************")
    print(">>>>>>>>>>>>>>>>Inicio do jogo<<<<<<<<<<<<<<<")
    print("**********************************************")

    print(" (1)jogo da força (2) jogo de adivinhação")

    jogo = int(input("qual jogo voce quer escolher?"))

    if (jogo==1):
        print("jogando forca")
        forca.jogar()
    elif (jogo==2):
        print("jogando advinhação")
        adv.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()
