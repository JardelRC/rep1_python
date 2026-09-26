import datetime
x = datetime.datetime.now()
print(f"{x.day}/{x.month}/{x.year}")
ano_max = x.year

import funcoes

biblioteca = []

def cadastro_livro():
    codigo = str(input("Insira o código do livro: "))
    if codigo == "":
        print("Código inválido, tente novamente.")
        return

    titulo = str(input("Digite o título do livro: "))
    if titulo == "":
        print("Título inválido, tente novamente.")
        return

    autor = str(input("Qual o autor? "))
    if autor == "":
        print("Autor inválido, tente novamente.")
        return

    ano = int(input("Qual o ano de publicação? "))
    if ano > 2026:
        print("Ano inválido, tente novamente")
        return

    else:
        livro = [codigo, titulo, autor, ano]
        biblioteca.append(livro)
        print("Livro cadastrado!")

def listar_livros():
    print("CÓDIGO // TÍTULO // AUTOR // ANO")
    for livro in biblioteca:            
        print(f"{livro[0]} // {livro[1]} // {livro[2]} // {livro[3]}")
    

#########################################################################
##### Menu principal:
while True:
    funcoes.saudacao()
    print("##### SISTEMA DE BIBLIOTECA #####")
    print("1 - Cadastrar livros")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Alterar livro")
    print("5 - Excluir livro")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")
    print()

    if opcao == "1":
        cadastro_livro()
    elif opcao == "2":
        listar_livros()


