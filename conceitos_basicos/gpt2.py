num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
soma = num1 + num2
dobro_soma = soma * 2


if soma > 10:
    print(f"{num1} + {num2} = {soma}")
    print(f"{soma} * 2 = {dobro_soma}")
    print("E a soma é maior que 10")
else:
    print(f"{num1} + {num2} = {soma}")
    print(f"{soma} * 2 = {dobro_soma}")
    print("E a soma é menor que 10")
