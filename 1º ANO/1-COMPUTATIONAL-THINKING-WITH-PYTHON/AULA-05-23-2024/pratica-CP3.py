def calcular_idade():
    ano = input('Antes de começarmos, por favor informe o seu ano de nascimento: ')
    while not ano.isnumeric():
        ano = input('Informe um ANO válido!!! Letras não não permitidas!!! ->  ')
    ano = int(ano)
    return 2024 - ano

def verificar_resposta():
    resposta = input('Digite "s" para iniciar a compra e digite "n" para ir ao carrinho: ')
    while resposta.isnumeric and resposta != "s" and resposta != "S" and resposta != "n" and resposta != "N":
        resposta = input('Digite "s" ou "n".\nSomente LETRAS.\nNúmeros NÃO são permitidos!!! -> ')
    return resposta

def exibir_menu():
    resposta_usuario = input('Nossas opções de vinho são:\n- Vinho Seco: R$100,00 (Digite 1)\n- Vinho Branco: R$120,00 (Digite 2)\n- Vinho Tinto: R$150,00 (Digite 3)\n Valor do frete: R$10,00\n O frete será aplicado a compras abaixo do valor de R$250,00\n Por favor, escolha uma opção acima (1,2 ou 3): ')
    return resposta_usuario

def forcar_escolha(opcao_do_usuario):
    while not opcao_do_usuario.isnumeric():
        opcao_do_usuario = input('Não é permitido digitar letras!!! Digite um número -> ')
    opcao_do_usuario = int(opcao_do_usuario)
    while opcao_do_usuario > 3:
        opcao_do_usuario = int(input('O número tem que ser 1,2 ou 3!!! -> '))
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
        preco_vinho += 120
    else:
        preco_vinho += 150
    print(f'O preço do vinho escolhido é de R${preco_vinho}')
    return preco_vinho

def calcular_frete(preco_atual):
    if preco_atual < 250:
        print(f'Sua compra deu R${preco_atual},00 e está abaixo de R$250,00\nO frete de R$10,00 será aplicado agora.')
        preco_atual += frete
        print(f'Valor total da compra incluindo frete: R${preco_atual},00')
    else:
        print(f'Valor total da compra (FRETE GRÁTIS): R${preco_atual},00')
    return preco_atual

print('Boas vindas à Vinheria Agnello. Desejamos que tenha uma experiência de compra incrível!')
idade = calcular_idade()
if idade >= 18:
    endereco = input('Por favor, informe o seu endereco: ')
    frete = 10
    preco = 0
    lista_vinhos = ['Vinho Seco', 'Vinho Branco', 'Vinho Tinto']
    lista_opcoes = [1, 2, 3]
    lista_valores = [100, 120, 150]
    resposta = verificar_resposta()
    while resposta == "s" or resposta == "S":
        opcao = exibir_menu()
        escolha = forcar_escolha(opcao)
        vinho = classificar_escolha(lista_opcoes)
        preco += classificar_preco(escolha)
        print(f'Sua compra atual está no valor de R${preco},00.')
        resposta = verificar_resposta()
    print(f'Você está no CARRINHO. ')
    calcular_frete(preco)
    print(f'A entrega será feita no endereço: {endereco}.\nA Vinheria Agnello agradece a preferência.\nVolte sempre!\n')
    print()
    print('COMPRA ENCERRADA!!!')
else:
    while True:
        print('Não é permitida a venda de bebidas alcóolicas para menores de 18 anos!\nA operação de compra será ENCERRADA!')
        break