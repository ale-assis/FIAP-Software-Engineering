'''pares = 0
qtd = 0

while qtd < 5:
    num = int(input("Diga um numero: "))
    if num % 2 == 0:
        pares = pares + 1
        qtd = qtd + 1'''

'''senha_cadastrada = '1234'
senha_tentativa = input('Diga sua senha: ')
tentativas = 1
while senha_tentativa != senha_cadastrada and tentativas < 3:
    print(f'Vc é hacker? Só mais {3 - tentativas} tentativas!')
    senha_cadastrada = input('Diga a sua senha: ')
    tentativas = tentativas + 1
if senha_cadastrada == senha_tentativa:
    print('Acesso Liberado')
else:
    print('Sai Hacker')'''

'''resposta = input('Diga sim ou não')
while resposta != 'sim' and resposta != 'não':
    resposta = input('Diga sim ou não: ')

resposta = input('Diga sim ou não')
while not(resposta == 'sim' or resposta == 'não'):
    resposta = input('Diga sim ou não: ')'''

'''i = 0
soma = 0
while i < 100:
    i += 1
    soma += i * i
print(soma)
'''

'''num = input('Diga um numero: ')
while not num.isnumeric: #num.isnumeric() == False
    num = input('Diga um número: ')
num = int(num)

print('idahdiadh'.isnumeric())
print('234nsd'.isnumeric())
print('1.23'.isnumeric())
print('4354'.isnumeric())'''

while True: #num.isnumeric() == False
    num = input('Diga um número: ')
    if num.isnumeric():
        num = int(num)
        if not (num < 0 or num > 10):
            break

while num < 0 or num > 10:
