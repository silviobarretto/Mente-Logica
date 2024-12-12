# Crie um programa que solicita um número inteiro ao usuário e
# verifica se ele é par ou ímpar.

num = int(input('Digite um número inteiro: '))

resultado = (num % 2) == 0

print('Número digitado: {}. Seu número é par? {}'.format(num, resultado))
