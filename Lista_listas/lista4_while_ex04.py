# Atividade 4: Menu
opcao = 0

while opcao != 3:
    print()
    print("Opção 1: Cadastro de livros")
    print("Opção 2: Listar livros cadastrados")
    print("Opção 3: Sair")
    print()
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print("Opção 1: Cadastro de livros")
    elif opcao == 2:
        print("Opção 2: Listar livros cadastrados")
    elif opcao == 3:
        print("Você saiu do programa. Reinicie para uma nova operação")
    else:
        print("Opção inválida.")

# Atividade 5: Idade

idade = 0

while idade < 0 or idade > 120:
    idade = int(input("Insira sua idade:"))
    if idade < 0 or idade > 120:
        print("Idade inválida. Tente novamente.")
    else:
        print("Sua idade: ", idade)