## Declaração de variáveis, conversão e entrada de dados
## pelo usuário

nome = input("Informe seu nome:")
idade = int(input("Informe sua idade:"))
altura = float(input("Informe sua altura:"))

## Implementação 1
print("O nome informado foi: ", nome)
print("A idade informada foi: ", idade)
print("A altura informada foi: ", altura)

## Implementação 2
print(f"O nome informado foi: {nome}")
print(f"A idade informada foi: {idade}")
print(f"A altura informada foi: {altura}")

## Condicionais:
if idade >= 18:
    print("Voto obrigatório")
elif idade >= 16:
    print("Voto facultativo")
else:
    print("Voto não obrigatório")