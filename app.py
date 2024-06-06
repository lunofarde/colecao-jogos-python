import os

def exibir_nome_do_programa():
    print("""
    █▀▀ █▀█ █░░ █▀▀ █▀▀ ▄▀█ █▀█   █▀▄ █▀▀   ░░█ █▀█ █▀▀ █▀█ █▀
    █▄▄ █▄█ █▄▄ ██▄ █▄▄ █▀█ █▄█   █▄▀ ██▄   █▄█ █▄█ █▄█ █▄█ ▄█
    """)

def exibir_opcoes():
    print('1. Cadastrar jogo')
    print('2. Listar jogos')
    print('3. Ativar jogo')
    print('4. sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando programa')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Você escolheu a opção: {opcao_escolhida}')

    if opcao_escolhida == 1:
        print('Cadastro de jogos')
    elif opcao_escolhida == 2:
        print('Listar jogos')
    elif opcao_escolhida == 3:
        print('Ativar jogo')
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()