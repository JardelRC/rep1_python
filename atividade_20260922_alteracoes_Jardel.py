### Atividade não-presencial - 22/09/2026
### Arquivo com alterações

livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Sair")
    print("6 - Quantidade de livros")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])

        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        for contador in livros:
            print("Título:", contador[0])
            print("Autor:", contador[1])

    elif opcao == "3":
    ### No código original, não havia resposta para título errado ou vazio.
    ### A correção é feita com uma condicional if/else e booleanos (Explicação na Questão 10):

        pesquisa = input("Digite o título que deseja pesquisar: ")
        encontrado = False

        for contador in livros:
            if contador[0] == pesquisa:
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
                encontrado = True
                break
            else:
                print("Título inválido ou inexistente. Tente novamente.")

    elif opcao == "4":
    ### Assim como na opção anterior, não havia resposta para título errado ou vazio.
    ### A correção é feita com uma condicional if/else e booleanos:

        pesquisa = input("Digite o título que deseja excluir: ")
        encontrado = False

        for contador in livros:
            if contador[0] == pesquisa:
                livros.remove(contador)
                print("Livro excluído!")
                encontrado = True
                break
            else:
                print("Título inválido ou inexistente. Tente novamente.")

    elif opcao == "5":

        print("Programa encerrado.")
        break

    ### Opção adicionada: Mostrar quantidade de livros (Questão 08)
    elif opcao == "6":
        print(f"Livros cadastrados: {len(livros)}")

    else:

        print("Opção inválida!")