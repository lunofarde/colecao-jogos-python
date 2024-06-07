import os

def exibir_nome_do_programa():

    print('''
░█████╗░░█████╗░██╗░░░░░███████╗░█████╗░░█████╗░░█████╗░  ██████╗░███████╗
██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██║░░░░░█████╗░░██║░░╚═╝███████║██║░░██║  ██║░░██║█████╗░░
██║░░██╗██║░░██║██║░░░░░██╔══╝░░██║░░██╗██╔══██║██║░░██║  ██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝███████╗███████╗╚█████╔╝██║░░██║╚█████╔╝  ██████╔╝███████╗
░╚════╝░░╚════╝░╚══════╝╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚══════╝

░░░░░██╗░█████╗░░██████╗░░█████╗░░██████╗
░░░░░██║██╔══██╗██╔════╝░██╔══██╗██╔════╝
░░░░░██║██║░░██║██║░░██╗░██║░░██║╚█████╗░
██╗░░██║██║░░██║██║░░╚██╗██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝██████╔╝
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░╚═════╝░''')
def exibir_opcao():
    print('1. cadrastra jogos')
    print('2. listar jogos')
    print('3. ativar jogod')
    print('4. sair\n')
def finalizar_app():
    os.sytem('cls')
    print('encerrando programa')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para reiniciar: ')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('escolha uma das opção: '))
        print('voce escolho a opção: ' , opcao_escolhida)
        print(f'voce escolho a opção: {opcao_escolhida}\n')
    
        if opcao_escolhida == 1:
            print('cadastro de jogos')
        elif opcao_escolhida == 2:
            print('lista de jogos')
        elif opcao_escolhida == 3:
            print('ativar jogos')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        

def main():
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()

if __name__ == '__main__':
     main()
   

