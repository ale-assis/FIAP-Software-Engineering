'''print("Seja bem vindo à Vinheria Agnello!!!")
ano = int(input("Diga seu ano de nascimento: "))
idade = 2024 - ano
if idade < 18:
    print("Que feio!!!!!!!! Exclamation marks!!!")
else:
    endereco = input("Diga seu endereço: ")
    vinho1 = 'Chapinha'
    vinho2 = 'Sangue de Boi'
    vinho3 = 'Levanta Defunto'
    preco1 = 10
    preco2 = 20
    preco3 = 30
    frete = 10
    print(f"Essas são as nossas opções de vinhos:\n{vinho1}:R${preco1:.2f}"
          f"\n{vinho2}:R${preco2:.2f}\n{vinho3}:R${preco3:.2f}")
    escolha = input("Diga o nome do vinho de sua preferência: ")
    if escolha == vinho1:
        preco = preco1
    elif escolha == vinho2:
        preco = preco2
    else:
        preco = preco3
    qtd = int(input(f"Quantas garrafas de {escolha} você vai levar?\n->"))
    valor = qtd*preco
    if valor < 100:
        valor += frete
    else:
        print("Frete grátis!!!!")
    print(f"Voce gastou R${valor:.2f} em {qtd} garrafas de {escolha} que serão entregues"
          f"em {endereco}")

senha_cadastrada = '1234'
senha = input("Diga sua senha: ")
tentativas = 1
while senha != senha_cadastrada and tentativas < 3:
    print(f"Vc é hacker? Só mais {3-tentativas} tentativas")
    senha = input("Diga sua senha: ")
    tentativas += 1
if senha == senha_cadastrada:
    print("Acesso liberado")
else:
    print("Sai hacker")

idoso = input("Você é idoso? sim/não\n->")
while idoso!= 'sim' and idoso != 'não':
    idoso = input("Você é idoso? sim/não\n->")
if idoso == 'sim':
    print("top")
else:
    print("bb")

print('sjdfhds'.isnumeric())
print('shi4h54'.isnumeric())
print('23543'.isnumeric())

num = input("Diga um numero: ")
while not num.isnumeric():
    num = input("Diga um numero: ")
print(type(num),num)
num = int(num)
print(type(num),num)

while True:
    num = input("Diga um numero entre 10 e 20: ")
    if num.isnumeric():
        num = int(num)
        if num > 10 and num < 20:
            break
        else:
            print("Não está no intervalo correto!")
    else:
        print("Deve ser um número!!!")
i = 0
soma = 0
while i <100:
    i+=1
    soma += i*i
print(soma)

'''
nome = 'Danilo'
print(len(nome))
