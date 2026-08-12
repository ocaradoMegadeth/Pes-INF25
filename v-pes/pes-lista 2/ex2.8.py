divida = 1000


juros = 0.153


meses = int(input("Quantidade de meses: "))


i = 0


while i < meses:
   divida = divida * (1 + juros)
   i = i + 1


print("Dívida final:", divida)


