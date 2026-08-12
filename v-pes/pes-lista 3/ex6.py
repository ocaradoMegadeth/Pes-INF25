# Cadastro de medidas corpóreas

codigos = [0] * 10
nomes = [""] * 10
idades = [0] * 10
alturas = [0] * 10
pesos = [0] * 10

proximo_codigo = 1
quantidade = 0

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Excluir por código")
    print("3 - Alterar")
    print("4 - Listar")
    print("5 - Pesquisar por nome")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if quantidade < 10:
            codigos[quantidade] = proximo_codigo

            print("Código da pessoa:", proximo_codigo)

            nomes[quantidade] = input("Nome: ")
            idades[quantidade] = int(input("Idade: "))
            alturas[quantidade] = float(input("Altura: "))
            pesos[quantidade] = float(input("Peso: "))

            proximo_codigo += 1
            quantidade += 1

            print("Cadastro realizado com sucesso!")
        else:
            print("Não há espaço para novos cadastros.")

    elif opcao == "2":
        codigo = int(input("Código para excluir: "))

        i = 0

        while i < quantidade:
            if codigos[i] == codigo:
                while i < quantidade - 1:
                    codigos[i] = codigos[i + 1]
                    nomes[i] = nomes[i + 1]
                    idades[i] = idades[i + 1]
                    alturas[i] = alturas[i + 1]
                    pesos[i] = pesos[i + 1]

                    i += 1

                quantidade -= 1
                print("Cadastro excluído!")
                break

            i += 1
        else:
            print("Código não encontrado.")

    elif opcao == "3":
        nome = input("Nome para alterar: ")

        i = 0

        while i < quantidade:
            if nomes[i] == nome:
                idades[i] = int(input("Nova idade: "))
                alturas[i] = float(input("Nova altura: "))
                pesos[i] = float(input("Novo peso: "))

                print("Cadastro alterado!")
                break

            i += 1
        else:
            print("Pessoa não encontrada.")

    elif opcao == "4":
        if quantidade == 0:
            print("Nenhum cadastro.")
        else:
            i = 0

            while i < quantidade:
                print("\nCódigo:", codigos[i])
                print("Nome:", nomes[i])
                print("Idade:", idades[i])
                print("Altura:", alturas[i])
                print("Peso:", pesos[i])

                i += 1

    elif opcao == "5":
        nome = input("Nome para pesquisar: ")

        i = 0

        while i < quantidade:
            if nomes[i] == nome:
                print("\nCadastro encontrado:")
                print("Código:", codigos[i])
                print("Nome:", nomes[i])
                print("Idade:", idades[i])
                print("Altura:", alturas[i])
                print("Peso:", pesos[i])
                break

            i += 1
        else:
            print("Pessoa não encontrada.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")