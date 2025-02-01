from Func_estr import hud
from Func_Jog import JogJog,JogMaq,MaqMaq

print('-='*25)
print(f'{'JOGO DA VELHA':>31}')
print('-='*25)
hud()
print('-='*25)
print('BEM VINDO AO JOGO DA VELHA')
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
    print('SAINDO...')
