# 3. Calculadora de Tarifas de Táxi
# Uma empresa de táxi cobra uma tarifa básica de R$4.00, mais R$0.25 por quilômetro rodado.
# Crie um programa que calcula o valor total da corrida com base na distância percorrida.

valorTarifa = 4.00
valorKm = 0.25
distancia = float(input("Digite a distância percorrida em km: "))

# Calcula o valor total da corrida

valorTotal = valorTarifa + (distancia * valorKm)
print("O valor total da corrida é R$ {:.2f}".format(valorTotal))
