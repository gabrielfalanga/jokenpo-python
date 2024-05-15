from random import randint
import os

def exibir_tela_pricipal(titulo, mensagem):
    'Exibe a tela principal de jogadas e pontuação.'
    global pontos_jogador, pontos_pc
    limpar_console()
    print(titulo)
    print("'s' - sair  |  'r' - resetar pontos\n")
    print(f'{mensagem:^35}\n')
    print(f'\t     PONTUAÇÃO')
    print(f'\t |Você: {pontos_jogador:.>9}|')
    print(f'\t |PC: {pontos_pc:.>11}|\n')


def limpar_console():
    'Limpa o console, independente do sistema operacional.'
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:                # Unix/Linux/MacOS
        os.system('clear')


titulo_jogo_jokenpo = '''\
-----------------------------------
           J O K E N P O           
-----------------------------------'''

jogadas = ['pe', 'pa', 'te']
pontos_jogador = 0
pontos_pc = 0
msg = ''


while True:
    exibir_tela_pricipal(titulo_jogo_jokenpo, msg)

    jogada_jogador = input('\n(Pe)dra, (Pa)pel, ou (Te)soura? ').lower()[:2]
    jogada_pc = jogadas[randint(0,2)]

    if jogada_jogador == jogada_pc:
        msg = f'Empate.'

    elif jogada_jogador == 'pe':
        if jogada_pc == 'pa':
            msg = 'Você perdeu. Papel cobre Pedra.'
            pontos_pc += 1
        else:
            msg = 'Você ganhou! Pedra quebra Tesoura.'
            pontos_jogador += 1

    elif jogada_jogador == 'pa':
        if jogada_pc == 'te':
            msg = 'Você perdeu. Tesoura cobre Papel.'
            pontos_pc += 1
        else:
            msg = 'Você ganhou! Papel cobre Pedra.'
            pontos_jogador += 1    

    elif jogada_jogador == 'te':
        if jogada_pc == 'pe':
            msg = 'Você perdeu. Pedra quebra Tesoura.'
            pontos_pc += 1
        else:
            msg = 'Você ganhou! Tesoura corta Papel.'
            pontos_jogador += 1

    elif jogada_jogador == 'r':
        pontos_jogador = 0
        pontos_pc = 0
        msg = 'A pontuação foi resetada.'
    
    elif jogada_jogador == 's':
        limpar_console()
        msg = 'Até a próxima...'
        exibir_tela_pricipal(titulo_jogo_jokenpo, msg)
        break

    else:
        msg = 'Comando inválido.'
