# Cadastro de medidas corpóreas

nomes = []
idades = []
alturas = []
pesos = []

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Alterar")
    print("4 - Listar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nomes.append(input("Nome: "))
        idades.append(int(input("Idade: ")))
        alturas.append(float(input("Altura: ")))
        pesos.append(float(input("Peso: ")))
        print("Cadastro realizado com sucesso!")

    elif opcao == "2":
        nome = input("Nome para excluir: ")

        if nome in nomes:
            i = nomes.index(nome)
            nomes.pop(i)
            idades.pop(i)
            alturas.pop(i)
            pesos.pop(i)
            print("Cadastro excluído!")
        else:
            print("Pessoa não encontrada.")

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
                    print("\nNome:", nomes[i])
                    print("Idade:", idades[i])
                    print("Altura:", alturas[i])
                    print("Peso:", pesos[i])
                    i += 1
                except IndexError:
                    break

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")