'''O programa deve:

- Cumprimentar o usuário.
- Perguntar se é usuário novo ou se já tem conta
    - Se for usuário novo, ir para a etapa de cadastro
        -  Cadastrar usuário
    - Se já tiver conta, fazer login e ir pro menu (criar lista de nome de usuário, verificar se o user tá nessa lista, se tiver faz o login, se não repete)
- Exibir menu com opções:
    - Cadastro de Resíduos
    - Verificar pontuação
    - Converter pontos em desconto
    - Sair do Menu

# Ideias adicionais
- printar msg de que o desconto do IPTU vai ser aplicado nas parcelas atrelada ao cpf forneceido???
- Materiais = Papel, Plástico, Vidro, Metal
7'''

def checar_letra(opcao):
    while not opcao.isnumeric():
        print('ATENÇÃO: Letras NÃO são permitidas. Digite um dos números correspondentes!!')
        opcao = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
    opcao = int(opcao)
    return opcao

def checar_num(opcao):
    while opcao > 3:
        print('ATENÇÃO: Digite 1, 2, ou 3!!')
        opcao = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
        opcao = checar_letra(opcao)
    opcao = int(opcao)
    return opcao

print('============================')
print('Bem vindo(a) ao SEASCASH!')
print('============================')
print()

verificar_usuario = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
verificar_usuario = checar_letra(verificar_usuario)
verificar_usuario = checar_num(verificar_usuario)
while True:
    if verificar_usuario == 1:
        #fazer página de login
        while True:
            #menu com as 4 opções
    elif verificar_usuario == 2:
        #fazer página de cadastro
        #criar uma lista e armazenar os usuarios dentro dela
        #verificar se os usuarios estao com usuario na lista
        #se tiver = aviso de que já tá cadastrado o mesmo usuario (fazer while?)
        #se nao tiver = usar append pra adicionar o usuario na lista
        #com a conta feita, redireciona o usuario pro menu
    else:
        print('O programa será encerrado agora.')
        break



