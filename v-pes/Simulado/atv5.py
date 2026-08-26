num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

while True:
    print("\n=== CALCULADORA ===")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        resultado = num1 + num2
        print(f"Resultado: {resultado}")

    elif opcao == 2:
        resultado = num1 - num2
        print(f"Resultado: {resultado}")

    elif opcao == 3:
        resultado = num1 * num2
        print(f"Resultado: {resultado}")

    elif opcao == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Erro: não é possível dividir por zero.")

    elif opcao == 0:
        print("Calculadora encerrada.")
        break

    else:
        print("Erro: opção inválida.")
