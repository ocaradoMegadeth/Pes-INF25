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
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        nomes = nomes + [nome]
        idades = idades + [idade]
        alturas = alturas + [altura]
        pesos = pesos + [peso]

        print("Cadastro realizado com sucesso!")

    elif opcao == "2":
        nome = input("Nome para excluir: ")

        if nome in nomes:
            novos_nomes = []
            novas_idades = []
            novas_alturas = []
            novos_pesos = []

            i = 0

            for pessoa in nomes:
                if pessoa != nome:
                    novos_nomes = novos_nomes + [pessoa]
                    novas_idades = novas_idades + [idades[i]]
                    novas_alturas = novas_alturas + [alturas[i]]
                    novos_pesos = novos_pesos + [pesos[i]]

                i += 1

            nomes = novos_nomes
            idades = novas_idades
            alturas = novas_alturas
            pesos = novos_pesos

            print("Cadastro excluído!")
        else:
            print("Pessoa não encontrada.")

    elif opcao == "3":
        nome = input("Nome para alterar: ")

        if nome in nomes:
            i = 0

            for pessoa in nomes:
                if pessoa == nome:
                    idades[i] = int(input("Nova idade: "))
                    alturas[i] = float(input("Nova altura: "))
                    pesos[i] = float(input("Novo peso: "))

                    print("Cadastro alterado!")
                    break

                i += 1
        else:
            print("Pessoa não encontrada.")

    elif opcao == "4":
        if nomes == []:
            print("Nenhum cadastro.")
        else:
            for nome, idade, altura, peso in zip(nomes, idades, alturas, pesos):
                print("\nNome:", nome)
                print("Idade:", idade)
                print("Altura:", altura)
                print("Peso:", peso)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")