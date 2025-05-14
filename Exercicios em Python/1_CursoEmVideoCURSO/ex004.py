valor = input('Digite oque vier em mente: ')

print(f"Oque você digitou que foi {valor} é do tipo {type(valor)}")
print(f"é Numeros e Letra?: {valor.isalnum()}")
print(f"é apenas Letras?: {valor.isalpha()}")
print(f"é apenas Digitos?: {valor.isdigit()}")
print(f"é Apenas Decimal: {valor.isdecimal()}")
print(f"è Somente Espaço?: {valor.isspace()}")
print(f"é Printable: {valor.isprintable()}")
print(f"é Identifier: {valor.isidentifier()}")

# Exercicio 4
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.