print("""
█▀▀ █▀█ █░░ █▀▀ █▀▀ ▄▀█ █▀█   █▀▄ █▀▀   ░░█ █▀█ █▀▀ █▀█ █▀
█▄▄ █▄█ █▄▄ ██▄ █▄▄ █▀█ █▄█   █▄▀ ██▄   █▄█ █▄█ █▄█ █▄█ ▄█
""")

print('1. Cadastrar jogo')
print('2. Listar jogos')
print('3. Ativar jogo')
print('4. sair\n')

def finalizar_app():
    print('Encerrando programa')

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


# if(opcao_escolhida == 1){

# }