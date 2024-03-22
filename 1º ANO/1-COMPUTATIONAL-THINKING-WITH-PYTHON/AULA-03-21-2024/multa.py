'''velocidade = int(input('Informe o numero da velocidade (Nao precisa informar os km/h): '))
multa = 0
if velocidade <= 100:
    print('Está ISENTO de multa')
elif velocidade <= 120:
    multa = velocidade * 0.2
elif velocidade <= 150:
    multa = (120 * 0.2) + (velocidade * 0.3)
else:
    multa = (120 * 0.2) + (150 * 0.3) + (velocidade * 0.4)
if multa:
    print(f'A multa é de R${multa:.0f},00')
'''

# SOLUÇÃO
velocidade = int(input('Informe o numero da velocidade (Nao precisa informar os km/h): '))
if velocidade <= 100:
    print('Está ISENTO de multa')
else:
    if velocidade <= 120:
        multa = velocidade * 0.2
    elif velocidade <= 150:
        multa = (120 * 0.2) + (velocidade * 0.3)
    else:
        multa = (120 * 0.2) + (150 * 0.3) + (velocidade * 0.4)
    print(f'A multa é de R${multa:.0f},00')
