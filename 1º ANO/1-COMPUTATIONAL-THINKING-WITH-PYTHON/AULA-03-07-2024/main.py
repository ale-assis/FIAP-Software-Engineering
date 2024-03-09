'''nome = input('Digite o seu nome: ')
primeiro_numero = int(input(f'{nome}, diga o primeiro número: '))
segundo_numero = int(input(f'{nome}, diga o segundo número: '))

soma = primeiro_numero + segundo_numero
print(f'A soma entre {primeiro_numero} e {segundo_numero} dá {soma}')

primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite um outro número: '))10
operacao = primeiro_numero + segundo_numero
print(f'A soma entre {primeiro_numero} e {segundo_numero} dá {operacao}')

operacao = primeiro_numero - segundo_numero
print(f'A subtracao entre {primeiro_numero} e {segundo_numero} dá {operacao}')

operacao = primeiro_numero / segundo_numero
print(f'A divisao entre {primeiro_numero} e {segundo_numero} dá {operacao}')

operacao = primeiro_numero * segundo_numero
print(f'A multipicação entre {primeiro_numero} e {segundo_numero} dá {operacao}')

# Pratica de variável acumuladora
frase = '0 '
print(frase)
frase = frase + 'São Paulo'
print(frase)
frase = frase + ' foi'
print(frase)
frase = frase + ' roubado'
print(frase)
frase = frase + ' domingo'
print(frase)

#OPERADORES BOOLEANOS

primeiro_numero = 2
segundo_numero = 3

a = primeiro_numero > segundo_numero
print(f'A comparação {primeiro_numero} > {segundo_numero} dá {a}')

a = primeiro_numero >= segundo_numero
print(f'A comparação {primeiro_numero} >= {segundo_numero} dá {a}')

a = primeiro_numero < segundo_numero
print(f'A comparação {primeiro_numero} < {segundo_numero} dá {a}')

a = primeiro_numero <= segundo_numero
print(f'A comparação {primeiro_numero} <= {segundo_numero} dá {a}')

a = primeiro_numero == segundo_numero
print(f'A comparação {primeiro_numero} == {segundo_numero} dá {a}')

a = primeiro_numero != segundo_numero
print(f'A comparação {primeiro_numero} != {segundo_numero} dá {a}')'''


'''a = 2
b = 3
c = 4
d = 5'''
'''print(f'A comparação {a} > {b} or {c} > {d}, ou seja, {a > b} or {c > d} dá {a > b or c > d}')
print(f'A comparação {a} < {b} or {c} > {d}, ou seja, {a < b} or {c > d} dá {a < b or c > d}')
print(f'A comparação {a} > {c} or {d} > {c}, ou seja, {a > c} or {d > c} dá {a > c or d > c}')
print(f'A comparação {d} > {c} or {c} < {d}, ou seja, {d > c} or {c < d} dá {d > c or c < d}')
'''

'''print(f'A comparação {a} > {b} and {c} > {d}, ou seja, {a > b} and {c > d} dá {a > b and c > d}')
print(f'A comparação {a} < {b} and {c} < {d}, ou seja, {a < b} and {c < d} dá {a < b and c < d}')
print(f'A comparação {b} > {c} and {c} < {d}, ou seja, {b > c} and {c < d} dá {b > c and c < d}')
print(f'A comparação {d} > {c} and {a} > {b}, ou seja, {d > c} and {a > b} dá {d > c and a > b}')'''

# CONDICIONAIS

'''idade = int(input('Diga sua idade: '))
if idade < 18:
    print('Você não pode beber!!!!')
    print('Que feio!!!')

if idade >= 18:
    print('Pode beber')'''

'''idoso = input('Você é idoso? ')
cadeirante = input('Você é cadeirante? ')
if idoso == 'sim' or cadeirante == 'sim':
    print('Pode estacionar')
'''

'''idade = int(input('Diga sua idade: '))
if idade < 18:
    print('Você não pode beber!!!!')
    print('Que feio!!!')
else:
    print('Pode beber')'''

# Exercício

'''lista_vogais = 'a e i o u'
letra = input('Digite uma letra: ')
if letra in lista_vogais:
    print(f'A letra {letra} é uma vogal!')
else:
    print(f'A letra {letra} é uma consoante!')'''

# Distributiva
''' ao invés de escrever:
letra = input('Digite uma letra: ')
if letra == "a" or "e" or "i" or "o" or "u":
    print(f'{letra} é vogal')
else:
    print(f'{letra} é consoante ')
use a solução abaixo:'''

'''letra = input('Digite uma letra: ')
if letra == 'a' or letra =='e' or letra =='i' or letra =='o' or letra =='u':
    print(f'{letra} é vogal')
else:
    print(f'{letra} é consoante ')


if 'danilo':
    print('oi')
if '':
    print('oieeeee')
letra = input('Digite uma letra: ')'''

'''vogal = False
letra = input('Diga uma letra: ')
if letra == 'a':
    print('Vogal')
    vogal = True
if letra == 'e':
    print('Vogal')
    vogal = True
if letra == 'i':
    print('Vogal')
    vogal = True
if letra == 'o':
    print('Vogal')
    vogal = True
if letra == 'u':
    print('Vogal')
    vogal = True
if not vogal:
    print('Consoante')'''

'''letra = input('Diga uma letra: ')
if letra == 'a':
    print('Vogal')
elif letra == 'e':
    print('Vogal')
elif letra == 'i':
    print('Vogal')
elif letra == 'o':
    print('Vogal')
elif letra == 'u':
    print('Vogal')
else:
    print('Consoante')'''

salario = float(input('Digite o seu salário: '))
aliquota1 = 0.075
aliquota2 = 0.15
aliquota3 = 0.225
aliquota4 = 0.275
if salario <= 1903.98:
    print('Você está ISENTO da declaração de imposto de renda')
elif salario == 1903.99 or salario <= 2826.65:
    ir = salario * aliquota1
    print(f'O imposto de renda com a aliquota {aliquota1} aplicada é de {ir}, e a parcela a deduzir será de R$ 142,80')
elif salario == 2826.66 or salario <= 3751.05:
    ir = salario * aliquota2
    print(f'O imposto de renda com a aliquota {aliquota2} aplicada é de {ir}, e a parcela a deduzir será de R$ 354,80')
elif salario == 3751.06 or salario <= 4664.68:
    ir = salario * aliquota3
    print(f'O imposto de renda com a aliquota {aliquota3} aplicada é de {ir}, e a parcela a deduzir será de R$ 636,13')
else: '''salario > 4664.69:'''
    ir = salario * aliquota4
    print(f'O imposto de renda com a aliquota {aliquota4} aplicada é de {ir}, e a parcela a deduzir será de R$ 869,36')

#Versão do professor
salario = int(input('Digite seu salário: '))
if salario <=1903.98:
    aliquota = 0
elif salario <= 2826.65:
    aliquota = 7.5
elif salario <= 3751.05:
    aliquota = 1.5
# Não deu pra completar o código, pq não deu pra tirar foto do código, mas deu pra pegar o raciocínio...
