'''
#exercício 1
while True:
    nota = input("Diga sua nota: ")
    if nota.isnumeric():
        nota = int(nota)
        if nota >= 0 and nota <= 10:
            break
        else:
            print("O numero deve ser entre 0 e 10")
    else:
        print("Voce deve digitar um numero!")
#exercício2
nome = input("Diga seu nome: ")
while len(nome) < 3:
    nome = input("Diga seu nome: ")

while True:
    nome = input("Diga seu nome: ")
    if len(nome) >= 3:
        break
    print("Deve ter pelo menos 3 caracteres")

while True:
    idade = input("Diga sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade >= 0 and idade <= 150:
            break
        print("O numero deve ser entre 0 e 150")
    else:
        print("Voce deve digitar um numero!")

salario = input("Diga seu salario: ")
while not salario.isnumeric():
    salario = input("Diga seu salario: ")

sx = input("Diga f ou m\n->")
while sx != 'f' and sx != 'm':#not (sx == 'f' or sx == 'm'):
    sx = input("Diga f ou m\n->")

ec = input("Diga s,c,v,d:\n->")
while not (ec == 's' or ec == 'c' or ec == 'v' or ec == 'd'):
    print("Opção inválida!")
    ec = input("Diga s,c,v,d:\n->")

#exercício 3
a = 80
b = 200
anos = 0
while a < b:
    a *= 1.03
    b *= 1.015
    anos += 1
print(anos)

qtd = 0
soma = 0
while qtd < 5:
    num = input(f"Diga o {qtd+1}º numero: ")
    while not num.isnumeric():
        print("Deve ser número!")
        num = input(f"Diga o {qtd+1}º numero: ")
    num = int(num)
    soma += num
    qtd += 1
print(f"A soma dos numeros foi {soma} e a media foi {soma/qtd}")

#exercício 5
a = int(input("diga um numero: "))
b = int(input("diga outro numero: "))
if a > b:
    aux = a
    a = b
    b = aux
while a <= b:
    print(a)
    a+=1

usuario = input("Diga seu nome de usuario: ")
senha = input("Diga sua senha: ")
while usuario == senha:
    print("Nome de usuario não pode ser igual à senha!")
    usuario = input("Diga seu nome de usuario: ")
    senha = input("Diga sua senha: ")

while True:
    usuario = input("Diga seu nome de usuario: ")
    senha = input("Diga sua senha: ")
    if senha != usuario:
        break
    print("Nome de usuario não pode ser igual à senha!")

num = 1
while num <= 10:
    print(f"Tabuada do {num}:")
    i = 1
    while i <= 10:
        print(f"{num}*{i} = {num*i}")
        i += 1
    num += 1
    print()

a = 1
print(a,end= ' ')
b = 1
print(b,end= ' ')
i = 0
while i < 50:
    c = a + b
    print(c/b,end= '\n')
    a = b
    b = c
    i+=1

qtd = 0
pares = 0
while qtd < 10:
    num = input(f"Diga o {qtd+1}º número: ")
    while not num.isnumeric():
        num = input(f"Diga o {qtd+1}º número: ")
    num = int(num)
    if num % 2 == 0:
        pares += 1
    qtd += 1
print(f"Vc digitou {pares} pares e {qtd - pares} impares")

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
print(fatorial_string)

num = 71
i = 2
while i < num**0.5:
    print(f"{num}%{i} = {num%i}")
    if num % i == 0:
        print("Não é primo!")
        break
    i+=1
if i >= num**0.5:
    print("é primo")


salario = 1000
taxa = 0.015
partida = 1995
while partida < 2024:
    salario *= 1 + taxa
    taxa *= 2
    partida += 1
print(salario)
'''
primeiro = 0
segundo = 0
terceiro = 0
quarto = 0
while True:
    num = input("Diga um numero entre 0 e 100 e maior que 100 para sair:\n->")
    while not num.isnumeric():
        num = input("Diga um numero entre 0 e 100 e maior que 100 para sair:\n->")
    num = int(num)
    if num<=25:
        primeiro += 1
    elif num <=50:
        segundo += 1
    elif num <= 75:
        terceiro += 1
    elif num <= 100:
        quarto += 1
    else:
        break





