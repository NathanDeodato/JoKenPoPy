# Libs
from random import randint
from time import sleep

# Colors
verde = '\033[32m'
vermelho = '\033[31m'
ciano = '\033[36m'
branco = '\033[37m'

# Start Game
print(branco + "=" * 100)

print(verde + "<< JoKenPo >>".center(100))

print(branco + "=" * 100)
sleep(1)

print(verde +"Instruções → Óla, você jogará JoKenPo, e será contra mim.")
print("Você estar se perguntando quem eu sou... Bom, eu sou sua máquina.")
print("Será que conseguirá me ganhar? (:" + branco)

print("=" * 100)
sleep(3)

print(verde + "[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA" + branco)

print(branco + "=" * 100)
sleep(1)

# Game
def JoKenPo(player, machine):
    elementos = ["PEDRA", "PAPEL", "TESOURA"]
    
    print(branco + "=" * 100)

    print(verde + "← JO! →")
    sleep(1)
    print(verde + "← KEN! →")
    sleep(1)
    print(verde + "← PO! →")
    sleep(1)

    print(branco + "=" * 100)
    
    sleep(1)
    print(verde + f"Player: → {elementos[player]} ←")
    sleep(1)
    print(verde + f"Machine: → {elementos[machine]} ←")
    sleep(1)

    print(branco + "=" * 100)
    sleep(1)

    # Verification elements
    result = ""
    if player == machine:
        result = "! EMPATE !"
    elif player == 0 and machine == 1:
        result= "! Machine Win !"
    elif player == 0 and machine == 2:
        result = "! Player Win !"
    elif player == 1 and machine == 0:
        result = "! Player Win !"
    elif player == 1 and machine == 2:
        result = "! Machine Win !"
    elif player == 2 and machine == 0:
        result = "! Machine Win !"
    elif player == 2 and machine == 0:
        result = "! Player Win !"
    
    print(verde + result.center(100))

    print(branco + "=" * 100)


player = int(input(verde + "Que elemento deseja ser? "))
machine = randint(0, 2)

sleep(1)

JoKenPo(player, machine)
