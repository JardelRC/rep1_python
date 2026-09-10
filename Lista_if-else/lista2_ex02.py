## Exercício 2: Controle de estoque
# Entradas:
produto = str(input("Digite o nome do produto:"))
qtd = int(input("Quantos desse produto ainda estão no estoque? "))

# Saídas:
print(f"O produto {produto} está com estoque de {qtd} unidades. Logo,")
if(qtd > 20):
    print("Estoque normal")
elif(qtd >= 6):
    print("Estoque baixo")
elif(qtd >= 1):
    print("Estoque crítico")
else:
    print("Produto esgotado")