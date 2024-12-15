# 1. Aprovando Empréstimo Bancário
# Crie um programa para uma instituição bancária que analisa o pedido de empréstimo.
# O cliente deve informar o valor do empréstimo, a renda mensal e o número de parcelas.
# O empréstimo será aprovado se o valor da parcela não exceder 30% da renda mensal.

valorEmprestimo = float(input("Digite o valor que você deseja emprestar: R$ "))
rendaMensal = float(input("Digite sua renda mensal: R$ "))
numeroParcelas = int(input("Digite o número de parcelas: "))

valorParcela = valorEmprestimo / numeroParcelas
limiteParcela = rendaMensal * 0.30

# Verifica se o valor da parcela não exceder 30% da renda mensal
if valorParcela <= limiteParcela:
    print("O empréstimo foi aprovado!")
    print("O valor da parcela é de R$ {:.2f}.".format(valorParcela))
else:
    print("Seu empréstimo não foi aprovado.")
    print("O valor da parcela de R$ {:.2f}, excede o valor de 30% da sua renda mensal".format(valorParcela))
