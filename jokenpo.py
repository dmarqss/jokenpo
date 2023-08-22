from tkinter import *
from random import randint
perdeu = 'VC PERDEU'
ganhou = 'VC GANHOU'
empate = 'O JOGO EMPATOU'

def pedra():
    pc = randint(1, 3)
    if pc == 2:
        print('VC\033[31m PERDEU\033[m')
        textfim['text'] = perdeu
    elif pc == 3:
        print('VC\033[32m GANHOU\033[m!!!')
        textfim['text'] = ganhou
    else:
        print('O JOGO EMPATOU')
        textfim['text'] = empate
def papel():
    pc = randint(1,3)
    if pc == 1:
        print('VC\033[32m GANHOU\033[m!!!')
        textfim['text'] = ganhou
    elif pc == 3:
        print('VC\033[31m PERDEU\033[m')
        textfim['text'] = perdeu
    else:
        print('O JOGO EMPATOU')
        textfim['text'] = empate
def tesoura():
    pc = randint(1, 3)
    if pc == 1:
        print('VC\033[31m PERDEU\033[m')
        textfim['text'] = perdeu
    elif pc == 2:
        print('VC\033[32m GANHOU\033[m!!!')
        textfim['text'] = ganhou
    else:
        print('O JOGO EMPATOU')
        textfim['text'] = empate
def jokenpo():
    while True:
        pc = randint(1,3)
        if pc == 1:
            pcn = ('PEDRA')
        elif pc == 2:
            pcn = ("PAPEL")
        else:
            pcn = ('TESOURA')

        print('\033[34m===\033[m' * 20)
        print('{}JOKENPO'.format(' '* 25))
        print('\033[34m===\033[m' * 20)
        print('1-PEDRA\n2-PAPEL\n3-TESOURA')
        num = int(input('INSIRA O NUMERO DA SUA ESCOLHA:'))
        if num == 1:
            numn = ('PEDRA')
        elif num == 2:
            numn = ("PAPEL")
        else:
            numn = ('TESOURA')
        print('\033[34m===\033[m' * 20)
        print('VC ESCOLHEU:{}\nO COMPUTADOR ESCOLHEU:{}'.format(numn,pcn))
        print('\033[34m===\033[m' * 20)
        if num == 1:
            pedra()
        elif num == 2:
            papel()
        elif num == 3:
            tesoura()
        print('\033[34m===\033[m' * 20)
        a = str(input('QUER JOGAR DNV? S/N'))
        if a.upper() == 'S':
            print('\n' * 150)
        elif a.upper() == 'N':
            break

janela = Tk()
janela.title('JOKENPO')
orientacao = Label(janela, text='ESCOLHA UM PARA COMEÇAR A JOGAR')
orientacao.grid(column=1, row=0)
bpedra = Button(janela, text='PEDRA', command=pedra)
bpedra.grid(column=0, row=2)
bpapel = Button(janela, text='PAPEL', command=papel)
bpapel.grid(column=1, row=2)
btesoura = Button(janela, text='TESOURA', command=tesoura)
btesoura.grid(column=2, row=2)
textfim = Label(janela, text='')
textfim.grid(column=1, row=4)
janela.mainloop()