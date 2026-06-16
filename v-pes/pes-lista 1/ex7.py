dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o mês do nascimento: "))

signos = [
    ((mes == 3 and dia >= 21) or (mes == 4 and dia <= 19), "Áries"),
    ((mes == 4 and dia >= 20) or (mes == 5 and dia <= 20), "Touro"),
    ((mes == 5 and dia >= 21) or (mes == 6 and dia <= 20), "Gêmeos"),
    ((mes == 6 and dia >= 21) or (mes == 7 and dia <= 22), "Câncer"),
    ((mes == 7 and dia >= 23) or (mes == 8 and dia <= 22), "Leão"),
    ((mes == 8 and dia >= 23) or (mes == 9 and dia <= 22), "Virgem"),
    ((mes == 9 and dia >= 23) or (mes == 10 and dia <= 22), "Libra"),
    ((mes == 10 and dia >= 23) or (mes == 11 and dia <= 21), "Escorpião"),
    ((mes == 11 and dia >= 22) or (mes == 12 and dia <= 21), "Sagitário"),
    ((mes == 12 and dia >= 22) or (mes == 1 and dia <= 19), "Capricórnio"),
    ((mes == 1 and dia >= 20) or (mes == 2 and dia <= 18), "Aquário"),
    ((mes == 2 and dia >= 19) or (mes == 3 and dia <= 20), "Peixes")
]

signo = ""

for condicao, nome in signos:
    if condicao and signo == "":
        signo = nome

if signo:
    print("Seu signo é", signo)
else:
    print("Data inválida!")