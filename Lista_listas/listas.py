## Inserindo e retirando nomes da lista:

alunos = ["Ana", "Carlos", "João", "Maria"]

for contador in alunos:
    print(contador)

# Para adicionar novos alunos:
AdicionarAlunos = int(input("Quantos alunos deseja adicionar? "))

for n in range(AdicionarAlunos):
    alunos.append(input("Informe o nome do aluno: "))   ### no fim da fila
    print(alunos)

## Cálculos:
print()
notas = [7, 8, 6, 9]
soma = 0

for nota in notas:
    print(f"Nota atual = {nota}")
    soma = soma + nota
    print("A soma atual das notas é: ", soma)