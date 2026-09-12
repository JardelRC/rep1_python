####################################################
# Atividade 3: Média de 4 notas
soma = 0

for numero in range(1, 5):
    nota = float(input("Digite uma nota (0,0-10,0): "))
    soma = soma + nota

media = soma / 4
print("A média é:", media)

####################################################
# Atividade 4: Estoque de produtos
for numero in range(1, 6):
    produto = str(input("Digite o nome de um produto: "))
    print(f"{produto} cadastrado no estoque.")

print("Produtos cadastrados.")