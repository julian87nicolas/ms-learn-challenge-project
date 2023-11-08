#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

"""
Reglas del juego:

La piedra gana a las tijeras (las rompe).
Las tijeras han ganado al papel (lo cortan).
El papel gana a la piedra (la envuelve).
El minijuego es multijugador y el equipo juega el papel del oponente y elige un elemento aleatorio de la lista de elementos
Interacción con el jugador:

La consola se usa para interactuar con el jugador.
El jugador puede elegir una de las tres opciones: rock, paper o scissors.
El jugador puede elegir si vuelve a jugar.
Se debe advertir al jugador si introduce una opción no válida.
El jugador ve su puntuación al final del juego.
Validación de la entrada del usuario:

En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente.
El minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida.
Al final de cada ronda, el jugador debe responder si quiere jugar de nuevo o no.
"""

import random

# Definir una lista de opciones
opciones = ["rock", "paper", "scissors"]

# Definir una lista de opciones ganadoras
ganadoras = [["rock", "scissors"], ["scissors", "paper"], ["paper", "rock"]]
# Definir una lista de opciones perdedoras
perdedoras = [["scissors", "rock"], ["paper", "scissors"], ["rock", "paper"]]
# Definir una lista de opciones empatadas
empatadas = [["rock", "rock"], ["scissors", "scissors"], ["paper", "paper"]]

# Definir una variable para la puntuación del jugador
puntuacion = 0

# Definir una variable para la puntuación del oponente
puntuacion_oponente = 0

# Definir una variable para el número de rondas
rondas = 0

# Definir una variable para el número de rondas ganadas
rondas_ganadas = 0

# Definir una variable para el número de rondas perdidas
rondas_perdidas = 0

# Definir una variable para el número de rondas empatadas
rondas_empatadas = 0

# Definir una variable para el número de rondas jugadas
rondas_jugadas = 0

# Recibir la entrada del usuario
def obtener_entrada():
    entrada = input("Enter a choice (rock, paper, scissors): ")
    return entrada

# Obtener la entrada del usuario
entrada = obtener_entrada()

# Definir entrada de oponente
entrada_oponente = random.choice(opciones)

# Obtener resultado de la ronda
def obtener_resultado_ronda(entrada, entrada_oponente):
    if [entrada, entrada_oponente] in ganadoras:
        resultado = "ganada"
    elif [entrada, entrada_oponente] in perdedoras:
        resultado = "perdida"
    elif [entrada, entrada_oponente] in empatadas:
        resultado = "empatada"
    return resultado


# Ejecutar
while True:
    entrada = obtener_entrada()
    entrada_oponente = random.choice(opciones)
    resultado_ronda = obtener_resultado_ronda(entrada, entrada_oponente)
    if resultado_ronda == "ganada":
        puntuacion += 1
        rondas_ganadas += 1
        rondas_jugadas += 1
    elif resultado_ronda == "perdida":
        puntuacion_oponente += 1
        rondas_perdidas += 1
        rondas_jugadas += 1
    elif resultado_ronda == "empatada":
        rondas_empatadas += 1
        rondas_jugadas += 1
    print("You chose " + entrada + ", and your opponent chose " + entrada_oponente + ".")
    print("You " + resultado_ronda + " this round.")
    print("Your score is " + str(puntuacion) + ".")
    print("Your opponent's score is " + str(puntuacion_oponente) + ".")
    print("You have won " + str(rondas_ganadas) + " rounds, lost " + str(rondas_perdidas) + " rounds, and tied " + str(rondas_empatadas) + " rounds.")
    print("You have played " + str(rondas_jugadas) + " rounds.")
    continuar = input("Do you want to play again? (yes/no): ")
    if continuar == "no":
        # Imprimir puntuación final
        print("Your final score is " + str(puntuacion) + ".")
        print("Your opponent's final score is " + str(puntuacion_oponente) + ".")
        print("You won " + str(rondas_ganadas) + " rounds, lost " + str(rondas_perdidas) + " rounds, and tied " + str(rondas_empatadas) + " rounds.")
        break
