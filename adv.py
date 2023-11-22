import random
def jogar():
    
    apresentaçao()


    numero_secreto=numero_aleatorio()
    pontos = 1000
    total_de_tentativas = 0
    print(numero_secreto)
    
    usuario = perg_usuario()
   
    total_de_tentativas = nivel_usuario_tentativas(total_de_tentativas)
    
    logica_jogo (usuario,pontos,numero_secreto,total_de_tentativas)

    finalizaçao(numero_secreto,usuario)

def apresentaçao():
        print("**********************************************")
        print(">>>>>>>>>>>>>>>>Inicio do jogo<<<<<<<<<<<<<<<")
        print("**********************************************")
        
def finalizaçao (numero_secreto,usuario):
        print(">>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>")
        print("o numero secreto é. {}".format(numero_secreto))
        print("Fim do jogo  {} , muito obrigador por jogar".format(usuario))
        print(">>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>")

def perg_usuario():
        usuario=input("qual seu nome?")
        print("qual nivel de dificuldade ?")
        print("(1) FAcil (2) Medio (3)Dificil")
        return usuario

def nivel_usuario_tentativas(total_de_tentativas):
    nivel=int(input("qual nivel de dificuldade voce deseja"))
    if(nivel==1):
        total_de_tentativas=50
    elif(nivel==2):
        total_de_tentativas=20
    else:
        total_de_tentativas=5
    return total_de_tentativas

def logica_jogo (usuario,pontos,numero_secreto,total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número {}: ".format(usuario))
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou {}!  e fez {} pontos".format(usuario,pontos))
            break
        else:
            if (maior):
                print("{} ,você errou! O seu chute foi maior que o número secreto, digite um numero menor!".format(usuario))
            elif (menor):
                print("{} ,você errou! O seu chute foi menor que o número secreto, digite um numero maior!".format(usuario))
                pontos_perdidos= abs(numero_secreto -chute)
                pontos = pontos-pontos_perdidos

def numero_aleatorio():
    numero_secreto =  round (random.random() *100)
    return numero_secreto

if (__name__=="__main__"):
    jogar()
