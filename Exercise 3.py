import random

def generar_arco():
    """Genera los posibles lugares a tirar en el arco. Simulando el juego en cuestion."""
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Devuelve una matriz representando el arco

def mostrar_arco(arco):                    # Imprime la matriz del arco.
    print("_____")           
    for fila in arco:                      # Permite encuadrar los numeros del arco
        print("|", end=" ")             
        for posicion in fila:
            print(f" {posicion} ", end=" ")  
        print("|")           

def obtener_posicion(accion):
    """Solicita al usuario que ingrese una posición para tirar o atajar, validando posteriormente si es un caracter valido para el juego, Repite la solicitud si es necesario."""
    while True:
        eleccion = input(f"\nElija donde desea {accion} (1-9): ")  # Solicita una posición al usuario
        try:
            valor = int(eleccion)                       # Intenta convertir la entrada a un número entero
            if 1 <= valor <= 9:                         # Filtra si es el valor correcto
                return valor                            # Devuelve el valor si está en el rango correcto saliendo del bucle
            print("El valor debe estar entre 1 y 9.")  
        except ValueError:
            print("Entrada no válida. Por favor, elija un número entre 1 y 9.")  # Mensaje de error si la entrada no es un número

def evaluar_disparo(disparo_usuario, usuario, marcador):
    """Evalúa el disparo comparando las elecciones del usuario y la computadora. Actualiza el marcador según el resultado del disparo."""
    disparo_computadora = random.randint(1, 9)  # La computadora elige una posición al azar
    if usuario:                          # Evalua si es el jugador
        if disparo_usuario != disparo_computadora and disparo_usuario not in [2, 5, 8]:  # Determina si es gol del usuario o no
            print("¡Gol del usuario!")
            marcador["usuario"] += 1      # Incrementa el marcador del usuario si es gol
        else:
            print("¡Atajado por la computadora!")  
    else:
        if disparo_computadora != disparo_usuario and disparo_computadora not in [2, 5, 8]:  # Determina si es gol de la computadora o no o no
            print("¡Gol de la computadora!")       
            marcador["computadora"] += 1  # Incrementa el marcador de la computadora si es gol
        else:
            print("¡Atajado!")            
    print(f"Marcador: Usuario {marcador['usuario']} - Computadora {marcador['computadora']}")  # Muestra el marcador actualizado una ves se resuelva el tiro en cuestion

def alternar_turnos(marcador, intentos):
    """Alterna los turnos de tiro entre el usuario y la computadora."""
    for i in range(intentos):                                                   # La variable intentos dentro del bucle permite la flexibilidad por si es la tanda normal de penales o la muerte subita
        print(f"\nRonda {(i + 1)}")
        evaluar_disparo(obtener_posicion("tirar"), True, marcador)              # La funcion llama a obtener_posicion obteniendo el tiro del usuario, de ahi la funcion principal determina que ocurre, el True verifica que es el usuario y el marcador esta para poder informar el resultado como quedo
        if marcador["usuario"] > marcador["computadora"] + (intentos - i) or marcador["computadora"] > marcador["usuario"] + (intentos - i - 1):      # Verifica que no haya un ganador de manera prematura
            break                                                               # Termina si el usuario o maquina tiene una ventaja inalcanzable                                                     
        evaluar_disparo(obtener_posicion("atajar"), False, marcador)            # Lo mismo pero esta ves el usuario elije con el objetivo de atajar y el False avisa al programa que patea la computadora
        if marcador["usuario"] > marcador["computadora"] + (intentos - i - 1) or marcador["computadora"] > marcador["usuario"] + (intentos - i - 1):
            break  

def determinar_ganador(marcador):
    """Determina y anuncia el ganador de la tanda de penales. En caso de empate iniciara la muerte subita."""
    if marcador["usuario"] > marcador["computadora"]:
        print("\n¡El usuario gana la tanda de penales!")  # Anuncia al usuario como ganador
    elif marcador["usuario"] < marcador["computadora"]:
        print("\n¡La computadora gana la tanda de penales!")  # Anuncia a la computadora como ganadora
    else:
        print("\n¡Empate! Se procede a muerte súbita.")  # Anuncia empate y procede o continua la muerte súbita
        muerte_subita(marcador)

def muerte_subita(marcador):
    """Ejecuta rondas de muerte súbita hasta que uno de los participantes obtenga la ventaja en el marcador."""
    while marcador["usuario"] == marcador["computadora"]:
        alternar_turnos(marcador, 1)  # Alterna turnos hasta que haya un ganador
    determinar_ganador(marcador)  # Determina y anuncia el ganador

def main():
    """Función principal."""
    print("Bienvenido a la tanda de penales.")
    arco = generar_arco()
    mostrar_arco(arco)  # Muestra el arco al iniciar el juego

    intentos = 5
    marcador = {"usuario": 0, "computadora": 0}  # Inicializa el marcador

    # Alterna los turnos de disparo
    alternar_turnos(marcador, intentos)
    # Determinar el ganador, inicia una muerte subita en caso de empate
    determinar_ganador(marcador)

main()
