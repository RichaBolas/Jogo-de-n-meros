import random

print("Jogo de número")
print("2 reais ou um número misterioso entre 1 e 100.\n")

numero_misterioso = random.randint(1, 100)
tentativas = 0

while True:
    apostas = int(input("Faça suas apostas: "))
    tentativas += 1

    if apostas < numero_misterioso:
        print("O número misterioso é maior")
    elif apostas > numero_misterioso:
        print("O número misterioso é menor.")
    else:
        print(f"\nParabéns! Você acertou o número {numero_misterioso}.")
        print(f"Total de tentativas: {tentativas}")
        break