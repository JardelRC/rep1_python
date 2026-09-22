## Atividade 1: notas de estudantes

notas = []
qtd_notas = 5

for nota in range(qtd_notas):
    notas.append(float(input("Insira a nota do aluno (0.0-10.0): ")))
    print(notas)

maior = max(notas)
print("A maior nota é: ", maior)
menor = min(notas)
print("A menor nota é: ", menor)
print()

## Atividade 2: Cadastro de produtos

produtos = []
qtd_produtos = 6

for produto in range(qtd_produtos):
    produtos.append(str(input("Insira o nome do produto: ")))
    print("Produtos cadastrados: ", produtos)

pesquisa = str(input("Digite um nome de um produto: "))
if pesquisa in produtos:
    print("Produto encontrado!")
else:
    print("Produto não encontrado...")
