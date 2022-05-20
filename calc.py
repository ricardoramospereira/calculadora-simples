def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

num1 = int(input('Whats is the first number: '))

for symbol in operations:
    print(symbol)
confirm = input('choose the operation: ')
num2 = int(input('Whats is the second number: '))
calculation = operations[confirm]
answer = calculation(num1, num2)

print(f'{num1} {confirm} {num2} = {answer}')
