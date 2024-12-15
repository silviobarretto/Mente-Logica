# 1. Decidindo o que vistir
clima = "tempestade"

if clima == "ensolarado":
    print("Vista uma camisa e shorts.")
elif clima == "nublado":
    print("Leve uam jaqueta leve.")
elif clima == "chuvoso":
    print("Não esqueça do guarda-chuva.")
else:
    print("Verifique a previsão do tempo.")

print("##############################################")

# 2. Semáfaro
semafaro = "vermelho"

if semafaro == "vermelho":
    print("Não passe.")
elif semafaro == "amarelo":
    print("Prepare-se para parar.")
elif semafaro == "verde":
    print("Siga em frente.")
else:
    print("Semaforo não reconhecido.")

print("##############################################")

# 3. Calculando Descontos em Compras
#Situação: Uma loja oferece descontos com base no valor da compra.
# Se o valor for maior ou igual a R$1000, o desconto é de 10%.
# Se for entre R$500 e R$999, o desconto é de 5%.
# Caso contrário, não há desconto

valorCompra = 500
print("Valor da compra: R$ {:.2f}".format(valorCompra))

if valorCompra >= 1000:
    desconto = valorCompra * 0.10
    print("Desconto de 10%: R$ {:.2f}".format(desconto))
elif valorCompra >= 500 and valorCompra <= 999:
    desconto = valorCompra * 0.05
    valorTotal = valorCompra - desconto
    print("Desconto de 5%: R$ {:.2f}".format(desconto))
else:
    desconto = 0
    print("Nenhum desconto foi aplicado.")

valorTotal = valorCompra - desconto
print("Valor total da compra: R$ {:.2f}".format(valorTotal))

print("##############################################")

# 4. Planejando um Passeio
# Situação: Você quer fazer um passeio ao parque, mas depende do clima e do dia da semana.
# Se for fim de semana (sábado ou domingo) e não estiver chovendo, você vai ao parque.
# Caso contrário, fica em casa e assiste a um filme.

diaDaSemana = "domingo"
chovendo = False
print("Dia da semana {}". format(diaDaSemana))
print("Está chovendo: {}".format(chovendo))

if (diaDaSemana == "sábado" or diaDaSemana == "domingo") and not chovendo:
    print("Vou ao parque")
else:
    print("Fico em casa e assisto a um filme")

print("##############################################")

# Exercícios Práticos
# 1. Verificando Se um Número é Positivo, Negativo ou Zero
# Crie um programa que solicita um número ao usuário e verifica se ele é:
# positivo, negativo ou zero.

num = int(input("Digite um número: (Positivo, Negativo ou Zero) "))
print("Número digitado:", num)
if num < 0:
    print("O número é negativo")
elif num > 0:
    print("O número é positivo")
else:
    print("O número é zero")
