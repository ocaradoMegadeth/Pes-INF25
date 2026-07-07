amigos = []  

while True:
    print("\nAmigos Próximos")
    print("---------------")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")

    opcao = int(input("-Opção: "))

    if opcao == 1:
        nome = input("Digite o nome do amigo a cadastrar: ")
        amigos.append(nome)
        print(f"'{nome}' foi cadastrado com sucesso!")

    elif opcao == 2:
        if len(amigos) == 0:
            print("A lista de amigos está vazia. Não há nada para excluir.")
        else:
            nome = input("Digite o nome do amigo a excluir: ")
            if nome in amigos:
                amigos.remove(nome)
                print(f"'{nome}' foi removido com sucesso!")
            else:
                print(f"'{nome}' não foi encontrado na lista.")

    elif opcao == 3:
        if len(amigos) == 0:
            print("A lista de amigos está vazia.")
        else:
            print("\nLista de amigos próximos:")
            for amigo in amigos:
                print(amigo)

    elif opcao == 0:
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")