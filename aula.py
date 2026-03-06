import random

opcoes = ["pedra", "papel", "tesoura"]

computador = random.choice(opcoes)

jogador = input("escolha pedra ou papel ou tesoura"). lower()

print("Computador escolheu: ", computador)

if jogador == computador:
    print ("Empate")

if jogador == "pedra":
    if computador == "tesoura":
        print("Voce Venceu!!")
else:
    print("Voce Perdeu")

if jogador == "papel":
    if computador == "pedra":
        print("Voce Venceu!!")
else:
    print("Voce Perdeu")

if jogador == "tesoura":
    if computador == "papel":
        print("Voce Venceu!!")
else:
    print("Voce Perdeu")














