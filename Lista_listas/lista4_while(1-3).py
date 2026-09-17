# Atividade 1: Contador

numero = 1
while numero <= 10:
    print(numero)
    numero = numero + 1
print()

# Atividade 2: Contador (pares)

num_par = 2
while num_par <= 20:
    print(num_par)
    num_par = num_par + 2

# Atividade 3: Cadastro de alunos

qtd_alunos = int(input("Quantos alunos deseja cadastrar? "))
contador = 1

while contador <= qtd_alunos:
    aluno = str(input("Qual o nome do aluno? "))
    print("Aluno cadastrado: ", aluno)
    qtd_alunos = qtd_alunos - 1