# Cadastro de placas de automóveis (até 15 veículos)

placas = [None] * 15

while True:
    print("\n===== ESTACIONAMENTO =====")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Verifica se existe espaço disponível
        if None in placas:
            placa = input("Digite a placa do veículo: ").upper()

            if placa in placas:
                print("Essa placa já está cadastrada.")
            else:
                indice = placas.index(None)
                placas[indice] = placa
                print("Placa cadastrada com sucesso!")
        else:
            print("Não há espaço disponível para novos cadastros.")

    elif opcao == "2":
        placa = input("Digite a placa que deseja excluir: ").upper()

        if placa in placas:
            indice = placas.index(placa)
            placas[indice] = None
            print("Placa excluída com sucesso!")
        else:
            print("Placa não encontrada.")

    elif opcao == "3":
        print("\nPlacas cadastradas:")
        encontrou = False

        for placa in placas:
            if placa is not None:
                print(placa)
                encontrou = True

        if not encontrou:
            print("Nenhuma placa cadastrada.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")