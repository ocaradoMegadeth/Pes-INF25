quantidade = int(input("Quantas notas deseja digitar? "))

notas = []  

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

print("\nNotas digitadas:")
for nota in notas:
    print(nota)