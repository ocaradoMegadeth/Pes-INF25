def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Chama a função
resultado = verificar_par_ou_impar(numero)

# Exibe o resultado
print("O número é", resultado)
