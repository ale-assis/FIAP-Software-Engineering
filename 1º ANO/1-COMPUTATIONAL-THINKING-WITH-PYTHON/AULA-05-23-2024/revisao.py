#verificando se um numero vai ser um string
def verifica_numero(msg, msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input('Diga um numero: ')
    num = int(num)
    return num

qtd = verifica_numero('Diga a quantidade: ', 'A qtd deve ser um numero!')
ano = verifica_numero('Diga o ano de nascimento: ', 'O ano deve ser um numero!')
print(qtd)
print(ano)

#forçando o usuário a escolher algo
def forca_opcao(lista_opcoes, msg):
    #junte os elmentos dessa lista com este separador
    #você pega os elementos de uma lista e junta com algum elemento... nesse caso o \n
    msg_erro = '\n'.join(lista_opcoes)
    escolha = input(msg)
    while escolha not in lista_opcoes:
        print(f'Opção inválida! Somente essas: \n{msg_erro}')
        escolha = input(msg)
    return escolha

#achando o indice dentro de uma lista
def acha_indice(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

#achando o maior numero
def indice_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            indice_maior = i
            maior = precos[indice_maior]
    return indice_maior

#achando o menor numero
def indice_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < maior:
            indice_menor = i
            menor = precos[indice_menor]
    return indice_menor

def indice_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            indice_maior = i
            maior = precos[indice_menor]
    return indice_maior

#achando a média
def media(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma/len(lista)
    return media


pingas = ['Pitu', 'Seleta', 'Salinas', '51', 'Velho Barreiro']
precos = [10, 15, 12, 20, 17]
pinguinha = forca_opcao(pingas, 'Qual pinga você quer?\n->', )
indice_pinguinha = acha_indice(pingas, pinguinha)
print(f'A pinga {pingas[indice_pinguinha]} custa R${precos[indice_pinguinha]:.2f}')
print(f'A pinga {pingas} custa R${precos[indice_pinguinha]:.2f}')

#maior e menor
pingas = ['Pitu', 'Seleta', 'Salinas', '51', 'Velho Barreiro']
precos = [10, 15, 12, 20, 17]
indice_mais_caro = indice_maior(precos)
print(f'A pinga mais cara é a {pingas[indice_mais_caro]} e custa R${precos[indice_mais_caro]}')
pinguinha = forca_opcao(pingas, 'Qual pinga voce quer?\n->')
indice_pinguinha = acha_indice(pingas, pinguinha)


#continuar_ou_encerrar = forca_opcao(['continuar', 'encerrar'], 'Você deseja continuar ou encerrar?')


#usou ifs nesse bloco porque não são condicionais excludentes, se fosse usaria o elif
#mas você quer que todas as condicionais ocorram e não somente uma delas
a= 2
b= 1
c= 3
d= 7
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d

