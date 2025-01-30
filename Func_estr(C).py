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
        print(f'PARABÉNS {inf}\033[33m, VOCÊ VENCEU'.center(50))
        print('-='*25)
        print('\033[m')
        return True
    if Ini[0][0]==Ini[1][0]==Ini[2][0]==inf or Ini[0][1]==Ini[1][1]==Ini[2][1]==inf or Ini[0][2]==Ini[1][2]==Ini[2][2]==inf:
        print('\033[33m-='*25)
        print(f'PARABÉNS {inf},\033[33m, VOCÊ VENCEU'.center(50))
        print('-='*25)
        print('\033[m')
        return True
    if Ini[0][0]==Ini[1][1]==Ini[2][2]==inf or Ini[0][2]==Ini[1][1]==Ini[2][0]==inf:
        print('\033[33m-='*25)
        print(f'PARABÉNS {inf}\033[33m, VOCÊ VENCEU'.center(50))
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
    #elif Op==2:
        #NovModo()
    else:
        print('SAINDO...')
        return False



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

#def NovModo():