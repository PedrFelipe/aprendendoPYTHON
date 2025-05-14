from math import floor, ceil

num = float(input('Digite um número real: '))
parte_decimal = num - int(num)

if parte_decimal >= 0.5:
    inteiro = ceil(num)
else:
    inteiro = floor(num)


print(f'O número {num} tem a parte inteira {inteiro}')

# Exercicio 16
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
