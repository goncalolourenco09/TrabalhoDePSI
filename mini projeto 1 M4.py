contador = 0
continuar = "Sim"

while continuar.upper() == "Sim":
    frase = input("\nIntroduza uma frase: ")

    palavras = frase.split()
    sigla = ""

    for palavra in palavras:
        # Ignorar palavras pequenas comuns
        if palavra.lower() not in ["de", "do", "da", "e"]:
            sigla += palavra[0].upper()

    print("Sigla gerada:", sigla)

    contador += 1
    print("Total de siglas criadas:", contador)

    continuar = input("Deseja criar outra frase? (Sim/Não): ")

print("\nPrograma terminado.")

 
