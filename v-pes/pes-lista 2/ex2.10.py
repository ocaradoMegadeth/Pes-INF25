soma = 0

cont = 0

while True:
    n = int(input("Digite um número (0 para parar): "))

    if n == 0:
        break

    soma += n

    cont += 1

if cont > 0:

    media = soma / cont

    print("Quantidade:", cont)
    print("Soma:", soma)
    print("Média:", media)
else:
    print("Nenhum número foi digitado.")
