'''letra = input("Diga uma letra: ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"{letra} é vogal")
else:
    print(f"{letra} é consoante")

nota = 7
if nota >= 6:
    print("Aprovado")
elif nota>=4:
    print("Exame")
else:
    print("Reprovado")

salario = int(input("Diga seu salario: "))
if salario <= 1903.98:
    aliquota = 0
elif salario <= 2826.68:
    aliquota = 7.5/100
elif salario <= 3751.05:
    aliquota = 15/100
elif salario <= 4664.68:
    aliquota = 22.5/100
else:
    aliquota = 27.5/100
desconto = aliquota*salario
salario = salario - desconto
print(f"Seu salário será de R${salario:.2f} após desconto de R${desconto:.2f}")

a = 1
b = 2
aux = a
a = b
b = aux
print(a,b)

#Exercício 1
primeiro_numero = int(input("Diga um numero: "))
segundo_numero = int(input("Diga outro numero: "))
if primeiro_numero > segundo_numero:
    print(primeiro_numero)
else:
    print(segundo_numero)

#Exercício 2
ano = int(input("Diga seu ano de nascimento: "))
idade = 2024 - ano
if idade >= 18:
    print("É obrigatório votar")
elif idade >= 16:
    print("É opcional votar")
else:
    print("Não pode votar")
#Exercício 3
senha = 1234
password = int(input("Diga sua senha: "))
if senha == password:
    print("Acesso liberado")
else:
    print("Acesso negado")

senha = '1234'
password = input("Diga sua senha: ")
if senha == password:
    print("Acesso liberado")
else:
    print("Acesso negado")'''

#Exercício 4
qtd = int(input("Qts maçãs? "))
preco = 0.3
if qtd >= 12:
    preco = 0.25
print(f"Vc vai gastar R${preco*qtd}")

'''
#Exercício 6
sexo = float(input("1: feminino, 2:masculino: "))
altura = float(input("Diga sua altura: "))
if sexo == 1:
    peso = 62.1*altura-44.7
else:
    peso = 72.7*altura-58
print(f"peso ideal: {peso}")

#Exercício 7
lados = int(input("Qts lados tem o polígono? "))
valor = float(input("Qual o valor do lado? "))
if lados == 3:
    forma = 'triangulo'
    perimetro = 3*valor
elif lados == 4:
    forma = 'quadrado'
    perimetro = 4*valor
else:
    forma = 'pentagono'
    perimetro = 5*valor
print(f"Voce escolheu um {forma} com perimetro de {perimetro}")

#Exercício 8
lados = int(input("Qts lados tem o polígono? "))
valor = float(input("Qual o valor do lado? "))
forma = ''
if lados < 3:
    print("Não é Polígono")
elif lados == 3:
    forma = 'triangulo'
    perimetro = 3*valor
elif lados == 4:
    forma = 'quadrado'
    perimetro = 4*valor
elif lados == 5:
    forma = 'pentagono'
    perimetro = 5*valor
else:
    print("Polígono não idetificado")
if forma:
    print(f"Voce escolheu um {forma} com perimetro de {perimetro}")

#Exercício 10
lado1 = int(input("Digao primeiro lado"))
lado2 = int(input("Digao segundo lado"))
lado3 = int(input("Digao terceiro lado"))

if lado1 == lado3 and lado2 == lado3:
    forma = "equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    forma = "isósceles"
else:
    forma = 'escaleno'
print(f"Seu triangulo é {forma}")
#Ecercício 11
ang1 = int(input("Digao primeiro angulo"))
ang2 = int(input("Digao segundo angulo"))
ang3 = int(input("Digao terceiro angulo"))

if ang1 == 90 or ang2 == 90 or ang3 == 90:
    forma = "retangulo"
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    forma = 'obtuso'
else:
    forma = 'agudo'
print(f"Seu triangulo é {forma}")

#Exercício 9
a = int(input("Diga o primeiro numero: "))
b = int(input("Diga o segundo numero: "))
c = int(input("Diga o terceiro numero: "))

if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

#Exercício 5
a = int(input("Diga o primeiro numero: "))
b = int(input("Diga o segundo numero: "))
c = int(input("Diga o terceiro numero: "))

if a>b and a>c:
    aux = a
    a = c
    c = aux
elif b>c:
    aux = b
    b = c
    c = aux
if a > b:
    aux = a
    a = b
    b = aux
print(a,b,c)

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
meio = a + b + c - menor - maior
print(menor,meio,maior)

senha = '1234'
password = input("Diga sua senha: ")
while senha != password:
    print("Vc é hacker? ")
    senha = input("Diga sua senha: ")'''
