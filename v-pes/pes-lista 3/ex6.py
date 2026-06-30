# Cadastro de medidas corpóreas

codigos = []
nomes = []
idades = []
alturas = []
pesos = []

proximo_codigo = 1

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
        codigos.append(proximo_codigo)
        print("Código da pessoa:", proximo_codigo)
        proximo_codigo += 1

        nomes.append(input("Nome: "))
        idades.append(int(input("Idade: ")))
        alturas.append(float(input("Altura: ")))
        pesos.append(float(input("Peso: ")))

        print("Cadastro realizado com sucesso!")

    elif opcao == "2":
        codigo = int(input("Código para excluir: "))

        if codigo in codigos:
            i = codigos.index(codigo)

            codigos.pop(i)
            nomes.pop(i)
            idades.pop(i)
            alturas.pop(i)
            pesos.pop(i)

            print("Cadastro excluído!")
        else:
            print("Código não encontrado.")

    elif opcao == "3":
        nome = input("Nome para alterar: ")

        if nome in nomes:
            i = nomes.index(nome)

            idades[i] = int(input("Nova idade: "))
            alturas[i] = float(input("Nova altura: "))
            pesos[i] = float(input("Novo peso: "))

            print("Cadastro alterado!")
        else:
            print("Pessoa não encontrada.")

    elif opcao == "4":
        if nomes == []:
            print("Nenhum cadastro.")
        else:
            i = 0
            while True:
                try:
                    print("\nCódigo:", codigos[i])
                    print("Nome:", nomes[i])
                    print("Idade:", idades[i])
                    print("Altura:", alturas[i])
                    print("Peso:", pesos[i])
                    i += 1
                except IndexError:
                    break

    elif opcao == "5":
        nome = input("Nome para pesquisar: ")

        if nome in nomes:
            i = nomes.index(nome)

            print("\nCadastro encontrado:")
            print("Código:", codigos[i])
            print("Nome:", nomes[i])
            print("Idade:", idades[i])
            print("Altura:", alturas[i])
            print("Peso:", pesos[i])
        else:
            print("Pessoa não encontrada.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")