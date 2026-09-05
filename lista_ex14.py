## Exercício 14 - Temperatura

celsius = float(input("Insira a temperatura em Celsius: "))
fah = celsius * 9/5 + 32

print(f"{celsius} graus Celsius equivalem a {fah} graus Frhreheit.")

fah2 = float(input("Digite a temperatura em Fahrenheit: "))
celsius2 = (-32 + fah2) / (9/5)

print(f"{fah2} graus Fherenaheit equivalem a {celsius2} graus Celsius.")
