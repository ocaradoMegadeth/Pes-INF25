def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


# Solicita as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Chama a função
media = calcular_media(nota1, nota2, nota3)

# Exibe o resultado
print("A média aritmética é:", media)
