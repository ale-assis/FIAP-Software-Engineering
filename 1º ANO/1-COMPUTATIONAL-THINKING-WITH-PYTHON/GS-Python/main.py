def verificar_letra(opcao):
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
    verificar_usuario = int(verificar_usuario)