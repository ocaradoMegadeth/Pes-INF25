while True:

    print("\nMenu")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("0 - Sair")

    op = int(input("Digite a opção: "))

    if op == 0:
        break

    if op < 1 or op > 4:
        print("Opção inválida")
        continue

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if op == 1:
        print("Resultado:", a + b)
    elif op == 2:
        print("Resultado:", a - b)
    elif op == 3:
        if b == 0:
            print("Erro: divisão por zero")
        else:
            print("Resultado:", a / b)
    elif op == 4:
        print("Resultado:", a * b)
