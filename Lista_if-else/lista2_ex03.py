## Exercício 3: Planos de Internet
# Entradas
cliente = str(input("Digite o nome do cliente: "))
velocidade = int(input("Qual velocidade de Internet contratada (Mbps)? "))

# Saídas
print(f"O cliente {cliente} contratou o plano de {velocidade} Mbps.")

if(velocidade >= 500):
    print("Plano contratado: Ultra")
elif(velocidade >= 200):
    print("Plano contratado: Avançado")
elif(velocidade >= 50):
    print("Plano contratado: Intermediário")
else:
    print("Plano contratado: Básico")