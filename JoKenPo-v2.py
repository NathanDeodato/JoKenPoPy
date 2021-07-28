# Libs
import PySimpleGUI as sg
from time import sleep
from random import randint

# Start
def JoKenPo():
    sg.theme("DarkBlack")

    layout = [
        [sg.Text("Instruções → Óla, você jogará JoKenPo, e será contra mim.", text_color="white")],
        [sg.Text("Você deve estar se perguntando quem eu sou...", text_color="white")],
        [sg.Text("Bom, eu sou sua máquina.Será que conseguirá me ganhar? (:", text_color="white")],

        [sg.Text("=" * 45, text_color="white")],

        [sg.Text(" " * 30), sg.Text("- Select Element -", text_color="white")],

        [sg.Text(" " * 20), sg.Button("Pedra", button_color="white", size=(6, 0)), sg.Button("Papel", button_color="white", size=(6, 0)), sg.Button("Tesoura", button_color="white", size=(6, 0))],

        [sg.Text("=" * 45, text_color="white")],

        [sg.Output(size=(49, 6))],

        [sg.Text(" " * 32), sg.Text("(c) NT Developer", text_color="white")],
    ]
    return(sg.Window("JoKePo", layout=layout))


window = JoKenPo()

while True:
    try:
        event, values = window.read()    
        
        # Close Window
        if event == sg.WINDOW_CLOSED:
            break

        # Game
        ## Machine
        machine = randint(1, 3)
        
        machine1 = ["Pedra"]
        machine2 = ["Papel"]
        machine3 = ["Tesoura"]

        ## Player
        if event == "Pedra" and machine == 1:
            print("-" * 85)

            print("                    Player: Pedra | Machine: Pedra")

            print("-" * 85)

            print("                                     !EMPATE!")

            print("-" * 85)

        elif event == "Pedra" and machine == 2:
            print("-" * 85)

            print("                    Player: Pedra | Machine: Papel")

            print("-" * 85)

            print("                                  !MACHINE WIN!")

            print("-" * 85)

        elif event == "Pedra" and machine == 3:
            print("-" * 85)
            
            print("                    Player: Pedra | Machine: Tesoura")

            print("-" * 85)

            print("                                   !PALYER WIN!")
                        
            print("-" * 85)


        if event == "Papel" and machine == 2:
            print("-" * 85)

            print("                    Player: Papel | Machine: Papel")

            print("-" * 85)

            print("                                     !EMPATE!")

            print("-" * 85)

        elif event == "Papel" and machine == 1:
            print("-" * 85)

            print("                    Player: Papel | Machine: Pedra")

            print("-" * 85)

            print("                                     !PLAYER WIN!")

            print("-" * 85)

        elif event == "Papel" and machine == 3:
            print("-" * 85)

            print("                    Player: Papel | Machine: Tesoura")

            print("-" * 85)

            print("                                     !MACHINE WIN!")

            print("-" * 85)

        if event == "Tesoura" and machine == 3:
            print("-" * 85)

            print("                    Player: Tesoura | Machine: Tesoura")

            print("-" * 85)

            print("                                     !EMPATE!")

            print("-" * 85)

        elif event == "Tesoura" and machine == 1:
            print("-" * 85)

            print("                    Player: Tesoura | Machine: Pedra")

            print("-" * 85)

            print("                                     !MACHINE WIN!")

            print("-" * 85)

        elif event == "Tesoura" and machine == 2:
            print("-" * 85)
 
            print("                    Player: Tesoura | Machine: Papel")

            print("-" * 85)

            print("                                     !PLAYER WIN!")

            print("-" * 85)

    except Exception as error:
        print(f"{error}")
