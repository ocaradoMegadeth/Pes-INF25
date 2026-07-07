import subprocess

nome = input("Digite o nome que deve ser usado no Git: ")
email = input("Digite o e-mail que deve ser usado no Git: ")

subprocess.run(["git", "config", "--global", "user.name", nome])

subprocess.run(["git", "config", "--global", "user.email", email])

print("\nConfiguração aplicada com sucesso!")

nome_configurado = subprocess.run(
    ["git", "config", "--global", "user.name"],
    capture_output=True, text=True
)
email_configurado = subprocess.run(
    ["git", "config", "--global", "user.email"],
    capture_output=True, text=True
)

print(f"user.name  = {nome_configurado.stdout.strip()}")
print(f"user.email = {email_configurado.stdout.strip()}")