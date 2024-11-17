import random

def obtener_eleccion_usuario():
    """
    Solicita al usuario que ingrese su elección y la devuelve.
    """
    while True:
        eleccion = input("Elige piedra, papel o tijera: ").lower()
        if eleccion in ["piedra", "papel", "tijera"]:
            return eleccion
        else:
            print("Elección no válida. Intenta de nuevo.")

def obtener_eleccion_computadora():
    """
    Genera y devuelve una elección aleatoria para la computadora.
    """
    elecciones = ["piedra", "papel", "tijera"]
    return random.choice(elecciones)

def determinar_ganador(usuario, computadora):
    """
    Determina y devuelve el ganador basándose en las elecciones del usuario y la computadora.
    """
    if usuario == computadora:
        return "Empate"
    
    if (usuario == "piedra" and computadora == "tijera") or \
       (usuario == "papel" and computadora == "piedra") or \
       (usuario == "tijera" and computadora == "papel"):
        return "Usuario"
    else:
        return "Computadora"

def mostrar_resultado(usuario, computadora, ganador):
    """
    Muestra el resultado del juego.
    """
    print(f"\nUsuario eligió: {usuario}")
    print(f"Computadora eligió: {computadora}")
    if ganador == "Empate":
        print("Es un empate.")
    else:
        print(f"{ganador} gana.")

def main():
    """
    Función principal que coordina el juego de piedra, papel y tijera.
    """
    print("Bienvenido al juego de Piedra, Papel y Tijera!")
    
    while True:
        usuario = obtener_eleccion_usuario()
        computadora = obtener_eleccion_computadora()
        ganador = determinar_ganador(usuario, computadora)
        mostrar_resultado(usuario, computadora, ganador)
        
        jugar_nuevamente = input("\n¿Quieres jugar otra vez? (yes/no): ").lower()
        if jugar_nuevamente != "yes":
            break
    
    print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()
