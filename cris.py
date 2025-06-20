import random

def obtener_eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (
        (usuario == "piedra" and computadora == "tijera") or
        (usuario == "tijera" and computadora == "papel") or
        (usuario == "papel" and computadora == "piedra")
    ):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def jugar():
    print("Bienvenido a Piedra, Papel o Tijera")
    usuario = input("Elige piedra, papel o tijera: ").lower()

    if usuario not in ["piedra", "papel", "tijera"]:
        print("Opción no válida.")
        return

    computadora = obtener_eleccion_computadora()
    print(f"La computadora eligió: {computadora}")

    resultado = determinar_ganador(usuario, computadora)
    print(resultado)

# Ejecutar el juego
jugar()
