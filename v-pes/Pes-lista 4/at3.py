quantidade = int(input("Quantas notas deseja digitar? "))

notas = []  

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

print("\nExibição com while:")
i = 0
while i < len(notas):
    print(f"Nota: {notas[i]}")
    i += 1

print("\nExibição com for:")
for nota in notas:
    print(f"Nota: {nota}")