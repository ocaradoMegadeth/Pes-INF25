# Solicita ao usuário a escolha de uma carro
poder = input("Escolha um carro (Mazda RX7, Lancia Delta S4 ou Nissan GTR): ")

# Verifica a escolha e exibe seu gosto
if poder == "Mazda RX7":
	print("Você tem um bom gosto pra carro!")
elif poder == "Lancia Delta S4":
	print("Você gosta de veiculos com historias na pista mesmo não sendo um carro vencendor!")
elif poder == "Nissan GTR":
	print("se você gosta desse modelo/carro você gosta só por faminha e não entende sobre carros!")
else:
	print("Opção inválida!")

# Solicita ao usuário a escolha do superpoder
poder = input("Escolha um superpoder (força, velocidade ou voo): ")

# Verifica a escolha e exibe o super-herói correspondente
if poder == "força":
	print("Você seria o Hulk!")
elif poder == "velocidade":
	print("Você seria o Flash!")
elif poder == "voo":
	print("Você seria o Superman!")
else:
	print("Opção inválida!")
