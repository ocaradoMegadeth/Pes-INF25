numeros = [0] * 15
i = 0

while i < 15:
    numero = int(input("Digite um número de 1 a 75: "))

    if numero < 1 or numero > 75:
        print("Número inválido!")
    else:
        repetido = 0

        for j in range(i):
            if numeros[j] == numero:
                repetido = 1

        if repetido == 1:
            print("Número repetido!")
        else:
            numeros[i] = numero
            i = i + 1


for i in range(14):
    for j in range(14 - i):
        if numeros[j] > numeros[j + 1]:
            aux = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = aux

print("Números em ordem crescente:")
print(numeros)
