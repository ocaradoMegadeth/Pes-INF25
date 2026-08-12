produtos = ["-1"] * 10

while True:
    print("\nMenu")
    print("----")
    print("1 - Cadastrar")
    print("2 - Listar todos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = input("Digite o código do produto: ")

        if codigo == "-1":
            print("Erro: código -1 não é permitido.")
        else:
            cadastrado = False
            i = 0

            while i < 10:
                if produtos[i] == "-1":
                    produtos[i] = codigo
                    print("Código cadastrado com sucesso!")
                    cadastrado = True
                    break
                i += 1

            if not cadastrado:
                print("Falha: não há espaço para cadastrar mais produtos.")

    elif opcao == "2":
        print("\nProdutos cadastrados:")
        tem_dados = False

        for codigo in produtos:
            if codigo != "-1":
                print(codigo)
                tem_dados = True

        if not tem_dados:
            print("Nenhum produto cadastrado.")

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")