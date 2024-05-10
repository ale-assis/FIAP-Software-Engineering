'''def podeVotar(nome, idade):
    if idade >= 16:
        print(f'Sim, a pessoa {nome} pode votar')
        return True'''

'''def calcular_Idade(ano_atual, ano_nasc):
    idade = ano_atual - ano_nasc
    print(f'Você possui {idade} anos de idade!')
    return idade

a = calcular_Idade(2024, 1997)
print(calcular_Idade(2024, 1978))'''

'''def podeVotar(nome, ano_nascimento):
    idade = calculaIdade(ano_nascimento)
    a = 12
    if idade >= 16:
        print(f'Sim, a pessoa{nome} pode votar')
        return True
    else:
        print(f'Não, a pessoa {nome} pode votar')
        return False

def calculaIdade(ano_nascimento):
    return 2024-ano_nascimento

a = input('Digite um nome: ')
b = int(input('Digite um ano de nascimento'))
podeVotar(a,b)'''

'''#função que retorna o maior elemento de uma lista
def maior(numeros):
    maior_i = 0
    maior_v = numeros[0]
    for indice in range(len(numeros)):
        if numeros[indice] >  numeros[maior_i]:
            maior_i = indice
            maior_v = numeros[indice]
    return numeros[maior_i]

n = maior([10,20,2,30,7]) #maior retorna o 30, o n vai valer 30
n2 = maior([100,200,2,30,7]) #maior retorna o 200, o n vai valer 200
n3 = maior([-2,-3,-1]) #retorna -1

maior([30, 12, 45, 9, 60])'''

'''def mais_um(hora,minuto):
    prox_minuto = minuto+1
    if hora==23 and prox_minuto==60:
        return "00:00"
    if prox_minuto==60:
        hora = hora+1
        return f'{hora}:00'
    if prox_minuto < 10:
        return f'{hora}:0{prox_minuto}'
    return f'{hora}:{prox_minuto}'

print(mais_um(12,39))
print(mais_um(12,4))
print(mais_um(12,59))
print(mais_um(23,59))'''

'''#Exemplo de uso do método isnumeric()

#String que representa um número inteiro
numero_inteiro = '12345'
print(numero_inteiro.isnumeric()) # Saída: True

#String que representa um número negativo
numero_negativo = '-12345'
print(numero_negativo.isnumeric()) #Saída: False

#String que representa um número decimal
numero_decimal = '123.45'
print(numero_decimal.isnumeric()) #Saída: False

#String que contém caracteres não numéricos
texto = '123abc456'
print(texto.isnumeric()) #Saída: False'''

'''def pega_numero():
    while True:
        a = input("digite um numero positivo")
        if a.isnumeric():
            return int(a)
            
n = pega_numero()'''

'''def telValido(stringTel):
    if not stringTel.isnumeric():
        return False
    if len(stringTel) > 11 or len(stringTel) < 8:
        return False
    return True
    
telValido("111")
telValido("111333555")
telValido("11133aaa5")

a = input('digite um telefone')
while not telValido(a):
    a = input('digite um telefone')
print(f"legal, o tel {a} é valido")'''

def pega_um_dos_carros(lista):
    a = input("me diz um carro")
    while True:
        for carro in lista:
            if a == carro:
                return a
        a = input("me diz um carro")

pega_um_dos_carros(['fusca','kombi'])
pega_um_dos_carros(['uno','mobi','500'])


