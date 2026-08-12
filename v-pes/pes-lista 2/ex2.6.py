n = int(input("Digite o número: "))


inicio = int(input("Digite o início da tabuada: "))


fim = int(input("Digite o fim da tabuada: "))


print("Tabuada do número", n)


i = inicio


while i <= fim:
   print(n, "x", i, "=", n * i)
   i = i + 1
