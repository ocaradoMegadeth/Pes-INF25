def esta_vazia(lista):
    return len(lista) == 0


def maior(lista):
    if esta_vazia(lista):
        return -1

    maior_valor = lista[0]
    for valor in lista:
        if valor > maior_valor:
            maior_valor = valor

    return maior_valor


def menor(lista):
    if esta_vazia(lista):
        return -1

    menor_valor = lista[0]
    for valor in lista:
        if valor < menor_valor:
            menor_valor = valor

    return menor_valor


def media(lista):
    if esta_vazia(lista):
        return -1

    soma = 0
    for valor in lista:
        soma += valor

    return soma / len(lista)


# Programa principal
lista_vazia = []
lista = [10, 5, 20, 8, 15]

print("Lista vazia:")
print("Está vazia?", esta_vazia(lista_vazia))
print("Maior valor:", maior(lista_vazia))
print("Menor valor:", menor(lista_vazia))
print("Valor médio:", media(lista_vazia))

print("\nLista com elementos:", lista)
print("Está vazia?", esta_vazia(lista))
print("Maior valor:", maior(lista))
print("Menor valor:", menor(lista))
print("Valor médio:", media(lista))
