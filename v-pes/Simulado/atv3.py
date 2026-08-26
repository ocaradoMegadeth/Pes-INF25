preco = int(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))

total = preco * quantidade

if total >= 100:
    desconto = total * 0.10
    valor_final = total - desconto
else:
    valor_final = total

print("Valor a pagar: R$", valor_final)
