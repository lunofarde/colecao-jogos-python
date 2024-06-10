import os

alunos = []

def exibir_nome_do_programa():
    print("""██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
             ██║░░╚═╝███████║██║░░██║███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║  ██║░░██║█████╗░░
             ██║░░██╗██╔══██║██║░░██║██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║  ██║░░██║██╔══╝░░
             ╚█████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝  ██████╔╝███████╗
             ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚══════╝

░█████╗░██╗░░░░░██╗░░░██╗███╗░░██╗░█████╗░
██╔══██╗██║░░░░░██║░░░██║████╗░██║██╔══██╗
███████║██║░░░░░██║░░░██║██╔██╗██║██║░░██║
██╔══██║██║░░░░░██║░░░██║██║╚████║██║░░██║
██║░░██║███████╗╚██████╔╝██║░╚███║╚█████╔╝█
    """)

def cadastrar_novo_aluno():
    os.system('cls')
    print('cadastrar novo aluno\n')
    nome_aluno = input('Digite o nome do aluno: ')
    idade_do_aluno = input('Digite a idade do aluno: ')    
    nota = input('Digite a nota do aluno: ') 
    dados_do_aluno = {'nome': nome_aluno, 'idade':idade_do_aluno, 'nota':nota}  
    alunos.append(dados_do_aluno)    

def listar_aluno():
    os.system('cls')
    print('Lista de alunos\n')
    for aluno in alunos:
        nome_aluno = aluno['nome']
        idade_do_aluno = aluno['idade']
        nota_do_aluno = aluno['nota']       
        print(f' - | {nome_aluno} | {idade_do_aluno} | {nota_do_aluno}' )

def main():
    while True:
        opcao = input('voce quer cadatras um aluno? (s\n)')
        if opcao ==  's':
            cadastrar_novo_aluno()
        elif opcao == 'n':
            listar_aluno()
            break
        else:
            print('opção invalida. digite outra opção')
    
if __name__ == '__main_':
    main()
