notas = []     
quantidade = 0  

while True:
    print("\nNotas")
    print("-----")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Calcular média")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        nota = float(input("Digite a nota a cadastrar: "))
        notas.append(nota)
        quantidade += 1
        print(f"Nota {nota} cadastrada com sucesso!")

    elif opcao == 2:
        if quantidade == 0:
            print("A lista de notas está vazia. Não há nada para excluir.")
        else:
            print("\nLista de notas:")
            i = 0
            for nota in notas:
                print(f"[{i}] Nota: {nota}")
                i += 1
            indice = int(input("Digite o índice da nota a excluir: "))
            if 0 <= indice < quantidade:
                nota_removida = notas.pop(indice)
                quantidade -= 1
                print(f"Nota {nota_removida} removida com sucesso!")
            else:
                print("Índice inválido.")

    elif opcao == 3:
        if quantidade == 0:
            print("A lista de notas está vazia.")
        else:
            print("\nLista de notas cadastradas:")
            i = 0
            for nota in notas:
                print(f"[{i}] Nota: {nota}")
                i += 1

    elif opcao == 4:
        if quantidade == 0:
            print("A lista de notas está vazia. Não é possível calcular a média.")
        else:
            soma = 0
            for nota in notas:
                soma += nota
            media = soma / quantidade
            print(f"\nMédia do aluno: {media:.2f}")
            if media >= 6:
                print("Situação: Aprovado")
            else:
                print("Situação: Reprovado")

    elif opcao == 0:
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")