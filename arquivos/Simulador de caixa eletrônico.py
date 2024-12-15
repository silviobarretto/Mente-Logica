# 5. Simulador de Caixa Eletrônico
# Crie um programa que simula um caixa eletrônico. O usuário deve informar o
# valor do saque (apenas valores inteiros) e o programa deve informar
# quantas cédulas de cada valor serão fornecidas.
# Considere cédulas de R$100, R$50, R$20, R$10, R$5 e R$2.

valorSaque = int(input("Digite o valor do saque: "))

if valorSaque < 0:
    print("Valor inválido")
else:
    cedulas_100 = valorSaque // 100
    valorSaque %= 100
    
    cedulas_50 = valorSaque // 50
    valorSaque %= 50
    
    cedulas_20 = valorSaque // 20
    valorSaque %= 20
    
    cedulas_10 = valorSaque // 10
    valorSaque %= 10
    
    cedulas_5 = valorSaque // 5
    valorSaque %= 5
    
    cedulas_2 = valorSaque // 2
    valorSaque %= 2

    if valorSaque != 0:
        print("Não é possível sacar o valor específicado com a cédulas disponíveis")
    else:
        print("Cédulas entregues")
        if cedulas_100 > 0:
            print(f"{cedulas_100} x R$100")
        if cedulas_50 > 0:
            print(f"{cedulas_50} x R$50")
        if cedulas_20 > 0:
            print(f"{cedulas_20} x R$20")
        if cedulas_10 > 0:
            print(f"{cedulas_10} x R$10")  
        if cedulas_5 > 0:
            print(f"{cedulas_5} x R$5")
        if cedulas_2 > 0:
            print(f"{cedulas_2} x R$2")
