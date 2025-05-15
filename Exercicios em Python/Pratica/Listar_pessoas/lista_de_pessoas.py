def coletar_dados():
    lista = []

    while True:
        nome = input("Insira um nome: ")
        idade = input("Insira a idade: ")
        lista.append([nome, idade])

        while True:

            continuar = input("Deseja Continuar? (S/N): ")

            if continuar.upper() in ["S", "N"]:
                break
            print("Opção Inválida. Digite S para continuar e N para sair.")
        if continuar.upper() == "N":
            break
    return lista


def exibir_lista(lista):
    print("\n --- Lista de pessoas cadastradas ---")
    for pessoa in lista:
        print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}")


def main():
    iniciar = input("Deseja começar? (S/N): ")

    if iniciar.upper() == "S":
        pessoas = coletar_dados()
        exibir_lista(pessoas)
    elif iniciar.upper() == "N":
        print("Programa Encerrado.")
    else:
        print("Opção inválida. Programa sera encerrado")


if __name__ == "__main__":
    main()
