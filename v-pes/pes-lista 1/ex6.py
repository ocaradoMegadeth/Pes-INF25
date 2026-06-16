
jogadas = {"pedra": 0, "papel": 1, "tesoura": 2}

jogador1 = input("Jogador 1 (pedra, papel ou tesoura): ").lower()
jogador2 = input("Jogador 2 (pedra, papel ou tesoura): ").lower()

if jogador1 not in jogadas or jogador2 not in jogadas:
    print("Entrada inválida!")
else:
    p1 = jogadas[jogador1]
    p2 = jogadas[jogador2]

    if p1 == p2:
        print("Empate!")
    elif (p1 - p2) % 3 == 1:
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")