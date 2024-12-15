# 2. Calculadora Simples
# Crie um programa que pede ao usuário dois números e uma operação (+, -, *, /) e
# realiza o cálculo correspondente.

num1 = int(input("Digite primeiro número: "))
operacao = (input("Qual operação deseja realizar (+, -, *, /): "))
num2 = int(input("Digite segundo número: "))

if operacao == "+":
    resultado = num1 + num2
    print("O resultado da adição é: ", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("O resultado da subtração é: ", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("O resultado da multiplicação é: ", resultado)
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("O resultado da divisão é: ", resultado)
    else:
        print("Erro: Divisão por zero!")
else:
    print("Você não escolheu")