deposito = float(input("Valor mensal depositado: "))

saldo = 0

juros = 0.005

for mes in range(1, 25):

    saldo = saldo * (1 + juros) + deposito

    print(f"Mês {mes}: R$ {saldo:.2f}")
