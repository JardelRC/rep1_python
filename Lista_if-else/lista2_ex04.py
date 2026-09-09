## Exercício 4: Acesso a laboratório
# Entradas:
aluno = str(input("Digite o nome do/a aluno/a: "))
idade = int(input("Qual a idade dele/a? "))
cadastro = str(input("O/A aluno/a está cadastrado/a? (S/N) "))

# Saídas
if(cadastro == "N"):
    print(f"O/A aluno/a {aluno} não possui cadastro no laboratório. Logo, acesso não permitido.")
else:
    if(idade >= 18):
        print(f"O/A aluno/a {aluno} tem acesso permitido a esse laboratório.")
    elif(idade >= 14):
        print(f"O/A aluno/a {aluno} tem acesso permitido a esse laboratório.")
    else:
        print(f"O/A aluno/a {aluno} tem acesso permitido a esse laboratório, apenas com a presença de um acompanhante.")