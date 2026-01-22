
nomes = []

while True:
    print("\n=== Sistema de Gestão de Nomes ===")
    print("1 - Adicionar nome")
    print("2 - Remover nome")
    print("3 - Listar todos os nomes")
    print("4 - Procurar um nome")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome a adicionar: ")
        nomes.append(nome)
        print("Nome adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome a remover: ")
        if nome in nomes:
            nomes.remove(nome)
            print("Nome removido com sucesso!")
        else:
            print("Nome não encontrado.")

    elif opcao == "3":
        if len(nomes) == 0:
            print("A lista está vazia.")
        else:
            print("Lista de nomes:")
            for n in nomes:
                print("-", n)

    elif opcao == "4":
        nome = input("Digite o nome a procurar: ")
        if nome in nomes:
            print("O nome existe na lista.")
        else:
            print("O nome não existe na lista.")

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
