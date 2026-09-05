## Exercício 15: Reajuste de salário

salario = float(input("Digite seu salário atual: "))
aumento = float(input("Qual será o aumento em %? "))

novo_sal = salario + salario * aumento / 100

print("O novo salário será: ", novo_sal)

#################################################
## Exercício 16: Desconto

valor = float(input("Qual o valor do produto: "))
desc = valor - valor * 0.1

print("O valor com desconto será: ", desc)

#################################################
## Exercício 17: Divisão

num1 = int(input("Digite o número que será dividido (dividendo):" ))
num2 = int(input("Digite o número que irá dividi-lo (divisor, menor que dividendo): "))

quoc = int(num1 / num2) 
resto = num1 - (quoc * num2)

print(f"O resultado da divisão será {quoc}, com resto {resto}.")