def saudacao():
    print("Bem-vindo!")

def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    biblioteca.append([titulo, autor])

def listar_livros():
    for contador in biblioteca:
        print(contador[0], "-", contador[1])

### while True:
    ### print("\n1 - Cadastrar")
    ### print("2 - Listar")
    ### print("0 - Sair")
    ### opcao = input("Escolha: ")

### if opcao == "1":
    ### cadastrar_livro()
### elif opcao == "2":
    ### listar_livros()
### elif opcao == "0":
    ### break
### else:
    ### print("Opção inválida")
