idades = []


i = 1


while i <= 6:
   idade = int(input("Digite a idade do aluno: "))
   idades.append(idade)
   i = i + 1


print("Idades maiores ou iguais a 16:")


i = 0


while i < 6:
   if idades[i] >= 16:
       print(idades[i])
   i = i + 1


