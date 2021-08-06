# calculadora simples

import time # biblioteca para cronomentar uma pausa no calculo

# função para somar os número escolhido pelop usuário
def soma(x, y):
    return x + y

# função para subtrair os número escolhido pelop usuário
def sub(x, y):
    return x - y

# função para multiplicar os número escolhido pelop usuário
def multi(x, y):
    return x * y

# função para dividir os número escolhido pelop usuário
def div(x, y):
    return x / y



print('****************** PYTHON CALCULADORA ****************** \n\n')
print('''Selecione o número da operação desejada:
1 - soma
2 - subitração
3 - multiplicação
4 - divisão \n''')

# pedi ao usuário que escolha as opções a cima 
opcao = int(input('Digite a Opção (1/2/3/4):'))

# pedi ao usuário os números para as operações
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

# modulo que atras 3 seg para mostras o resultado das operações
print('Calculando ...')
time.sleep(3)


if opcao == 1: # condição se o usuário escolher a operação soma
    print('\n')
    print(f'A soma de: {numero1} + {numero2} = {soma(numero1, numero2)}')
    print('\n')


elif opcao == 2: # condição se o usuário escolher a operação subtração
    print('\n')
    print(f'A subtração de: {numero1} - {numero2} = {sub(numero1, numero2)}')
    print('\n')

   
elif opcao == 3: # condição se o usuário escolher a operação multiplicação
    print('\n')
    print(f'A multiplicação de: {numero1} * {numero2} = {multi(numero1, numero2)}')
    print('\n')


elif opcao == 4: # condição se o usuário escolher a operação divisão
    print('\n')
    print(f'A divisão de: {numero1} / {numero2} = {div(numero1, numero2)}')
    print('\n')
    
else: # condição se o usuário escolher uma opção invalida
    print('Opção invalida!!! escolha (1/2/3/4)')