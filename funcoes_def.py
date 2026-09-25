def saudacao():
    print("Olá!")

saudacao()

def add(a, b):
    result = a + b
    return result

a = int(input("Insira um número: "))
b = int(input("insira outro número: "))
add(a, b)

def saudacao(nome, dia):
    print(f"Olá, {nome}, hoje é {dia}.")

nome = input("Digite seu nome: ")
dia = input("Digite a data de hoje: ")

saudacao(nome, dia)
