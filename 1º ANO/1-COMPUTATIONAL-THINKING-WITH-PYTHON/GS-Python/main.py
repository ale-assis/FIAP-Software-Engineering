'''def verificar_letra(opcao):
    while not opcao.isnumeric():
        print('ATENÇÃO: Letras NÃO são permitidas. Digite um dos números correspondentes!!')
        opcao = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
    opcao = int(opcao)
    return opcao


print('============================')
print('Bem vindo(a) ao SEASCASH!')
print('============================')
print()

verificar_usuario = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
while not verificar_usuario.isnumeric():
    print('ATENÇÃO: Letras NÃO são permitidas. Digite um dos números correspondentes!!')
    verificar_usuario = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
verificar_usuario = int(verificar_usuario)
while (verificar_usuario > 3):
    print('ATENÇÃO: Digite 1, 2, ou 3!!')
    verificar_usuario = input( 'Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
    while not verificar_usuario.isnumeric():
        print('ATENÇÃO: Letras NÃO são permitidas. Digite um dos números correspondentes!!')
        verificar_usuario = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
    verificar_usuario = int(verificar_usuario)


###mesmo codigo, so que com função
while (verificar_usuario > 3):
    print('ATENÇÃO: Digite 1, 2, ou 3!!')
    verificar_usuario = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
    checar_letra(verificar_usuario)
    verificar_usuario = int(verificar_usuario)'''



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

'''def fazer_cadastro(lista_usuarios):
    cadastro_user = input('Faça seu cadastro no SEASCASH. Digite um username: ')
    while cadastro_user in lista_usuarios:
        cadastro_user = input('O nome de usuário digitado JÁ EXISTE. Digite outro\n-> ')
    lista_usuarios.append(cadastro_user)
    return lista_usuarios, cadastro_user'''


print('============================')
print('Bem vindo(a) ao SEASCASH!')
print('============================')
print()

lista_usuarios = ['user1']
escolha_usuario = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
escolha_usuario = checar_letra(escolha_usuario)
escolha_usuario = checar_num(escolha_usuario)


while escolha_usuario == 1:
    username = input('Digite seu username para fazer login: ')
    if username in lista_usuarios:
        print('Você está logado.')
        print('Bem vindo ao menu')
        '''fazer página de login
        While true com menu com as 4 opções'''
    else:
        escolha_usuario = input('Não foi encontrado um usuário com esse nome na nossa base de dados.\nDigite 2 para fazer seu cadastro ou Digite 3 para encerrar.\n-> ')
        escolha_usuario = int(escolha_usuario)
        #fazer função pra cadastro e colocar aqui?
while escolha_usuario == 2:
    cadastro_user = input('Faça seu cadastro no SEASCASH. Digite um username: ')
    while cadastro_user in lista_usuarios:
        cadastro_user = input('O nome de usuário digitado JÁ EXISTE. Digite outro\n-> ')
    lista_usuarios.append(cadastro_user)
    print(f'Cadastro realizado com sucesso.\n {lista_usuarios}\nVocê será redirecionado ao MENU')
    escolha_usuario = 1
    fazer_login()
    '''#fazer página de cadastro
            #criar uma lista e armazenar os usuarios dentro dela
            #verificar se os usuarios estao com usuario na lista
            #se tiver = aviso de que já tá cadastrado o mesmo usuario (fazer while?)
            #se nao tiver = usar append pra adicionar o usuario na lista
            #com a conta feita, redireciona o usuario pro menu'''
    print('O programa será encerrado agora.')
    break

def cadastrar_residuos():
    residuo = input(
        '==============\nTABELA DE RESÍDUOS\n==============\nPAPEL: 10 pontos/kg\nMETAL: 20 pontos/kg\nVIDRO: 20 pontos/kg\nPLASTICO: 50 pontos/kg\nCadastre o seu resíduo (Insira o nome corretamente do resíduo que quer cadastrar, 1 por vez).\n-> ')
    sim_ou_nao = input('Deseja adicionar mais resíduos os carrinho?\nDigite S/s ou N/n\n-> ')
    return residuo, sim_ou_nao

def opcao_menu(menu):
    menu = input('===============\nSEASCASH MENU\n===============\n1- Cadastro de Resíduos\n2- Verificar SALDO de pontos\n3- Encerrar\n-> ')
    menu = checar_letra(menu)
    menu = checar_num(menu)
    return menu

##vai ter que ir usando break em todos os
# while quando terminar os códigos
#adicionar a perguntade kg APÓS a linha que fala:
# cadastre o resu residuo(insira o noem...)
