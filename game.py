import sys

## Tabuleiro

def maketabuleiro():
    tabuleiro = {}
    lin = ['1','2','3']
    col = ['A','B','C','D']
    for l in lin :
        for c in col :
            key = str(l) + '-' + str(c)
            tabuleiro.setdefault(key,'0')
    #print('DEBUG: '+str(tabuleiro))
    return tabuleiro

def printcasa(casa):
    if casa:
        return ' ' + str(casa) + ' '
    else:
        return '   '
    
def showtabuleiro(tabuleiro):
    print("\n")
    print(printcasa(tabuleiro['1-A']) + '|' + printcasa(tabuleiro['1-B'])+ '|' + printcasa(tabuleiro['1-C'])+ '|' + printcasa(tabuleiro['1-D']))
    print('---------------')
    print(printcasa(tabuleiro['2-A']) + '|' + printcasa(tabuleiro['2-B'])+ '|' + printcasa(tabuleiro['2-C'])+ '|' + printcasa(tabuleiro['2-D']))
    print('---------------')
    print(printcasa(tabuleiro['3-A']) + '|' + printcasa(tabuleiro['3-B'])+ '|' + printcasa(tabuleiro['3-C'])+ '|' + printcasa(tabuleiro['3-D']))
    print("\n")
    
######

#Jogadas das peças Verdes
def jogada_verdes(tabuleiro):
    lin = ['1','2','3']
    col = ['A','B','C','D']

    move = input("\nOnde quer jogar?: ")
    valida = '0'

    for r in lin :
        for c in col :
            key = str(r) + '-' + str(c)
            if key == move :
                valida = '1'

    if tabuleiro[move] != '0':
        print('\nNão podes jogar ai\n')
        return False
    elif valida:
        tabuleiro[move] = 'G'
        return True
    else : 
        print('\nPosição Invalida\n')
        return False
    

#Jogadas das peças Amarelas
def jogada_amarelas(tabuleiro):
    lin = ['1','2','3']
    col = ['A','B','C','D']

    move = input("\nOnde quer jogar?: ")
    valida = '0'

    for r in lin :
        for c in col :
            key = str(r) + '-' + str(c)
            if key == move :
                valida = '1'

    if tabuleiro[move] != 'G':
        print('\nNão podes jogar ai\n')
        return False
    elif valida:
        tabuleiro[move] = 'Y'
        return True
    else : 
        print('\nPosição Invalida\n')
        return False


#Jogadas das peças Vermelhas
def jogada_vermelhas(tabuleiro):
    lin = ['1','2','3']
    col = ['A','B','C','D']

    move = input("\nOnde quer jogar?: ")
    valida = '0'

    for r in lin :
        for c in col :
            key = str(r) + '-' + str(c)
            if key == move :
                valida = '1'

    if tabuleiro[move] != 'Y':
        print('\nNão podes jogar ai\n')
        return False
    elif valida:
        tabuleiro[move] = 'R'
        return True
    else : 
        print('\nPosição Invalida\n')
        return False



def game():
    tabuleiro = maketabuleiro()

    
    while True:
        showtabuleiro(tabuleiro)

        while True:
            cor = input("Qual a cor que quer jogar? \n(G) Verde \n(Y) Amarelo \n(R) Vermelho \n: ")
            
            if (cor == 'G'):
                move = jogada_verdes(tabuleiro)

            elif (cor == 'Y'):
                move = jogada_amarelas(tabuleiro)

            elif (cor == 'R'):
                move = jogada_vermelhas(tabuleiro)

            else:
                print("\n\nCor invalida, tente novamente.")

            if move:
                break

            showtabuleiro(tabuleiro)
        showtabuleiro(tabuleiro)




# MENU
def menu():

    print("\n\n----- MENU -----\n\n")
    escolha = int(input("O que quer fazer? \n(1) Regras \n(2) Jogar 1vs1 \n(3) Sair \n: "))

    if (escolha == 1):
        print("\nO jogo é composto por um tabuleiro de 3x4 espaços (casas) \npara ambos os jogadores. Para jogar usam-se 24 peças, 8 de \ncada cor em 3 cores distintas Verde, Amarelo e Vermelho. \nAs peças e o tabuleiro são partilhados por ambos os jogadores. \nÀ vez, cada jogador seleciona uma peça e coloca-a no \ntabuleiro. Como regra na base pode ser colocada uma peça \nverde, uma peça verde pode ser substituída por uma peça amarela e uma peça amarela pode ser \nsubstituída por uma peça vermelha. \nSe ao colocar uma peça um jogador conseguir fazer uma linha com três peças da mesma cor \nautomaticamente ganha o jogo.\n")
    
    elif (escolha == 2):
        game()

    elif (escolha == 3):
        sys.exit()

    else:
        print("Escolha invalida, tente novamente.")

menu()








