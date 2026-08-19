def somar(lista):
    return sum(lista)


# Programa principal
numeros = []

for i in range(4):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

resultado = somar(numeros)

print("A soma dos números é:", resultado)
