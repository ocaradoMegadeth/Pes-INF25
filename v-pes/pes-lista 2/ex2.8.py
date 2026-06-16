divida = 1000

juros = 0.153

meses = int(input("Quantidade de meses: "))

for i in range(meses):
    divida = divida * (1 + juros)

print(f"Dívida final: R$ {divida:.2f}")
