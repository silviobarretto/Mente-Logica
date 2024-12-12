# O Índice de Massa Corporal (IMC) é calculado dividindo o peso (em kg)
# pela altura (em metros) elevada ao quadrado.
# Crie um programa que calcula o IMC e verifica se a pessoa está
# dentro do peso ideal (IMC entre 18.5 e 24.9)

altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))

calculoImc = peso / (altura ** 2)

pesoIdeal = (calculoImc >= 18.5) and (calculoImc <= 24.9)

print('Seu IMC é {:.2f}. Você está dentro do peso ideal? {}'.
      format(calculoImc, pesoIdeal))
