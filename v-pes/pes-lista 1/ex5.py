temperatura = float(input("Digite a temperatura do dia (°C): "))

limites = [10, 20, 25, 30]
mensagens = [
    "Está muito frio! Use roupas quentes.",
    "Frio. Vista-se bem!",
    "Temperatura agradável.",
    "Está ficando quente!",
    "Está muito quente! Fique hidratado."
]

if temperatura < limites[0]:
    print(mensagens[0])
elif temperatura <= limites[1]:
    print(mensagens[1])
elif temperatura <= limites[2]:
    print(mensagens[2])
elif temperatura <= limites[3]:
    print(mensagens[3])
else:
    print(mensagens[4])