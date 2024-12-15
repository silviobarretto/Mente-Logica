import random

# 2. Jogo Pedra, Papel ou Tesoura
# Crie um programa que simula o jogo "Pedra, Papel ou Tesoura" entre o usuário e o computador.

opcoes = ["pedra", "papel", "tesoura"]

usuario = input("Escolha uma opção (pedra, papel ou tesoura): ").lower()
computador = random.choice(opcoes)

print(f"Você escolheu {usuario}")
print(f"O computador escolheu {computador}")

if usuario == computador:
    print("Empate!")
elif (usuario == "pedra" and computador == "tesoura") or \
        (usuario == "tesoura" and computador == "papel") or \
        (usuario == "papel" and computador == "pedra"):
    print("Você venceu!")
elif usuario in opcoes:
    print("Você perdeu!")
else:
    print("Escolha inválida!")
