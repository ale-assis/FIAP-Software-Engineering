'''lados = int(input("Diga qts lados: "))
forma = ''
if lados < 3:
    print("Não é um polígono")
elif lados == 3:
    forma = "Triângulo"
elif lados == 4:
    forma = "Quadrado"
elif lados == 5:
    forma = "Pentágono"
else:
    print("Não identificado")
if forma:
    medida = int(input("Diga a medida do lado: "))
    perimetro = lados*medida
    print(f"Voce escolheu um {forma} de perímetro {perimetro}")

lados = int(input("Diga qts lados: "))
if lados < 3:
    print("Não é um polígono")
elif lados > 5:
    print("Não identificado")
else:
    if lados == 3:
        forma = "Triângulo"
    elif lados == 4:
        forma = "Quadrado"
    else:
        forma = "Pentágono"
    medida = int(input("Diga a medida do lado: "))
    perimetro = lados*medida
    print(f"Voce escolheu um {forma} de perímetro {perimetro}")

v = int(input("Diga a velocidade: "))
if v<=100:
    print("Isento")
else:
    if v<=120:
        multa = 0.2*v
    elif v<=150:
        multa = 0.2*120+0.3*v
    else:
        multa = 0.2*120 + 0.3*150 + 0.4*v
    print(f"A multa será de R${multa:.2f}")

par = 0
qtd = 0
while qtd < 5:
    num = int(input("Diga um número: "))
    if num % 2 == 0:
        par += 1
    qtd += 1
print(f"{par} pares e {qtd-par} impares")

senha = "1234"
password = input("Diga sua senha: ")
tentativas = 1
while senha != password and tentativas < 3:
    print(f"Vc é hacker???? Só mais {3 - tentativas} tentativas")
    password = input("Diga sua senha: ")
    tentativas += 1
if senha == password:
    print("Acesso liberado")
else:
    print("Sai Hacker")

i = 0
soma = 0
while i < 100:
    i+=1
    soma = soma + i
    print(i)
print(soma)
'''

















