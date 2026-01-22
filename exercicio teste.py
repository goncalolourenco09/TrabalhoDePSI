notas = []

print("Introduza as notas (0 a 20). Para terminar, digite -1.")

while True:
    nota = float(input("Nota: "))

    if nota == -1:
        break
    elif 0 <= nota <= 20:
        notas.append(nota)
    else:
        print("Nota inválida.")

while True:
    print("\nMENU")
    print("1 - Ver notas")
    print("2 - Ver média")
    print("0 - Sair e ver resultado final")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        if notas:
            print("\nNotas introduzidas:")
            for n in notas:
                print(n)
        else:
            print("Não há notas.")

    elif opcao == 2:
        if notas:
            media = sum(notas) / len(notas)
            print(f"\nMédia das notas: {media:.2f}")
        else:
            print("Não há notas.")

    elif opcao == 0:
        if notas:
            media = sum(notas) / len(notas)
            print(f"\nMédia final: {media:.2f}")
            if media >= 10:
                print("Resultado: APROVADO ")
            else:
                print("Resultado: REPROVADO ")
        else:
            print("Não foram introduzidas notas.")
        break

    else:
        print("Opção inválida.")
