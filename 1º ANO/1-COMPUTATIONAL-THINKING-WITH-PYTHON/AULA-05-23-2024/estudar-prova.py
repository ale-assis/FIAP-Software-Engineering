print('Boa noite. Bem vindos a VINHERI AGNELLO.')

#calcular idade do usuário
ano = input('Antes de começarmos, por favor informe o seu ano de nascimento: ')
while not ano.isnumeric():
    ano = input('Antes de começarmos, por favor informe o seu ano de nascimento: ')
ano = int(ano)
idade = 2024 - ano

#condição para saber se entra na loja ou sai da loja
if idade >= 18:
    #usuário maior de idade = inicia a loja
    endereco = input('Por favor, informe o seu endereço: ')
    #definindo variáveis importantes pro código
    frete = 10
    preco = 0
    #resposta do usuário que inicia o loop da loja
    resposta = input('Digite "s" para iniciar a compra ou "n" para ir ao carrinho: ')
    while resposta.isnumeric and resposta != 's' and resposta != 'S' and resposta != 'n' and resposta != 'N':
        resposta = input('Digite "s" ou "n".\nSomente LETRAS.\nNúmeros NÃO são permitidos!!! -> ')
    while resposta == 's' or resposta == 'S':
        #resposta SIM que inicia o loop para o usuário escolher os vinhos
        escolha = input('Nossas opções de vinho são:\n- Vinho 1 (Digite 1)\n- Vinho 2 (Digite 2)\n- Vinho 3 (Digite 3)\n Valor do frete: R$10,00\n O frete será aplicado a compras abaixo do valor de R$250,00\n Por favor, escolha uma opção: ')
        #verifica se o usuário digitou uma letra invés de número
        while not escolha.isnumeric():
            escolha = input('Não é permitido digitar letras!!!  -> ')
        #transforma o número do input em INTEIRO
        escolha = int(escolha)
        #verifica se o usuário digitou um número MAIOR que 3
        while escolha > 3:
            escolha = input('O número tem que ser 1,2 ou 3!!! -> ')
        #verifica a escolha do usuário e classifica em vinho 1, 2 ou 3
        if escolha == 1:
            preco += 100
            vinho = 'VINHO 1'
        elif escolha == 2:
            preco += 200
            vinho = 'VINHO 2'
        else:
            preco += 300
            vinho = 'VINHO 3'
        #identifica qual foi o vinho escolhido pelo usuário
        print(f'O vinho escolhido foi o {vinho}.')
        #verifica a resposta para saber se entra ou se sai do carrinho
        resposta = input(f'Sua compra atual está no valor de R${preco},00.\n-- Digite "s" caso queira comprar outro vinho\n-- Digite "n" caso queira ir para ir para o carrinho\n -> ')
        #obriga o usuário a digitar a letra "s,S" ou "n, N"
        while resposta.isnumeric and resposta != 's' and resposta != 'S' and resposta != 'n' and resposta != 'N':
            resposta = input('Digite "s" ou "n".\nSomente LETRAS.\nNúmeros NÃO são permitidos!!! -> ')
    #abre o carrinho, caso a resposta seja "n, N"
    print('Você está no carrinho.')
    #calcula o frete ao preço dos vinhos
    if preco < 250:
        print(f'Sua compra deu R${preco},00 e está abaixo de R$250,00\nO frete de R$10,00 será aplicado agora.')
        preco += frete
        print(f'Valor total da compra incluindo frete: R${preco},00')
    #só vai calcular o frete caso entre na condicional do preço ser menor que 250, caso contrário deduz-se que o preço é maior que 250
    print(f'Valor total da compra (FRETE GRÁTIS): R${preco},00\nA entrega será feita no endereço: {endereco}.\nA Vinheria Agnello agradece a preferência.\nVolte sempre!\n')
    print()
    print('COMPRA ENCERRADA!!!')
#usuário menor de idade = encerra a loja
else:
    while True:
        print('Não é permitida a venda de bebida alcóolica para menores de 18 anos!!!\n A compra será encerrada!!!')
        break

