## Exercício 01 - Classificação de suporte técnico
# Entrada #1: Descrição do problema

usuario = str(input("Digite o nome do usuário: "))
tempo_problema = int(input("Há quanto tempo o problema ocorre (dias)? "))

# Entrada #2 - Nível do problema
# Cliente deverá informar qual se encaixa melhor em sua situação
tipo_problema = int(input("Qual o tipo de problema? (4-Indisponibilidade total, 3-Lentidão, 2-Problema que não impede trabalho, 1-Outros) "))

# Saídas:
print(f"O usuário {usuario} reporta um problema em seu PC há {tempo_problema} dias.")

if(tipo_problema == 4):
    nivel_problema = "Crítico"
    print("Problema: Indisponibilidade total // Prioridade: Crítico")
elif(tipo_problema == 3):
    nivel_problema = "Alto"
    print("Problema: Lentidão // Prioridade: Alta")
elif(tipo_problema == 2):
    nivel_problema = "Médio"
    print("Problema: simples, que não impede trabalho // Prioridade: Média")
elif(tipo_problema == 1):
    nivel_problema = "Baixo"
    print("Outros problemas // Prioridade: Baixa")
else:
    print("Os dados do problema parecem errados. Tente novamente.")