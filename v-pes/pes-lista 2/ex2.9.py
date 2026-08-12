qtd = int(input("Quantidade de notas: "))


soma = 0
i = 0


while i < qtd:
   nota = float(input("Digite a nota: "))
   soma = soma + nota
   i = i + 1


media = soma / qtd


print("Média:", media)


if media >= 6:
   print("Aprovado")
else:
   print("Reprovado")
