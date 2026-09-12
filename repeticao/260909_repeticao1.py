## Estruturas de repetição:

####################################################
# Atividade 1: Para contagem regressiva: começa em 10, termina em 0 e diminui 1 a cada laço
for numero in range(10, 0, -1):
    print(numero)
print("Fim da contagem")

####################################################
# Atividade 2: Para verificar uma divisão exata (resto = 0):
for numero in range(1, 31):
    if numero % 3 == 0:
        print(numero)