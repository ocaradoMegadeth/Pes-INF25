total = 0

while True:
    codigo = int(input("Código do produto (0 para sair): "))

    if codigo == 0:
        break

    qtd = int(input("Quantidade: "))

    if codigo == 1:
        nome = "Suco"
        valor = 6.0
    elif codigo == 2:
        nome = "Pão de queijo"
        valor = 3.0
    elif codigo == 3:
        nome = "Pastel"
        valor = 7.0
    elif codigo == 4:
        nome = "Salada de frutas"
        valor = 9.0
    elif codigo == 5:
        nome = "Café com leite"
        valor = 3.5
    elif codigo == 6:
        nome = "Cappuccino"
        valor = 4.5
    elif codigo == 7:
        nome = "Iogurte"
        valor = 6.5
    elif codigo == 8:
        nome = "Água"
        valor = 2.5
    else:
        print("Código inválido")
        continue

    subtotal = valor * qtd

    total += subtotal

    print(f"{nome} - Total: R$ {subtotal:.2f}")


print(f"Total do caixa: R$ {total:.2f}")
