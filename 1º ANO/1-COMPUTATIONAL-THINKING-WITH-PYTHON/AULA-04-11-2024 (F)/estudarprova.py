#ex1

'''nota = input('Insira uma nota de 0 a 10: ')
while not nota.isnumeric():
    print('Digite um NÚMERO de 0 a 10!!')
    nota = input('Inserir nota: ')
nota = int(nota)
while nota > 10:
    print('Digite uma nota de 0 a 10!!')
    nota = input('Inserir nota: ')
print(f'Sua nota é {nota}!')'''

'''while True:
    nota = input('Digite uma nota de 0 a 10: ')
    if nota.isnumeric():
        nota = int(nota)
        if nota > 10:
            print('Insira uma nota ENTRE 0 e 10! ')
        else:
            break
    else:
        print('Deve ser um número!!')
print(f'Sua nota é {nota}')'''

#ex 2
nome = 'Alexandre'
print(len(nome))
