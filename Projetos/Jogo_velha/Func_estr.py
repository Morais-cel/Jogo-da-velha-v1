from time import sleep

Ini=[[1,2,3],[4,5,6],[7,8,9]]

def hud():
    for c1 in range(0,3):
        for c2 in range(0,3):
            if c2==2:
                Aux=''
            else:
                Aux='/'
            print(f' {Ini[c1][c2]} ',end=Aux)
            sleep(0.3)
        print('')

def Subs(val,inf):
    for c1 in range(0,3):
        for c2 in range(0,3):
            if Ini[c1][c2]==val:
                Ini[c1][c2]=inf
            else:
                pass
    hud()
    print('-='*25)

def VerVit(inf):
    if Ini[0][0]==Ini[0][1]==Ini[0][2]==inf or Ini[1][0]==Ini[1][1]==Ini[1][2]==inf or Ini[2][0]==Ini[2][1]==Ini[2][2]==inf:
        print('\033[33m-='*25)
        print(f'PARABÉNS {inf}\033[33m, VOCÊ VENCEU'.rjust(45))
        print('-='*25)
        print('\033[m')
        return True
    if Ini[0][0]==Ini[1][0]==Ini[2][0]==inf or Ini[0][1]==Ini[1][1]==Ini[2][1]==inf or Ini[0][2]==Ini[1][2]==Ini[2][2]==inf:
        print('\033[33m-='*25)
        print(f'PARABÉNS {inf}\033[33m, VOCÊ VENCEU'.rjust(45))
        print('-='*25)
        print('\033[m')
        return True
    if Ini[0][0]==Ini[1][1]==Ini[2][2]==inf or Ini[0][2]==Ini[1][1]==Ini[2][0]==inf:
        print('\033[33m-='*25)
        print(f'PARABÉNS {inf}\033[33m, VOCÊ VENCEU'.rjust(45))
        print('-='*25)
        print('\033[m')
        return True

def VerEmp():
    for c1 in range(0,3):
        for c2 in range(0,3):
            if type(Ini[c1][c2])==int:
                return False
            
def Teste(val):
    for c1 in range(0,3):
        for c2 in range(0,3):
            if Ini[c1][c2]==val:
                return True

def opc():
    print('-='*25)
    print('FIM DE JOGO...')
    print('1 -> Jogar Novamente')
    print('2 -> Mudar modo de jogo')
    print('3 -> Sair')
    print('-='*25)
    Op=int(input('Digite a opção desejada: '))
    if Op==1:
        JogNov()
    elif Op==2:
        NovModo()
    else:
        print('\033[31mSAINDO',end='')
        for c in range(0,3):
            print('.',end='')
            sleep(0.5)
        print('\033[m')
        return True

def JogNov():
    from Func_Jog import jogo
    global Ini
    Ini=[[1,2,3],[4,5,6],[7,8,9]]
    Maq='\033[34mO\033[m'
    hud()
    print('VAMOS COMEÇAR NOVAMENTE...')
    Jogador=str(f'\033[33m{input('Digite o símbolo que você deseja ser: ')}\033[m')
    print(f'Então você será {Jogador} e jogará contra {Maq}')
    print('-='*25)
    jogo(Jogador,Maq)

def NovModo():
    from Func_Jog import JogJog,JogMaq,MaqMaq

    global Ini
    Ini=[[1,2,3],[4,5,6],[7,8,9]]
    
    print('--'*10,'MENU','--'*10)
    print('1 -> Jogar contra outro jogador local')
    print('2 -> Jogar contra a máquina')
    print('3 -> Deixar a máquina jogar contra ela mesma')
    print('4 -> Sair')
    print('--'*23)
    while True:
        while True:
            try:
                Esc=str(input('Digite a opção desejada: '))
                Esc=int(Esc)
                break
            except:
                print('\033[31mERRO! POR FAVOR, DIGITE UM NÚMERO\033[m')
        if 0<Esc<=4:
            break
        else:
            print('\033[31mERRO! POR FAVOR, ESCOLHA UMA OPÇÃO ENTRE 1 E 4\033[m')
    print('-='*23)
    if Esc==1:
        JogJog()
    elif Esc==2:
        JogMaq()
    elif Esc==3:
        MaqMaq()
    else:
        print('\033[31mSAINDO',end='')
        for c in range(0,3):
            print('.',end='')
        print('\033[m]')
        return True