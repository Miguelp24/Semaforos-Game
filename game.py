import sys
import random

## Tabuleiro

def maketabuleiro():
    tabuleiro = {}
    lin = ['1','2','3']
    col = ['A','B','C','D']
    for l in lin :
        for c in col :

            key = str(l) + str(c)
            tabuleiro.setdefault(key,False)

    return tabuleiro

def printcasa(casa):
    if casa:
        return ' ' + str(casa) + ' '
    else:
        return '   '
    
def showtabuleiro(tabuleiro):

    print(printcasa(tabuleiro['1A']) + '|' + printcasa(tabuleiro['1B'])+ '|' + printcasa(tabuleiro['1C'])+ '|' + printcasa(tabuleiro['1D']))
    print('---------------')
    print(printcasa(tabuleiro['2A']) + '|' + printcasa(tabuleiro['2B'])+ '|' + printcasa(tabuleiro['2C'])+ '|' + printcasa(tabuleiro['2D']))
    print('---------------')
    print(printcasa(tabuleiro['3A']) + '|' + printcasa(tabuleiro['3B'])+ '|' + printcasa(tabuleiro['3C'])+ '|' + printcasa(tabuleiro['3D']))
    print("\n")
    
######

#Jogadas das peças Verdes
def jogada_verdes(tabuleiro):
    verdes = 8
    lin = ['1','2','3']
    col = ['A','B','C','D']

    move = input("\nOnde quer jogar?: ")
    valida = '0'

    for r in lin :
        for c in col :
            key = str(r) + str(c)
            if key == move :
                valida = '1'

    if (verdes == 0):
        print("Acabaram as peças verdes")
        return False

    if tabuleiro[move] != False:
        print('\nNão podes jogar ai\n')
        return False
    elif valida:
        tabuleiro[move] = 'G'
        verdes = verdes - 1
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
            key = str(r) + str(c)
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
            key = str(r) + str(c)
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


## Determinar vitoria 

def vitoria(tabuleiro):
    
    lin = ['1','2','3']
    col = ['A','B','C','D']

    a = ''
    b = 0
    n = ' '
    v = False
    

    for r in lin:
        a = ''
        b = 0
        n = ' '

        for c in col:
            a = str(r)+str(c)
            if(tabuleiro[a]==False):
                n = ''
                continue
            elif(tabuleiro[a] == n ):
                b = b + 1
            else:
                n = tabuleiro[a]
            if (b == 2): 
                v = True
                continue
            

        if (b == 2):
            break
        
    
    if (v == True):
            print("\n\nFim do jogo! Vitória")     
            return False  

    a = ''
    b = 0
    n = ''

    for c in col:
        a = ''
        b = 0
        n = ''
        for r in lin:
            
            a = str(r)+str(c)
            if(tabuleiro[a]==False):
                continue
            if(tabuleiro[a] == n ):
                b = b + 1
            if (b == 2): 
                v = True
                continue
            if(n == False):
                continue
            else:
                n = tabuleiro[a]

        if (b == 2):
            break
        
    
    if (v == True):
        print("\n\nFim do jogo! Vitória")     
        return False  
    
    if (tabuleiro['1A'] == tabuleiro['2B'] and tabuleiro['1A']==tabuleiro['3C'] and tabuleiro['1A'] != False and tabuleiro['2B'] != False and tabuleiro['3C'] != False):
        print("\n\nFim do jogo! Vitória")     
        return False
    if (tabuleiro['1B'] == tabuleiro['2C'] and tabuleiro['1B']==tabuleiro['3D'] and tabuleiro['1B'] != False and tabuleiro['2C'] != False and tabuleiro['3D'] != False):
        print("\n\nFim do jogo! Vitória")     
        return False
    if (tabuleiro['1C'] == tabuleiro['2B'] and tabuleiro['1C']==tabuleiro['3A'] and tabuleiro['1C'] != False and tabuleiro['2B'] != False and tabuleiro['3A'] != False):
        print("\n\nFim do jogo! Vitória")     
        return False
    if (tabuleiro['1D'] == tabuleiro['2C'] and tabuleiro['1D']==tabuleiro['3B'] and tabuleiro['1D'] != False and tabuleiro['2C'] != False and tabuleiro['3B'] != False):
        print("\n\nFim do jogo! Vitória")     
        return False

    return True
 


## Jogadores 
def changeplayer(p1, p2, p1_name, p2_name):

    if(p1 == False):
        print("--- Player " + p1_name + " ---\n")
    elif(p2 == False):
        print("--- Player " + p2_name + " ---\n")


def escolhercor(tabuleiro):
    
    while True:
        cor = input("Qual a cor que quer jogar? \n(G) Verde \n(Y) Amarelo \n(R) Vermelho \n: ")
        
        if (cor == 'G' or cor == 'g'):
            move = jogada_verdes(tabuleiro)
        elif (cor == 'Y' or cor == 'y'):
            move = jogada_amarelas(tabuleiro)
        elif (cor == 'R' or cor == 'r'):
            move = jogada_vermelhas(tabuleiro)
        else:
            print("\n\nCor invalida, tente novamente.")
            continue

        showtabuleiro(tabuleiro)

        if move:
            break



def game():
    p1_name = input("\nInsira o nome do Player 1: ")
    p2_name = input("\nInsira o nome do Player 2: ")
    p_name = ""
    tabuleiro = maketabuleiro()
    fim = True
    p1 = False
    p2 = False
    
    while (fim == True):
        showtabuleiro(tabuleiro)
        
        if (p1 == False):
            changeplayer(p1, p2, p1_name, p2_name)
            p1 = True
            p2 = False
            p_name = p1_name

        elif (p2 == False):
            changeplayer(p1, p2, p1_name, p2_name)
            p2 = True
            p1 = False
            p_name = p2_name
        
        escolhercor(tabuleiro)
        
        fim = vitoria(tabuleiro)

    print("\nGanhou o Player " + p_name + "\n\n")



## BOT
    
def escolhaposiçao_bot(tabuleiro):
    random.seed()
    opcoes_linha = ('1','2','3')
    opcoes_coluna = ('A','B','C','D')
    valida = False

    while (valida == False):
        opcao_lin = random.choice(opcoes_linha)
        opcao_col = random.choice(opcoes_coluna)

        move = opcao_lin + opcao_col


        if(tabuleiro[move] == False):
            tabuleiro[move] = 'G'
            valida = True

        elif(tabuleiro[move] == 'G'):
            tabuleiro[move] = 'Y'
            valida = True

        elif(tabuleiro[move] == 'Y'):
            tabuleiro[move] = 'R'
            valida = True

    return False



def bot():
    name_bot = "BOT Diogo"
    print("\nOlá eu sou o BOT Diogo, vamos jogar?")
    p1_name = input("\nInsira o seu nome: ")
    p_name = ""
    tabuleiro = maketabuleiro()
    fim = True
    p1 = False
    p2 = False
    
    while (fim == True):
        showtabuleiro(tabuleiro)
        
        if (p1 == False):
            changeplayer(p1, p2, p1_name, name_bot)
            p1 = True
            p2 = False
            p_name = p1_name

        elif (p2 == False):
            changeplayer(p1, p2, p1_name, name_bot)
            p2 = True
            p1 = False
            p_name = name_bot
        
        if (p1 == True):
            escolhercor(tabuleiro)

        elif(p2 == True):
            escolhaposiçao_bot(tabuleiro)
        
        fim = vitoria(tabuleiro)

    print("\nGanhou o Player " + p_name + "\n\n")



# MENU
def menu():
    
    print("\nJOGO DOS SEMÁFOROS")
    print("\n\n----- MENU -----\n\n")
    
    escolha = int(input("O que quer fazer? \n(1) Regras \n(2) Jogar 1vs1 \n(3) Jogar com o BOT\n(4) Sair \n: "))

    if (escolha == 1):
        print("\nO jogo é composto por um tabuleiro de 3x4 espaços (casas) \npara ambos os jogadores. Para jogar usam-se 24 peças, 8 de \ncada cor em 3 cores distintas Verde, Amarelo e Vermelho. \nAs peças e o tabuleiro são partilhados por ambos os jogadores. \nÀ vez, cada jogador seleciona uma peça e coloca-a no \ntabuleiro. Como regra na base pode ser colocada uma peça \nverde, uma peça verde pode ser substituída por uma peça amarela e uma peça amarela pode ser \nsubstituída por uma peça vermelha. \nSe ao colocar uma peça um jogador conseguir fazer uma linha com três peças da mesma cor \nautomaticamente ganha o jogo.\n")
    
    elif (escolha == 2):
        game()
    elif (escolha == 3):
        bot()
    elif (escolha == 4):
        sys.exit()

    else:
        print("Escolha invalida, tente novamente.")
        menu()

menu()








