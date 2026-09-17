# Atividade 5: Idade

idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 120:
    if idade < 0:
        print("Idade inválida. Tente novamente.")
    elif idade > 120:
        print("Idade inválida. Tente novamente.")
    idade = int(input("Digite sua idade novamente: "))
print("Sua idade: ", idade)