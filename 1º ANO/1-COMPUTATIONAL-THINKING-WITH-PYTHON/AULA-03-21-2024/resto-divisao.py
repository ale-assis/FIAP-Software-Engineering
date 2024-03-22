# PEDIR 5 NUMEROS PRO USUARIO E CONTE QUANTOS DELES SAO PAR E IMPAR.

par = 0
qtd = 0
while qtd < 5: 
    num = int(input('Diga um número: '))
    if num % 2 == 0:
        par = par + 1
    qtd = qtd + 1
print(f'{par} pares e {qtd-par} impares')

