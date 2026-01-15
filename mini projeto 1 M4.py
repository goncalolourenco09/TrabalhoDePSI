contador = 0
continuar = "S"

while continuar.upper() == "S":
    frase = input("\nIntroduza uma frase: ")

    palavras = frase.split()
    sigla = ""

    for palavra in palavras:
        # Ignorar palavras pequenas comuns
        if palavra.lower() not in ["de", "do", "da", "dos", "das", "e"]:
            sigla += palavra[0].upper()

    print("Sigla gerada:", sigla)

    contador += 1
    print("Total de siglas criadas:", contador)

    continuar = input("Deseja criar outra sigla? (S/N): ")

print("\nPrograma terminado.")
 