# Libs
from os import system
from random import randint
from time import sleep

# Colors
azul = '\033[1;34m'
vermelho = '\033[1;31m'
preto = '\033[1;30m'

# Start Game
print(preto + "=" * 100)

print(azul + "<< JoKenPo >>".center(100))

print(preto + "=" * 100)
sleep(1)

print(azul +"Instruções → Óla, você jogará JoKenPo, e será contra mim.")
print("Você deve estar se perguntando quem eu sou... Bom, eu sou sua máquina.")
print("Será que conseguirá me ganhar? (:" + preto)

print("=" * 100)
sleep(3)

# Placar
#empates = 0
#player_wins = 0
#machine_wins = 0


# Game
def JoKenPo():
    elementos = ["PEDRA", "PAPEL", "TESOURA"]
    
    print(azul + "[ 0 ] PEDRA")
    print("[ 1 ] PAPEL")
    print("[ 2 ] TESOURA")

    print(preto + "=" * 100)
    sleep(1)

    while True:
        try:
            player = int(input(azul + "Que elemento deseja ser? "))
            machine = randint(0, 2)

            print(preto + "=" * 100)

            print(azul + "← JO! →")
            sleep(1)
            print(azul + "← KEN! →")
            sleep(1)
            print(azul + "← PO! →")
            sleep(1)

            print(preto + "=" * 100)
            
            sleep(1)
            print(azul + f"Player: → {elementos[player]} ←")
            sleep(1)
            print(azul + f"Machine: → {elementos[machine]} ←")
            sleep(1)

            print(preto + "=" * 100)
            sleep(1)

            # Verification elements
            result = ""
            if player == machine:
                result = "! EMPATE !"
            elif player == 0 and machine == 1:
                result = "! Machine Win !"
            elif player == 0 and machine == 2:
                result = "! Player Win !"
            elif player == 1 and machine == 0:
                result = "! Player Win !"
            elif player == 1 and machine == 2:
                result = "! Machine Win !"
            elif player == 2 and machine == 0:
                result = "! Machine Win !"
            elif player == 2 and machine == 1:
                result = "! Player Win !"
            
            print(azul + result.center(100))

            print(preto + "=" * 100)
            
            break

        except Exception as erro:
            print(preto + "=" * 100)
            print(vermelho + f"Erro: {erro}")
            print(preto + "=" * 100)


# Loop JoKenPo
while True:
    go = 0
    try:
        print(azul + "<< JoKenPo Start >>".center(100))
        print(preto + "=" * 100)

        print(azul + "[ 1 ] Sim")
        print("[ 2 ] Não")

        go = int(input(azul + "Continue? "))
        while go != 1 and go != 2:
            go = int(input("Continue? "))

        print(preto + "=" * 100)

        if go == 1:
            JoKenPo()
            go = 0
            
        elif go == 2:
            #print(f"! Player wins !: {player_wins}")
            #print(f"! Machine wins !: {machine_wins}")
            #print(f"! Empates !: {empates}")
            
            system("cls")

            print(azul + "<< JokenPo End >>".center(100))
            print(preto + "=" * 100)

            print(azul + "(c) NT Developer".center(100))
            print(preto + "=" * 100)

            break

        print(azul + "(c) NT Developer".center(100))
        print(preto + "=" * 100)

    except Exception as erro:
        print(preto + "=" * 100)
        print(vermelho + f"Erro: {erro}")
        print(preto + "=" * 100)
