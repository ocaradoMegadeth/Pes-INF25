qtd = int(input("Quantidade de notas: "))

soma = 0

for i in range(qtd):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

media = soma / qtd

print(f"Média: {media:.2f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
