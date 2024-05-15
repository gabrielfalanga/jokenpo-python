from random import randint
import os

def limpar_console():
    'Limpa o console, independente do sistema operacional.'
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:                # Unix/Linux/MacOS
        os.system('clear')


t = ['ped', 'pap', 'tes']

titulo_jogo_jokenpo = '''
-----------------------------------
           J O K E N P O           
-----------------------------------
'''

pontos_jogador = 0
pontos_pc = 0
mensagem = ''

print('Olá, vamos jogar Pedra, Papel ou Tesoura!')
nome = input('Digite o seu nome: ').title().strip()
limpar_console()

def ganhou():
    global pontos_jogador
    pontos_jogador += 1
    print('\n-----------------------------------')
    print(mensagem)
    print(f'Computador: {pontos_pc}\n{nome}: {pontos_jogador}')
    print('-----------------------------------')

def perdeu():
    global pontos_pc
    pontos_pc += 1
    print('\n-----------------------------------')
    print(mensagem)
    print(f'Computador: {pontos_pc}\n{nome}: {pontos_jogador}')
    print('-----------------------------------')

while True:
    print(titulo_jogo_jokenpo)
    pc = t[randint(0,2)]
    print("\nPara sair, digite 'exit'\nPara reiniciar a pontuação, digite 'reset'\n")
    jogador = input('Pedra(ped), Papel(pap) ou Tesoura(tes)? ').lower().strip()
    
    if jogador == pc:
        print('\n------------------------------------')
        print('Empate.')
        print(f'Computador: {pontos_pc}\n{nome}: {pontos_jogador}')
        print('------------------------------------')
    elif jogador == 'ped':
        if pc == 'pap':
            mensagem = 'Você perdeu. Papel cobre Pedra.'
            perdeu()
        else:
            mensagem = 'Você ganhou! Pedra quebra Tesoura.'
            ganhou()
    elif jogador == 'pap':
        if pc == 'tes':
            mensagem = 'Você perdeu. Tesoura cobre Papel.'
            perdeu()
        else:
            mensagem = 'Você ganhou! Papel cobre Pedra.'
            ganhou()
    elif jogador == 'tes':
        if pc == 'ped':
            mensagem = 'Você perdeu. Pedra quebra Tesoura.'
            perdeu()
        else:
            mensagem = 'Você ganhou! Tesoura corta Papel.'
            ganhou()
    elif jogador == 'reset':
        pontos_jogador = 0
        pontos_pc = 0
        print('A pontuação foi resetada.\n')
        print(f'Computador: {pontos_pc}\n{nome}: {pontos_jogador}')
    elif jogador == 'exit':
        break
    else:
        print('Jogada inválida. Por favor, digite um comando válido.')
