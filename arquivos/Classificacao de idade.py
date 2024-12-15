# 3. Classificação de Idade
# Crie um programa que classifica a idade de uma pessoa em:
# Criança: 0 a 12 anos
# Adolescente: 13 a 17 anos
# Adulto: 18 a 59 anos
# Idoso: 60 anos ou mais

idade = int(input("Digite a sua idade: "))
if idade >= 0 and idade <= 12:
    print("Você é uma criança")
elif idade >= 13 and idade <= 17:
    print("Você é adolescente")
elif idade >= 18 and idade <= 59:
    print("Você é adulto")
elif idade >= 60:
    print("Você é Idoso")
else:
    print("Idade não encontrada")