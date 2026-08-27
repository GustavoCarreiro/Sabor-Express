import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}] 


def exibir_nome_do_programa():
    ''' Essa função exibe o nome do aplicativo na tela '''
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══ ██║ ██╔═══╝ ██╔═══╝ ██║ ╚═╝ ██║ ╚═╝ ██║ ╚═╝ ██║ ╚═╝ ██║ ╚═╝ ██║ ╚═╝ ██║ ╚═╝ ██║ ╚═╝ ██║ ╚═
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcao():
    ''' Essa função exibe as opções do menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Essa função exibe a mensagem de "Aplicativo finalizado" '''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    ''' Essa função solicita que uma tecla seja pressionada para voltar ao menu principal 
    
    Output: 
    - Volta ao menu principal 
    '''
    input('\nDigite uma tecla para retornar ao menu.')
    main()

def opcao_invalida():
    ''' Essa função exibe a mensagem "Opção Inválida" quando o usuário digite uma opção que não está no menu principal 
    
    Output:
    - Volta ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa função exibe o subtítulo de cada opção escolhida contido no menu principal 
    
    Inputs:
    - texto: str - O subtítulo de cada opção do menu principal
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante(): 
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes.
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:  ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:  ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():
    ''' Essa função é responsável por listar os restaurantes existentes e os novos restaurantes 
    
    Output: 
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status' )
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
   
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Essa função é responsável por exibir o status do restaurante entre "Ativado" ou "Desativado" 
    
    Input:
    - Status do restaurante

    Output:
    - Exibe a mensagem de alteração do status do restaurante escolhido
    '''
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar seu estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Essa função é responsável por exibir as opções disponíveis no menu principal e executar a opção escolhida 
    
    Input:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    ''' Essa função inicializa o aplicativo '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()

if __name__ == '__main__':
    main()
    