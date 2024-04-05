#ex1
'''num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

if num1 > num2:
    print(f'O maior número é {num1}')
else:
        print(f'O maior número é {num2}')'''

#ex2
'''idade = int(input('Informe a sua idade: '))

if (idade >= 16) and (idade < 18):
    print('Você é maior de 16 anos e seu voto é OPCIONAL')
elif idade >= 18:
    print('Você é maior de 18 anos e seu voto é OBRIGATÓRIO')
else:
        print('Você é menor de 16 anos e NÃO pode votar')'''

#ex3
'''gabarito = 1234
senha = int(input('Digite a senha: ')

if (senha == gabarito):
    print('Senha CORRETA! Acesso LIBERADO')
else:
    print('Senha INCORRETA! Acesso NEGADO')'''

#ex4
'''macas = int(input('Quantas maças você vai comprar? '))
preco = 0.3
if macas >= 12:
    preco = 0.25
print(f'Você comprou {macas} maças e o preço é R${macas*preco}')'''

#ex5
'''a = int(input("Diga o primeiro numero: "))
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
print(a,b,c)'''

#ex7
lados = int(input('Quantos lados tem o polígono? '))
valor = float(input('Qual o valor, em cm, dos lados desse polígono? '))

if lados == 3:
    forma = 'Triângulo'
    perimetro = valor * 3
elif lados == 4:
    forma = 'Quadrado'
    perimetro = valor * 4
else:
    forma = 'Pentágono'
    perimetro = valor * 5
print(f'O polígono em questão se trada de um {forma} e seu perímetro é de {perimetro}')

#ex8
lados = int(input('Quantos lados tem o polígono? '))
valor = float(input('Qual o valor, em cm, dos lados desse polígono? '))

if lados < 3:
    print('A figura em questão NÃO É UM POLÍGONO!')
elif lados == 3:
    forma = 'TRIÂNGULO'
    perimetro = valor * 3
elif lados == 4:
    forma = 'QUADRADO'
    perimetro = valor * 4
elif lados == 5:
    forma = 'PENTÁGONO'
    perimetro = valor * 5
else:
    print('Polígono NÃO IDENTIFICADO!')
if forma:
    print(f'O polígono em questão se trada de um {forma} e seu perímetro é de {perimetro}')

FiapaJ8b!