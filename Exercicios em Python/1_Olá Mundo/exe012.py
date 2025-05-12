n1 = float(input('Qual valor do produto? R$'))
n2 = int(input('Qual valor do desconto?'))
desconto = n1 * (n2 / 100)
n3 = n1 - desconto
print(
    f'O valor do produto é R${n1:.2f} e o desconto é de {n2}%, totalizando R${n3:.2f}.')

# Exercicio 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
