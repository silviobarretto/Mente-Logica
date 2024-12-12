# Três amigos vão dividir igualmente uma conta de R$150.
# Verifique quanto cada um deve pagar e se a divisão é exata
# (sem centavos restantes).

valorConta = 150.0
qtdePessoas = 3

pagamento = valorConta / qtdePessoas

divisaoExata = (valorConta % qtdePessoas) == 0

print('Cada pessoa deve pagar R$ {:.2f}'.format(pagamento))
print('A divisão é exata?', divisaoExata)
