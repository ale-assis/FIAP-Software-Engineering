'''def checa_numero(msg, msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num'''

'''ano = checa_numero('Diga seu ano de nascimento: ', 'Ano deve ser um número!')
print(ano)
qtd = checa_numero('Diga a quantidade de garrafas: ', 'Qtd deve ser um numero!')'''

'''def soma_lista(lista_numero):
    print(f'Opa, cheguei na função soma_lista com: {lista_numero}')
    soma = 0
    for num in lista_numero:
        soma += num
    return soma

def media_lista(lista):
    print(f'Agora estou na função media_lista com: {lista}!!!!!')
    soma = soma_lista(lista)
    print(f'Terminou a função soma_lista e o resultado foi {soma}')
    media = soma/len(lista)
    print(f'Agora vou retornar a media {media}!!!')
    return media

lista = [3,2,4,1,6,8,7,9,4,5,2,10]
media = media_lista(lista)
print(media)'''

# EX 1: Faça uma função que recebe uma lista de números e retorna outra lista contendo somente os pares da lista  original

'''lista = [1,2,3,4,5,6,7,8,9,10]
def adicionar_pares(lista_original):
    lista_pares = []
    for i in lista_original:
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

pares = adicionar_pares(lista)
print(pares)

#correção
def filtra_pares(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
        print(pares)
    return pares
    
def filtra_pares_range(lista):
    pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(num)
        print(pares)
    return pares

lista = [3,1,6,8,7,9,4,5,2,10]
pares = filtra_pares(lista)
print(pares)'''

'''# EX 2: Função que dada uma lista e um elemento, retorna True se o  elemento tá na lista e False caso contrário
def checar_elemento(lista, elemento):
    for i in lista:
        if i == elemento:
            return True
    return False

lista = ['São Paulo']
print(checar_elemento(lista, 1))'''

# EX 3: Função que dada uma lista e um elemento, retorne o local do elemento (seu índice)
#correção ex 3
def meu_index(lista, buscar):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return i
    return False

# possivel modelo do CP3 para estudarmos
def meu_in(lista, buscar):
    for nome in lista:
        if nome == buscar:
            return True
    return False

def forca_opcao(msg, lista_opcoes):
    opcao = input(msg)
    #enquanto não estiver na minha lista... porque eu quero que o usuário digite somente um dos nomes na lista
    while not meu_in(lista_opcoes, opcao):
        opcao = input(msg)
    return opcao

professores = ['Danilo', 'Jones', 'Yan', 'Caio', 'Lucas', 'Patrícia', 'Cordeiro']
materias = ['Python', 'Matemática', 'Edge', 'Web', 'Front', 'Story', 'Software Design']
prof = forca_opcao('Diga o nome de um professor: ', professores)
local_prof = meu_index(professores, prof)
print(f'O/a prof {professores[local_prof]} dá {materias[local_prof]}')

#buscar = 'Caio'
#achou = meu_in(professores, buscar)
#print(achou)

#Achando o maior elemento de uma lista

a = 2
b = 1
c = 3
d = 4
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d

#corrigindo o exercicio com for
#vai cair na prova também
def acha_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        print(f'Vou testar se {lista[i]} > {maior}')
        if lista[i] > maior:
            print(f'Deu certo, vou trocar {maior} por {lista[i]}')
            maior = lista[i]
            indice_maior = i
    return indice_maior

precos = [10, 15, 1000000, 50, 20]
carros = ['up', 'uno', 'celtinha brabo', 'gol', 'kombi']
local_mais_caro = acha_maior(precos)
print(f'O carro mais caro é o {carros[local_mais_caro]} e custa {precos[local_mais_caro]}')
acha_maior(precos)

#inverter uma
#lista = [1,2,3,4,5,6,7,8,9]
'''aux = lista[0]
lista[0] = lista[ultimo-i]
lista[ultimo-1] = aux
aux = lista[1]
lista[1] = lista[8-1]
lista[8-1] = aux'''

#tamanho - 1 = len(lista-1)

#correção
ultimo = len(lista) - 1
def meu_reverse(lista):
    for i in range(len(lista)//2):
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
    return lista

lista = [1,2,3,4,5,6,7,8,9]
lista
print(meu_reverse(lista))




