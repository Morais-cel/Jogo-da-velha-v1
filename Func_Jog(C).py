from random import randint
from time import sleep
from Func_estr import Subs,VerVit,opc,Teste,VerEmp

Núm_Maq=randint(0,9)

def jogo(Jog,maq):
    print('Primeiro vamos decidir quem vai jogar primeiro')
    print('Escolha entre PAR ou IMPAR, e logo depois escolha um número de 0-9')
    Esc=str(input('PAR/ÍMPAR: ')).upper().strip()
    while True:
        if Esc not in 'PARÍMPARIMPARParImparparímparimpar':
            print('\033[31mERRO! ESCOLHA ENTRE PAR OU IMPAR\033[m')
            Esc=str(input('PAR/ÍMPAR: ')).upper().strip()
        else:
            break
    Núm_Jog=int(input('Digite um número: '))
    while True:
        if 0<=Núm_Jog<=9:
            break
        else:
            print('\033[31mERRO! ESCOLHA UM NÚMERO ENTRE 0-9\033[m')
            Núm_Jog=int(input('Digite um número: '))
    if (Núm_Jog+Núm_Maq)%2==0 and Esc[0]=='P' or (Núm_Jog+Núm_Maq)%2!=0 and Esc[0]=='I':
        print(f'A soma entre \033[33m{Núm_Jog}\033[m e \033[34m{Núm_Maq}\033[m é {Núm_Jog+Núm_Maq}, ou seja, \033[32mé\033[m um número {Esc}. Você é o primeiro a jogar!!')
        J1=Jog
        J2=maq
    else:
        print(f'A soma entre \033[33m{Núm_Jog}\033[m e \033[34m{Núm_Maq}\033[m é {Núm_Jog+Núm_Maq}, ou seja,\033[31m não é\033[m um número {Esc}. A máquina é o primeiro a jogar!!')
        J1=maq
        J2=Jog
    if J1==maq:
        Aux=J1
    else:
        Aux=J2
    Jogar(J1,J2,Aux)

def Jogar(J1,J2,inf):
    if J1==inf:
        Ran=J1
    else:
        Ran=J2
    print('-='*25)
    print(f'Então vamos começar ojogo, {J1} será o primeiro a jogar')
    sleep(0.8)
    for c in range(0,9):
        if c%2!=0:
            if Ran==J2: #Caso a máquina seja o jogador 2
                Jog_At=J2
                print(f'{J2} irá escolher um número entre 1 e 9')
                sleep(0.8)
                Núm_Jog=randint(1,9)
                Teste(Núm_Jog)
                while True:
                    if not Teste(Núm_Jog):
                        Núm_Jog=randint(1,9)
                    else:
                        break
                print(f'{J2} escolheu o número: \033[34m{Núm_Jog}\033[m')
                sleep(0.8)
            else: #Caso você seja o jogador 2
                Jog_At=J2
                print(f'{J2}, Escolha um número de 1 à 9')
                while True:
                    while True:
                        try:
                            Núm_Jog=str(input('Digite um número: '))
                            Núm_Jog=int(Núm_Jog)
                            break
                        except:
                            print('\033[31mERRO! DIGITE UM NÚMERO\033[m')
                    if 1<=Núm_Jog<=9:
                        Teste(Núm_Jog)
                        if Teste(Núm_Jog):
                            break
                        else:
                            print('\033[31mERRO! ESCOLHA UM NÚMERO QUE AINDA NÃO FOI ESCOLHIDO\033[m')
                    else:
                        print('\033[31mERRO! ESCOLHA UM NÚMERO ENTRE 1-9\033[m')
                print(f'{J2} escolheu o número: \033[33m{Núm_Jog}\033[m')
        else:
            if Ran==J1:#Caso a máquina seja o jogador 1
                Jog_At=J1 
                print(f'{J1} irá escolher um número entre 1 e 9')
                sleep(0.8)
                Núm_Jog=randint(1,9)
                Teste(Núm_Jog)
                while True:
                    if not Teste(Núm_Jog):
                        Núm_Jog=randint(1,9)
                    else:
                        break
                print(f'{J1} escolheu o número: \033[34m{Núm_Jog}\033[m')
                sleep(0.8)
            else:#Caso você seja o jogador 1
                Jog_At=J1 
                print(f'{J1}, Escolha um número de 1 à 9')
                while True:
                    while True:
                        try:
                            Núm_Jog=str(input('Digite um número: '))
                            Núm_Jog=int(Núm_Jog)
                            break
                        except:
                            print('\033[31mERRO! DIGITE UM NÚMERO\033[m')
                    if 1<=Núm_Jog<=9:
                        Teste(Núm_Jog)
                        if Teste(Núm_Jog):
                            break
                        else:
                            print('\033[31mERRO! ESCOLHA UM NÚMERO QUE AINDA NÃO FOI ESCOLHIDO\033[m')
                    else:
                        print('\033[31mERRO! ESCOLHA UM NÚMERO ENTRE 1-9\033[m')
                print(f'{J1} escolheu o número: \033[33m{Núm_Jog}\033[m')
        print('-='*16)
        print(f'\033[36mJogando',end='')
        for d in range(0,3):
            print('.',end='')
            sleep(0.5)
        print('\033[m')
        print('-='*16)
        sleep(0.5)
        Subs(Núm_Jog,Jog_At) #Substitui o número escolhido pelo jogador/Máquina
        if VerVit(Jog_At): #Verifica se o jogador/Máquina venceu
            opc()
            if not opc():
                break
        if VerEmp(): #Verifica se deu empate
            print('-='*16)
            print('FIM DE JOGO POR EMPATE!!'.center(30))
            print('-='*16)
            opc()
            if not opc():
                break




#Para jogar contra outro player
    '''print(f'Então vamos começar a jogar, {J1} será o primeiro a jogar')
    for c in range(0,9):
        if c==0:
            print(f'{J1}, Escolha um número de 1-9')
            Jog_At=J1
        else:
            if c%2!=0:
                print(f'{J2}, Escolha um número de 1-9')
                Jog_At=J2
            else:
                print(f'{J1}, Escolha um número de 1-9')
                Jog_At=J1
        while True:
            Núm_Jog=int(input('Digite um número: '))
            if 1<=Núm_Jog<=9:
                break
            else:
                print('\033[31mERRO! ESCOLHA UM NÚMERO ENTRE 1-9\033[m')
        print('-='*25)
        print('\033[36mJogando...\033[m')
        print('-='*25)
        sleep(0.5)
        Subs(Núm_Jog,Jog_At)
        VerVit(Jog_At)
        if VerVit(Jog_At):
            #reset()
            break'''