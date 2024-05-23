def calcular_idade():
    ano = input('Informe o ano de nascimento: ')
    while not ano.isnumeric():
        ano = input('Digite um ano VÁLIDO: ')
    ano = int(ano)
    return 2024 - ano

def verificar_resposta():
    resposta = input('Digite "s"/"S" para iniciar a compra ou "n"/"N" para ir direto pro carrinho: ')
    while resposta.isnumeric and resposta != 's' and resposta != "S" and resposta != 'n' and resposta != 'N':
        resposta = input('Digite "s" ou "n" para prosseguir!!! -> ')
    return resposta

def exibir_menu():
    resposta_usuario = input('Nossas opções de vinho são:\n- Vinho Seco: R$100,00 (Digite 1)\n- Vinho Branco: R$120,00 (Digite 2)\n- Vinho Tinto: R$150,00 (Digite 3)\n Valor do frete: R$10,00\n O frete será aplicado a compras abaixo do valor de R$250,00\n Por favor, escolha uma opção acima (1,2 ou 3): ')
    return resposta_usuario

def forcar_escolha(opcao_do_usuario):
    while not opcao_do_usuario.isnumeric():
        opcao_do_usuario = input('Não é permitido digitar LETRAS!!!-> ')
    opcao_do_usuario = int(opcao_do_usuario)
    while opcao_do_usuario > 3:
        opcao_do_usuario = int(input('Digite um NÚMERO ENTRE 1, 2 e 3!!! -> '))
    return opcao_do_usuario

def classificar_escolha(lista_opcoes):
    for i in range(len(lista_opcoes)):
        if lista_opcoes[i] == escolha:
            print(f'Opção de vinho escolhida: {lista_vinhos[i]}')
    return True

def classificar_preco(escolha):
    preco_vinho = 0
    if escolha == 1:
        preco_vinho += 100
    elif escolha == 2:
        preco_vinho += 200
    else:
        preco_vinho += 300
    print(f'O preço do vinho escolhido é de R${preco_vinho}')
    return preco_vinho


print('Bem vindos a vinheria Agnello')
idade = calcular_idade()
if idade >= 18:
    endereco = input('Informe seu endereço: ')
    lista_vinhos = ['Vinho Seco', 'Vinho Branco', 'Vinho Tinto']
    lista_opcoes = [1,2,3]
    lista_preco = [100, 200, 300]
    frete = 10
    preco = 0
    resposta = verificar_resposta()
    while resposta == 's' or resposta == 'S':
        opcao = exibir_menu()
        escolha = forcar_escolha(opcao)
        vinho = classificar_escolha(lista_opcoes)
        preco += classificar_preco(escolha)
        print(f'TOTAL da sua compra atual: R$ {preco},00')




else:
    while True:
        print('Não é permitida bebidas alcóolicas para menores de idade!!!\n A compra será encerrada!!!')
        break