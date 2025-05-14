peso = float(input("Insira seu peso:"))

indetificador = input("(K)g ou (L)ibras: ")

if indetificador.upper() == "K":
    print("-" * 38)
    print("")
    print(f"{peso}Kg é igual a {peso * 2.20462} Libras")
    print("")
    print("-" * 38)
elif indetificador.upper() == "L":
    print("-" * 38)
    print("")
    print(f"{peso}Libras é igual a {peso / 2.20462}Kg")
    print("")
    print("-" * 38)

else:

    print("Valor inválido, insira K ou L")
    exit()


# Exercicio 1
# Insira um peso e diga ele convetido de Kg para libras e vice-versa
