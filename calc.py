def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

num1 = int(input('Qual é o primeiro número? '))

for symbol in operations:
    print(symbol)

resultado = True
while resultado:
    confirm = input('Escolha a operação? ')
    num2 = int(input('Qual é o próximo número? '))
    calculation = operations[confirm]
    answer = calculation(num1, num2)

    print(f'{num1} {confirm} {num2} = {answer}')

    if (input(f'Quer continuar o calculo com {answer}? [S/N] ')) in 'Ss':
        num1 = answer
    else:
        resultado = False

