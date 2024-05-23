def checa_numero(msg,msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num

def soma_lista(lista_numeros):
    print(f"Opa, cheguei na função soma_lista com: {lista_numeros}")
    soma = 0
    for num in lista_numeros:
        soma += num
    return soma
def media_lista(lista):
    print(f"Agora estou na função media_lista com: {lista}!!!!!!!")
    soma = soma_lista(lista)
    print(f"Terminou a função soma_lista e o resultado foi {soma}")
    media = soma/len(lista)
    print(f"Agora vou retornar a media {media}!!!!")
    return media

def filtra_pares_range(lista):
    pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
        print(pares)
    return pares
def filtra_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        print(pares)
    return pares
def meu_in(lista,buscar):
    for nome in lista:
        if nome == buscar:
            return True
    return False

def meu_index(lista,buscar):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return i
    return False

def forca_opcao(msg,lista_opcoes):
    opcao = input(msg)
    while not meu_in(lista_opcoes,opcao):
        opcao = input(msg)
    return opcao

def acha_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        print(f"Vou testar se {lista[i]} > {maior}")
        if lista[i] > maior:
            print(f"Deu certo, vou trocar {maior} por {lista[i]}")
            maior = lista[i]
            indice_maior = i
    return indice_maior
def meu_reverse(lista):
    ultimo = len(lista) - 1
    for i in range(len(lista)//2):
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
    return lista
lista = [1,2,3,4,5,6,7,8,9]
print(meu_reverse(lista))

precos = [10,15,1000000,50,20]
carros = ['up','uno','celtinha brabo','gol','kombi']
local_mais_caro = acha_maior(precos)
print(f"O carro mais caro é o {carros[local_mais_caro]} e custa {precos[local_mais_caro]}")

professores = ['Danilo','Jones','Yan','Caio','Lucas','Patrícia','Cordeiro']
materias = ['Python','Matemática','Edge','Web','Front','Story','Sw&TX']
prof = forca_opcao("Diga o nome de um professor: ",professores)
local_prof = meu_index(professores,prof)
print(local_prof)
print(f"O/a prof {professores[local_prof]} dá {materias[local_prof]}")

lista = [3,1,6,8,7,9,4,5,2,10]
pares = filtra_pares(lista)
print(pares)
media = media_lista(lista)
print(media)
soma = soma_lista(lista)
print(soma)

lista2 = [3,2,4,1,6,9,32,15,43,17]
soma = soma_lista(lista2)
print(soma)
ano = checa_numero("Diga seu ano de nascimento: ",'Ano deve ser um numero!')
print(ano)
qtd = checa_numero("Diga a quantidade de garrafas: ",'Qtd deve ser um numero!')
