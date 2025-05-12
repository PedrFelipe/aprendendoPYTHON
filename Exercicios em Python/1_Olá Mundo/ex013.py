salario = float(input("Qual o salário atual? R$"))
aumento = int(input("Qual a porcentagem de aumento? "))
novo_salario = salario * (1 + aumento / 100)

print(f'O salário atual é R${salario:.2f} e o novo salário com {aumento}% de aumento é R${novo_salario:.2f}.')

# Exercicio 11
# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.