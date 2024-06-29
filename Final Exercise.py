import random
 
obstaculos = {              #las posibles vallas
    "valla baja": [1, 2],
    "valla media": [1, 2, 3],
    "valla alta": [1, 2, 3, 4]
}
 
jugador_tiempo = 10
 
def verificar(salto):
    """Verifica la entrada de salto, pide un reingreso por si este no es correcto"""
    try:
        while salto < 1 or salto > 4:
            salto = int(input("Ingrese un numero para el salto: "))
            if salto < 1 or salto > 4:
                print("Ingrese un numero valido")
        return salto
    except ValueError:                  #si no se entrega el valor correcto
        print("El ingreso es incorrecto. Intente nuevamente.")
        return verificar(int(input("Ingrese altura a saltar: ")))
 
 
 
def carrera(distancia):
    """Contiene la logica del juego"""
    print("\n¡Empezó la carrera!")
    global jugador_tiempo               #Se llama a una variable global
    for i in range(distancia):          #dependiendo de lo que eliga el jugador el loop es mayor o menor
        valla_siguiente = random.choice(list(obstaculos.keys()))            #elige la valla que le va a tocar al jugador
        computadora = random.choice(obstaculos[valla_siguiente])        
        print(f"\n¡Una {valla_siguiente} en frente! Elige un número entre {obstaculos[valla_siguiente]}")
       
        usuario = verificar(int(input("Ingrese el número para saltar la valla: ")))
       
        if usuario != computadora:
            jugador_tiempo += 1
            print("¡Te comiste la valla! Perdiste tiempo")
        else:
            print(f"Saltaste la {valla_siguiente}, no perdiste tiempo")
    print(f"El tiempo total del jugador es: {jugador_tiempo} segundos")
 
def bienvenida():
    """Da la bienvenida a la carrera y da a elegir el largo de la misma"""
    print("\nBienvenido a la carrera de vallas de los juegos olímpicos\nhabrá 3 tipos de pistas en las que podrás participar")
    print("1. Carrera corta\n2. Carrera media\n3. Carrera larga")
    try:
        tipo_carrera = int(input("Seleccione el tipo de carrera en el que quieres participar: "))
        if tipo_carrera == 1:
            return 10
        elif tipo_carrera == 2:
            return 20
        elif tipo_carrera == 3:
            return 30
        else:
            print("Selección no válida. Por favor, seleccione una opción válida.")
            return bienvenida()
    except ValueError:          #si no se entrega el valor correcto
        print("Error: No se introdujo un número")
        return bienvenida()
    except Exception as e:
        print(f"Error: {e}")
        return bienvenida()
 
def main():
    distancia_de_carrera = bienvenida()
    carrera(distancia_de_carrera)
main()