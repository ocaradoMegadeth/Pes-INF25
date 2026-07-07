bairros = ["Centro"] 
for i in range(5):
    bairro = input(f"Digite o nome do bairro {i + 1}: ")
    bairros.append(bairro)

print("\nBairros cadastrados:")
for bairro in bairros:
    print(bairro)