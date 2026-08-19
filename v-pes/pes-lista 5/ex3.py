def volume(altura, raio):
    return 3.14 * raio * raio * altura

altura = float(input("Digite a altura: "))
raio = float(input("Digite o raio: "))

resultado = volume(altura, raio)

print("O volume é:", resultado)
