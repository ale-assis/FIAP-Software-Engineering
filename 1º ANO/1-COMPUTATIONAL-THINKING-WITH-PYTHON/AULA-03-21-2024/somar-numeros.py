# Somar todos os numeros de 1 a 100. Quanto é a soma de todos os numeros de 1 a 100

'''num = 1
while num != 100:
    soma = num + 1
print(soma)
'''

'''i = 0
soma = 0

while i != 100:
    i += 1
    soma += i
print(soma)'''

#correção do prof

'''i = 0
soma = 0
while i < 100:
    1+=1
    soma = soma + 1
    print(i)'''

# Enquanto a resposta do usuario nao for sim ou nao, repita a pergunta

resposta = input('Digite somente SIM ou NAO')
while resposta != 'SIM' and  resposta != 'NAO':
    print(input('Resposta errada! Tente novamente'))
print('Resposta CORRETA')
