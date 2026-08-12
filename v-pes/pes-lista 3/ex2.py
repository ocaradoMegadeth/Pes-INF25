notas = []


i = 1
soma = 0


while i <= 4:
   nota = float(input("Digite a nota: "))
   notas.append(nota)
   soma = soma + nota
   i = i + 1


media = soma / 4


print("Média:", media)


if media >= 7:
   print("Situação: Aprovado(a)")
else:
   print("Situação: Reprovado(a)")
