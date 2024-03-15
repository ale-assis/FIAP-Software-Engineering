# EXERCÍCIO 1
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor:'))
if valor1 > valor2:
    print(f'O valor {valor1} é maior que o valor {valor2}')
else:
    print(f'O valor {valor2} é maior que o valor {valor1}')

# EXERCÍCIO 2
idade = int(input('Informe a sua idade: '))
if (idade >= 16):
    print('Você pode votar.')
else:
    print('Você não pode votar')

# EXERCÍCIO 3
senha = int(input('Digite a senha correta: '))
validade = 1234
if (senha == validade):
    print('A senha está correta.')
else:
    print('A senha está incorreta')

# EXERCÍCIO 4
compra = int(input('Quantas maçãs você comprou? '))
if (compra < 12):
    valor = compra * 0.30
else:
    valor = compra * 0.25
print(f'Você comprou {compra} maça(s) e o valor foi de R${valor:.2f}')

# EXERCÍCIO 5
valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
valor3 = int(input('Digite o 3º valor: '))
if (valor1 > valor2) and (valor1 > valor3):
    valor1 = valor1
else:
    aux = valor1
    valor3 = valor1
if (valor2 > valor1) and (valor2 > valor3):
    aux = valor2
    valor1 = valor2
else:
    aux = valor3
    valor3 = valor2
if (valor3 > valor1) and (valor3 > valor2):
    valor1 = valor3
else:
    valor3 = valor3
print(f'A ordem crescente dos valores digitados é {valor1}, {valor2} e {valor3}')

# Estrutura de Repetição

senha = '123'
password = input('Diga sua senha: ')
while senha != password:
    print('Você é hacker?')
    password = input('Diga sua senha: ')
