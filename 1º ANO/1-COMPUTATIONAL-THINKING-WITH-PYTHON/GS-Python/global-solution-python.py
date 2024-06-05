# FIAP GLOBAL SOLUTION - COMPUTIIONAL THINKING WITH PYTHON
# ENGEHARIA DE SOFTWARE - 1º ANO (NOTURNO)
# ALUNOS:
# ALEXANDRE ASSIS DO NASCIMENTO - RM:
# HERBERT DE SOUZA - RM:

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

def cadastrar_residuos(residuo):
    residuo = input(
        '==============\nTABELA DE RESÍDUOS\n==============\nPAPEL: 10 pontos/kg\nMETAL: 20 pontos/kg\nVIDRO: 20 pontos/kg\nPLASTICO: 50 pontos/kg\nCadastre o seu resíduo (Insira o nome corretamente do resíduo que quer cadastrar, 1 por vez).\n-> ')
    sim_ou_nao = input('Deseja adicionar mais resíduos os carrinho?\nDigite S/s ou N/n\n-> ')
    return residuo, sim_ou_nao

def exibir_menu(menu):
    menu = input('===============\nSEASCASH MENU\n===============\n1- Cadastro de Resíduos\n2- Verificar SALDO de pontos\n3- Encerrar\n-> ')
    menu = checar_letra(menu)
    menu = checar_num(menu)
    menu = int(menu)
    return menu

print('============================')
print('Bem vindo(a) ao SEASCASH!')
print('============================')
print()

lista_usuarios = ['user1']
escolha_usuario = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
escolha_usuario = checar_letra(escolha_usuario)
escolha_usuario = checar_num(escolha_usuario)
while True:
    while escolha_usuario != 3:
        if escolha_usuario == 1:
            username = input('Digite seu username para fazer login: ')
            if username in lista_usuarios:
                print('Você está logado.')
                # iniciando menu
                opcao_menu = ''
                opcao_menu = exibir_menu(opcao_menu)
                # iniciando processo de cadastro
                while opcao_menu == 1:
                    lista_residuos = []
                    lista_pontos = []
                    lista_kilos = []
                    # iniciando cadastro dos resíduos
                    residuo = ''
                    kilo = int(input(f'Quantos kilos você vai descartar desse resíduo? ->'))
                    lista_kilos.append(kilo)
                    residuo, sim_ou_nao = cadastrar_residuos(residuo)
                    lista_residuos.append(residuo)
                    while sim_ou_nao == 'S' or sim_ou_nao == 's':
                        kilo = int(input(f'Quantos kilos você vai descartar? ->'))
                        lista_kilos.append(kilo)
                        residuo, sim_ou_nao = cadastrar_residuos(residuo)
                        lista_residuos.append(residuo)
                    '''print(lista_residuos)
                    print(sim_ou_nao)
                    print(lista_kilos)'''
                    break #break do while cadastrar produtos
                # voltando ao menu principal
                opcao_menu = exibir_menu(opcao_menu)
                # verificando pontuação
                if opcao_menu == 2:
                    for i in range(len(lista_residuos)):
                        residuo_indice = lista_residuos[i]
                        kilo = lista_kilos[i]
                        if residuo_indice == 'Papel' or residuo_indice == 'papel':
                            lista_pontos.append(10*kilo)
                        elif residuo_indice == 'Metal' or residuo_indice == 'metal':
                            lista_pontos.append(20*kilo)
                        elif residuo_indice == 'Vidro' or residuo_indice == 'vidro':
                            lista_pontos.append(20*kilo)
                        elif residuo_indice == 'Plastico' or residuo_indice == 'plastico':
                            lista_pontos.append(50*kilo)
                    print(kilo)
                    total_pontos = 0
                    for pontos in lista_pontos:
                        total_pontos += pontos
                    print(f'Resíduos descartados: {lista_residuos}\nPARABÉNS, {username}, seu Saldo total é de: {total_pontos} pontos!\nConsulte os estabelecimentos parceiros por meio dos seus sites ou pessoalmente para se informar sobre as trocas de pontos por recompensas exclusivas\nAo atingir 250 pontos, você pode utilizar seus pontos para ganhar 10% de desconto no IPTU\nAo atingir 500 pontos, você pode utilizar seus pontos para ganhar 30% de desconto no IPTU\nAo atingir 1000 pontos, você pode utilizar seus pontospara ganhar 80% de desconto no IPTU')
                    opcao_menu = exibir_menu(opcao_menu)
                    break
            else:
                escolha_usuario = input('Não foi encontrado um usuário com esse nome na nossa base de dados.\nDigite 2 para fazer seu cadastro ou Digite 3 para encerrar.\n-> ')
                escolha_usuario = int(escolha_usuario)
        if escolha_usuario == 2:
            cadastro_user = input('Faça seu cadastro no SEASCASH. Digite um username: ')
            while cadastro_user in lista_usuarios:
                cadastro_user = input('O nome de usuário digitado JÁ EXISTE. Digite outro\n-> ')
            lista_usuarios.append(cadastro_user)
            print(f'Cadastro realizado com sucesso.\n {lista_usuarios}\nVocê será redirecionado ao MENU')
        '''escolha_usuario = 1'''
    print('O programa será encerrado agora.')
    break




