from random import randint
from time import sleep
from Func_estr import Subs,VerVit,opc,Teste,VerEmp

Núm_Maq=randint(0,9)

def JogJog(): #Jogo jogador contra jogador
    tip=1
    Jogador1=str(f'\033[34m{input('Digite o símbolo do jogador 1: ')}\033[m')
    Jogador2=str(f'\033[33m{input('Agora digite o símbolo do jogador 2: ')}\033[m')
    print('-='*32)
    print(f'Então o jogador 1 será {Jogador1} e o jogador 2 será {Jogador2}. Vamos começar!!')
    print('-='*32)
    sleep(0.7)
    jogo(Jogador1,Jogador2,tip)

def JogMaq(): #Jogo jogador contra máquina
    tip=2
    Maq='\033[34mO\033[m'
    Jogador=str(f'\033[33m{input('Digite o símbolo que você deseja ser: ')}\033[m')
    print(f'Então você será {Jogador} e jogará contra {Maq}. Vamos começar!!')
    print('-='*25)
    sleep(0.7)
    jogo(Jogador,Maq,tip)

def MaqMaq(): #Jogo máquina contra máquina
    tip=3
    Maq1='\033[34mO\033[m'
    Maq2='\033[33mX\033[m'
    print('-='*32)
    print(f'Então a Máquina 1 será {Maq1} e a Máquina 2 será {Maq2}. Vamos começar!!')
    print('-='*32)
    sleep(0.9)
    jogo(Maq1,Maq2,tip)


def jogo(Jog1,Jog2,inf):
    print('Primeiramente, vamos decidir quem vai jogar primeiro.')
    if inf==1: #método de jogo para jogador contra jogador
        print(f'Jogador 1 ({Jog1}), escolha entre PAR ou IMPAR, e logo depois escolha um número de 0 à 9')
        Esc1=str(input('PAR/ÍMPAR: ')).upper().strip()
        while True:
            if Esc1 not in 'PARÍMPARIMPARParImparparímparimpar':
                print('\033[31mERRO! ESCOLHA ENTRE PAR OU IMPAR\033[m')
                Esc1=str(input('PAR/ÍMPAR: ')).upper().strip()
            else:
                break
        while True: #Input número par ou ímpar para jogador 1
            while True:
                try:        
                    Núm_PI1=str(input('Digite um número: '))
                    Núm_PI1=int(Núm_PI1)
                    break
                except:
                    print('\033[31mERRO! DIGITE UM NÚMERO VÁLIDO\033[m')
            if 0<=Núm_PI1<=9:
                break
            else:
                print('\033[31mERRO! ESCOLHA UM NÚMERO ENTRE 0-9\033[m')
        print('-='*32)
        print(f'Agora é sua vez, Jogador 2 ({Jog2}). Digite um valor entre 0 e 9 para decidirmos quem jogará primeiro!!')
        while True: #Input número par ou ímpar para jogador 2
            while True:
                try:        
                    Núm_PI2=str(input('Digite um número: '))
                    Núm_PI2=int(Núm_PI2)
                    break
                except:
                    print('\033[31mERRO! DIGITE UM NÚMERO VÁLIDO\033[m')
            if 0<=Núm_PI2<=9:
                break
            else:
                print('\033[31mERRO! ESCOLHA UM NÚMERO ENTRE 0-9\033[m')
        if (Núm_PI1+Núm_PI2)%2==0 and Esc1[0]=='P' or (Núm_PI1+Núm_PI2)%2!=0 and Esc1[0]=='I': #Decisão de quem joga primeiro
            print(f'A soma entre \033[33m{Núm_PI1}\033[m e \033[34m{Núm_PI2}\033[m é {Núm_PI1+Núm_PI2}, ou seja, \033[32mé\033[m um número {Esc1}. Portanto, o Jogador 1 ({Jog1}) é o primeiro a jogar!!')
            J1=Jog1
            J2=Jog2
        else:
            print(f'A soma entre \033[33m{Núm_PI1}\033[m e \033[34m{Núm_PI2}\033[m é {Núm_PI1+Núm_PI2}, ou seja,\033[31m não é\033[m um número {Esc1}. Portanto, o Jogador 1 ({Jog1}) é o primeiro a jogar!!')
            J1=Jog2
            J2=Jog1
        Jogar(J1,J2,inf)

    elif inf==2: #método de jogo para jogador contra máquina
        print('Escolha entre PAR ou IMPAR, e logo depois escolha um número de 0 à 9')
        Esc=str(input('PAR/ÍMPAR: ')).upper().strip()
        while True:
            if Esc not in 'PARÍMPARIMPARParImparparímparimpar':
                print('\033[31mERRO! ESCOLHA ENTRE PAR OU IMPAR\033[m')
                Esc=str(input('PAR/ÍMPAR: ')).upper().strip()
            else:
                break
        while True: #Input número par ou ímpar
            while True:
                try:        
                    Núm_PI=str(input('Digite um número: '))
                    Núm_PI=int(Núm_PI)
                    break
                except:
                    print('\033[31mERRO! DIGITE UM NÚMERO VÁLIDO\033[m')
            if 0<=Núm_PI<=9:
                break
            else:
                print('\033[31mERRO! ESCOLHA UM NÚMERO ENTRE 0-9\033[m')
        if (Núm_PI+Núm_Maq)%2==0 and Esc[0]=='P' or (Núm_PI+Núm_Maq)%2!=0 and Esc[0]=='I': #Decisão de quem joga primeiro
            print(f'A soma entre \033[33m{Núm_PI}\033[m e \033[34m{Núm_Maq}\033[m é {Núm_PI+Núm_Maq}, ou seja, \033[32mé\033[m um número {Esc}. Você é o primeiro a jogar!!')
            J1=Jog1
            J2=Jog2
        else:
            print(f'A soma entre \033[33m{Núm_PI}\033[m e \033[34m{Núm_Maq}\033[m é {Núm_PI+Núm_Maq}, ou seja,\033[31m não é\033[m um número {Esc}. A máquina é o primeiro a jogar!!')
            J1=Jog2
            J2=Jog1
        if J1==Jog2:
            Aux=J1
        else:
            Aux=J2
        Jogar(J1,J2,inf,Ext=Aux)

    elif inf==3: #método de jogo para máquina contra máquina
        ParouImpar=['PAR','IMPAR']
        print(f'A Máquina 1 ({Jog1}) escolherá entre PAR ou IMPAR, e logo depois escolherá um número de 0 à 9')
        sleep(0.7)
        Esc1=ParouImpar[randint(0,1)]
        print(f'A Máquina 1 ({Jog1}) escolheu {Esc1}.')
        sleep(0.7)
        Núm_PI1=randint(0,9)
        print(f'A Máquina 1 ({Jog1}) escolheu o número {Núm_PI1}.')
        sleep(0.7)
        print('-='*32)
        print(f'Agora é a vez da Máquina 2. Ela escolherá um número entre 0 e 9 para decidirmos quem jogará primeiro!!')
        sleep(0.7)
        Núm_PI2=randint(0,9)
        print(f'A Máquina 2 ({Jog2}) escolheu o número {Núm_PI2}.')
        sleep(0.7)
        print('-='*32)
        if (Núm_PI1+Núm_PI2)%2==0 and Esc1[0]=='P' or (Núm_PI1+Núm_PI2)%2!=0 and Esc1[0]=='I': #Decisão de quem joga primeiro
            print(f'A soma entre \033[33m{Núm_PI1}\033[m e \033[34m{Núm_PI2}\033[m é {Núm_PI1+Núm_PI2}, ou seja, \033[32mé\033[m um número {Esc1}. Portanto, a Máquina 1 ({Jog1}) é a primeiro a jogar!!')
            J1=Jog1
            J2=Jog2
        else:
            print(f'A soma entre \033[33m{Núm_PI1}\033[m e \033[34m{Núm_PI2}\033[m é {Núm_PI1+Núm_PI2}, ou seja,\033[31m não é\033[m um número {Esc1}. Portanto, o Máquina 1 ({Jog1}) é o primeiro a jogar!!')
            J1=Jog2
            J2=Jog1
        sleep(0.8)
        Jogar(J1,J2,inf)

def Jogar(J1,J2,inf,Ext=''):
    if inf==1: #Funcionamento jogo jogador contra jogador
        print('-=' *25)
        print(f'Então vamos começar o jogo, {J1} será o primeiro a jogar')
        sleep(0.8)
        for c in range(0,9): #Jogo
            if c%2==0: #Processo de jogada de J1
                Jog_At=J1
                while True:
                    while True:
                        try:
                            Núm_Jog=str(input(f'{J1}, Escolha um número de 1 à 9: '))
                            Núm_Jog=int(Núm_Jog)
                            break
                        except:
                            print('\033[31mERRO! DIGITE UM NÚMERO VÁLIDO\033[m')
                    if 1<=Núm_Jog<=9:
                        if Teste(Núm_Jog):
                            break
                        else:
                            print('\033[31mERRO! ESCOLHA UM NÚMERO QUE AINDA NÃO FOI ESCOLHIDO\033[m')
                    else:
                        print('\033[31mERRO! ESCOLHA UM NÚMERO ENTRE 1 E 9\033[m')
                print(f'{J1} escolheu o número: \033[33m{Núm_Jog}\033[m')
            else: #Processo de jogada de J2
                Jog_At=J2
                while True:
                    while True:
                        try:
                            Núm_Jog=str(input(f'{J2}, Escolha um número de 1 à 9: '))
                            Núm_Jog=int(Núm_Jog)
                            break
                        except:
                            print('\033[31mERRO! DIGITE UM NÚMERO VÁLIDO\033[m')
                    if 1<=Núm_Jog<=9:
                        if Teste(Núm_Jog):
                            break
                        else:
                            print('\033[31mERRO! ESCOLHA UM NÚMERO QUE AINDA NÃO FOI ESCOLHIDO\033[m')
                    else:
                        print('\033[31mERRO! ESCOLHA UM NÚMERO ENTRE 1 E 9\033[m')
                print(f'{J2} escolheu o número: \033[33m{Núm_Jog}\033[m')
            print('-='*16)
            print(f'\033[36mJogando',end='')
            for d in range(0,3):
                print('.',end='')
                sleep(0.5)
            print('\033[m')
            print('-='*16)
            sleep(0.5)
            Subs(Núm_Jog,Jog_At) #Substitui o número escolhido pelo jogador atual
            if VerVit(Jog_At): #Verifica se o jogador atual venceu
                if opc():
                    break
            if VerEmp(): #Verifica se deu empate
                print('-='*16)
                print('FIM DE JOGO POR EMPATE!!'.center(30))
                print('-='*16)
                if opc():
                    break

    if inf==2: #Funcionamento jogo jogador contra máquina
        if J1==Ext:
            Ran=J1
        else:
            Ran=J2
        print('-='*25)
        print(f'Então vamos começar o jogo, {J1} será o primeiro a jogar')
        sleep(0.8)
        for c in range(0,9):#Jogo
            if c%2!=0:
                if Ran==J2: #Caso a máquina seja o jogador 2
                    Jog_At=J2
                    print(f'{J2} irá escolher um número entre 1 e 9')
                    sleep(0.8)
                    Núm_Jog=randint(1,9)
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
                                print('\033[31mERRO! DIGITE UM NÚMERO VÁLIDO\033[m')
                        if 1<=Núm_Jog<=9:
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
                                print('\033[31mERRO! DIGITE UM NÚMERO VÁLIDO\033[m')
                        if 1<=Núm_Jog<=9:
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
                if opc():
                    break
            if VerEmp(): #Verifica se deu empate
                print('-='*16)
                print('FIM DE JOGO POR EMPATE!!'.center(30))
                print('-='*16)
                if opc():
                    break

    if inf==3: #Funcionamento jogo máquina contra máquina
        print('-=' *25)
        print(f'Então vamos começar o jogo, {J1} será o primeiro a jogar')
        sleep(0.8)
        for c in range(0,9): #Jogo
            if c%2==0: #Processo de jogada de Máquina 1
                Jog_At=J1
                print(f'{J1} irá escolher um número entre 1 e 9')
                sleep(0.8)
                Núm_Jog=randint(1,9)
                while True:
                    if not Teste(Núm_Jog):
                        Núm_Jog=randint(1,9)
                    else:
                        break
                print(f'{J1} escolheu o número: \033[34m{Núm_Jog}\033[m')
                sleep(0.8)
            else: #Processo de jogada de Máquina 2
                Jog_At=J2
                print(f'{J2} irá escolher um número entre 1 e 9')
                sleep(0.8)
                Núm_Jog=randint(1,9)
                while True:
                    if not Teste(Núm_Jog):
                        Núm_Jog=randint(1,9)
                    else:
                        break
                print(f'{J2} escolheu o número: \033[34m{Núm_Jog}\033[m')
                sleep(0.8)
            print('-='*16)
            print(f'\033[36mJogando',end='')
            for d in range(0,3):
                print('.',end='')
                sleep(0.5)
            print('\033[m')
            print('-='*16)
            sleep(0.5)
            Subs(Núm_Jog,Jog_At) #Substitui o número escolhido pela Máquina atual
            if VerVit(Jog_At): #Verifica se a Máquina atual venceu
                if opc():
                    break
            if VerEmp(): #Verifica se deu empate
                print('-='*16)
                print('FIM DE JOGO POR EMPATE!!'.center(30))
                print('-='*16)
                if opc():
                    break