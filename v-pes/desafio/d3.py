from deep_translator import GoogleTranslator

while True:     
    print("Tradutor de Português")
    print("----------------------")
    print("1 - Italiano")
    print("2 - Inglês")
    print("3 - Japonês")
    print("4 - Alemão")
    print("5 - Russo")

    opcao = int(input("Escolha o idioma de destino: "))

    if opcao == 1:
        idioma_destino = "it"
        nome_idioma = "Italiano"
    elif opcao == 2:
        idioma_destino = "en"
        nome_idioma = "Inglês"
    elif opcao == 3:
        idioma_destino = "ja"
        nome_idioma = "Japonês"
    elif opcao == 4:
        idioma_destino = "de"
        nome_idioma = "Alemão"
    elif opcao == 5:
        idioma_destino = "ru"
        nome_idioma = "Russo"
    else:
        idioma_destino = None
        nome_idioma = None

    # Só traduz se a opção for válida
    if idioma_destino is not None:
        texto = input("Digite o texto em português: ")
        traducao = GoogleTranslator(source="pt", target=idioma_destino).translate(texto)

        print(f"\nTexto original (pt): {texto}")
        print(f"Tradução ({nome_idioma}): {traducao}")
    else:
        print("Opção inválida.")


        