# Crie um programa que verifica se uma pessoa pode assistir a um
# filme classificado como "maiores de 16 anos".
# Dados:
# Idade da pessoa: Pergunte ao usuário

idade = int(input('Qual a sua idade? '))

autorizacao = (idade >= 16)

print('Você tem permissão para assistir ao filme?', autorizacao)
