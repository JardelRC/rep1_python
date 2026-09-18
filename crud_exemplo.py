## Passo 1: Create (criar novo registro)

biblioteca = []

codigo = str(input("Digite o código do livro: "))
titulo = str(input("Qual o título do livro? "))
autor = str(input("Quem é o autor? "))
ano = int(input("Qual o ano de publicação? "))

livro = [codigo, titulo, autor, ano]
biblioteca.append(livro)

print("Livro cadastrado!\n")
print(biblioteca)

## Passo 2: Read (ler os dados)
# Listando os itens:
for livro in biblioteca:
    print("Código:", livro[0])
    print("Título:", livro[1])
    print("Autor:", livro[2])
    print("Ano:", livro[3])

# Pesquisa pelo código:
busca_codigo = input("Digite o código: ")

for livro in biblioteca:
    if livro[0] == busca_codigo:
        print("Livro encontrado!")
        print("Título:", livro[1])
        print("Autor:", livro[2])
        print("Ano:", livro[3])
    else:
        print("Livro não encontrado. Tente novamente.")

## Passo 3: Update (alterar um livro):
busca_codigo = input("Digite o código: ")

for livro in biblioteca:
    if livro[0] == busca_codigo:
        livro[1] = input("Novo título: ")
        livro[2] = input("Novo autor: ")
        livro[3] = input("Novo ano: ")

        print("Livro atualizado!")
print(biblioteca)