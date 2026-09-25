biblioteca = []

import datetime
x = datetime.datetime.now()
print(f"{x.day}/{x.month}/{x.year}")
ano_max = x.year

while True:
    print("##### SISTEMA DE BIBLIOTECA #####")
    print("1 - Cadastrar livros")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Alterar livro")
    print("5 - Excluir livro")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))
    print()

### Opção 1: Cadastro
    if opcao == 1:
        print("### Opção 1: Cadastro de livros ###")
        qtd_livros = int(input("Quantos livros deseja cadastrar? "))
        for numero in range(qtd_livros):
            print(f"### Livro #{numero}")
            codigo = str(input("Digite o código do livro: "))
            if codigo == "":
                print("Código inválido. Tente novamente")
            else:
                titulo = str(input("Qual o título do livro? "))
                if titulo == "":
                    print("Título inválido. Tente novamente.")
                else:
                    autor = str(input("Quem é o autor? "))
                    if autor == "":
                        print("Autor desconhecido. Tente novamente.")
                    else:
                        ano = int(input("Qual o ano de publicação? "))
                        if ano > ano_max:
                            print("Ano inválido. Tente novamente.")
                        else:
                            livro = [codigo, titulo, autor, ano]
                            biblioteca.append(livro)
                            print("Livro cadastrado!")
        print()


### Opção 2: Lista de livros
    elif opcao == 2:
        print("### Opção 2: Lista de livros ###")
        print("Esses são os livros cadastrados:")
        print("CÓDIGO // TÍTULO // AUTOR // ANO")
        for livro in biblioteca:            
            print(f"{livro[0]} // {livro[1]} // {livro[2]} // {livro[3]}")
        print()


### Opção 3: Pesquisar livros
    elif opcao == 3:
        print("### Opção 3: Pesquisar livros ###")
        codigo = str(input("Digite o código do livro: "))
        for livro in biblioteca:
            if codigo == livro[0]:
                print("Livro encontrado!")
                print("Título:", livro[1])
                print("Autor:", livro[2])
                print("Ano:", livro[3])
            else:
                print("Livro não encontrado ou erro do código digitado. Tente novamente.")

        print()

### Opção 4: Alterar dados
    elif opcao == 4:
        codigo = str(input("Digite o código do livro: "))
        for livro in biblioteca:
            if codigo == livro[0]:
                livro[1] = input("Novo título: ")
                livro[2] = input("Novo autor: ")
                livro[3] = int(input("Novo ano: "))
                print("Livro atualizado!")
            else:
                print("Livro não encontrado ou erro do código digitado. Tente novamente.")
        print()

### Opção 5: Excluir livro
    elif opcao == 5:
        codigo = str(input("Digite o código do livro: "))
        if codigo == "":
            print("Livro não encontrado ou erro do código digitado. Tente novamente.")
        else:
            for livro in biblioteca:
                if livro[0] == codigo:
                    biblioteca.remove(livro)
                    print("Livro excluído.")

### Opção 6: Sair
    elif opcao == 6:
        print("Você saiu da operação. Reinicie para novas operações.")
        break

### Opções erradas:
    else:
        print("Opção errada. Reinicie a operação.")
        print()