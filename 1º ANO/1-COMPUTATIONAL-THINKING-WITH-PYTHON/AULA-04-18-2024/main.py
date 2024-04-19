# LISTA DE EXERCÍCIOS DA AULA DO DIA 11-04-2024 (ESTRUTURAS DE REPETIÇÃO - WHILE)

'''#ex1
#forma 1 de resolver o ex 1
while True
    nota = input('Diga sua nota: ')
    if nota.isnumeric():
        nota = int(nota)
        if nota >= 0 and nota <= 10:
            break
        else:
            print('O numero deve ser entre 0 e 10')
    else:
        print('Você deve digitar um número! ')

#ex1
#forma 2 de resolver o ex 1
nome = input('Diga seu nome: ')
while len(nome) < 3:
    nome = input('Diga seu nome:')

while True:
    nome = input('Diga seu nome: ')
    if len(nome) >= 3:
        break'''

'''#ex2
while True
    idade = input('Diga sua idade: ')
    if idade.isnumeric():
        idade = int(nota)
        if idade >= 0 and idade <= 150:
            break
        print('O numero deve ser entre 0 e 10')
    else:
        print('Você deve digitar um número! ')

salario = input('Diga seu salario: ')
while not salario.isnumeric():
    salario = input('Diga seu salario: ')

sx = input('Diga f ou m\n->')
while sx != 'f' and sx != 'm': #not (sx == 'f' or sx == 'm'):
    sx = input('Diga f ou m \n->')

ec = input('Diga s, c, v, d\n->')
while not (ec == 's' or ec == 'c' or ec == 'v' or ec == 'd'):
    print('Opção inválida!')
    ec = input('Diga s, c, v, d:\n->')'''

'''#ex3
a = 80
b = 200
anos = 0
while a < b:
    a *= 1.03
    b *= 1.015
    anos += 1
print(anos)'''

'''#ex4

qtd = 0
while qtd < 5:
    num = input(f'Diga o {qtd+1}° numero: ')
    while not num.isnumeric():
        print('Digite um numero: ')
        num = input(f'Diga 0 {qtd+1}° numero: ')
    num = int(num)
    soma += num
    qtd += 1
print(f'A soma dos numeros foi {soma} e a media foi {soma/qtd}')'''

'''#ex5
a = int(input('diga um numero: '))
b = int(input('diga outro numero: '))
if a > b:
    aux = a
    a = b
    b = aux
while a < b:
    print(a)
    a += 1'''

'''#ex6
usuario = input('Diga seu nome de usuario: ')
senha = input('Diga sua senha: ')
while usuario == senha:
    print('Nome de usuario não pode ser igual à senha!')
    usuario = input('Diga seu nome de usuario: ')
    senha = input('Diga sua senha: ')

while True:
    usuario = input('Diga seu nome de usuario: ')
    senha = input('Diga sua senha: ')
    if senha != usuario:
        break
    print('Nome de usuario não pode ser igual à senha!')'''

'''#ex7
num = 1
while num <= 10:
    print(f'Tabuada do {num}:')
    i = 1
    while i <= 10:
        print(f'{num}x{i} = {num*i} ')
        i +=1
    num +=1
    print()'''

'''#ex8

a = 1
print(, end=' ')
b = 1
print(b, end=' ')
i = 0
while i < 17:
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    i +=1'''

#ex9
qtd = 0
while qtd < 10:
    num = input(f'Diga o {qtd+1}° número: ')
    while not num.isnumeric():
        num = input(f'Diga o {qtd+1}° número: ')
    num = int(num)
    if num % 2 == 0:
        pares += 1
    qtd += 1
print(f'Vc digitou {pares} pares e {qtd - pares} impares')

'''#ex10
num = 5
fatorial = num
fatorial_string = f"{num}! = {num}"
print(fatorial_string)
while num > 1:
    num -= 1
    fatorial *= num
    fatorial_string += f"*{num}"
    print(fatorial_string)
fatorial_string += f" = {fatorial}"
print(fatorial_string)'''

'''#ex11
num = 15
i = 2
while i < num**0.5:
    print(f'{num}%{i} = {num%i}')
    if num % i == 0:
        print('Não é primo!')
        break
    i+=1
if i >= num**0.5:
    print('É primo')'''

#ex12
#igual o 4, já está pronto

#ex13
salario = 1000
taxa = 0.015
partida = 1995
while partida < 2000:
    salario *= 1 + taxa
    taxa *= 2
    partida += 1
print(salario)

#ex14
while True:
    num = input('Diga um numero entre 0 e 100 e maior que 100 para sair:\n-> ')
    while not num.isnumeric():
        num = input('Diga um numero entre 0 e 100 e maior que 100 para sair: \n->')
    num = int(num)
    if num <= 25:
        primeiro += 1
    elif num <= 50:
        segundo += 1
    elif num <= 50:
        segundo += 1
    elif num <= 75:
        terceiro += 1
    elif num <= 100:
        quarto +=1
    else:
        break




