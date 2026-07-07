quantidade = int(input("Quantas cidades deseja cadastrar? "))

cidades = []  

for i in range(quantidade):
    cidade = input(f"Digite o nome da cidade {i + 1}: ")
    cidades.append(cidade)

print("\nCidades cadastradas:")
for cidade in cidades:
    print(cidade)

remover = input("\nDigite o nome da cidade que deseja remover: ")

if remover in cidades:
    cidades.remove(remover)
    print(f"\nCidade '{remover}' removida com sucesso!")
else:
    print(f"\nA cidade '{remover}' não foi encontrada na lista.")

print("\nLista de cidades atualizada:")
for cidade in cidades:
    print(cidade)