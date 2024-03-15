# Classificando uma letra como VOGAL ou CONSOANTE
'''letra = input('Diga uma letra: ')
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'{letra} é vogal')
else:
    print(f'{letra} é consoante')'''

# Classificando se o aluno passou de semestre pela sua nota
'''nota = 7
if nota >= 6:
    print('Aprovado')
elif nota >= 4 and nota < 6:
    print('Exame')
else:
    print('Reprovado')'''

# Calculando imposto de renda de acordo com salario

salario = int(input('Diga o seu salário: '))
if salario < 1903.98:
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
print(f'Seu salário será de R${salario:.2f} após desconto de R${desconto:.2f}')
