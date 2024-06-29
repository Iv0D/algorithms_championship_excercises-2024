import random

def generar_datos(jugadores_olimpiadas, iteraciones):
    """Genera los datos: pase realizados o no, pais, jugadora, dorsal y el minuto de juego, mediante un sistema aleatorio, que luego lo almacena en una lista"""
    datos_generados = []
    for _ in range(iteraciones):
        pase = random.randint(0, 1)
        pais, jugadora, numero = random.choice(jugadores_olimpiadas)
        minuto = random.randint(0, 60)                                  #Cambiamos los minutos debido a que investigamos que solo se juegan 60 minutos
        datos_generados.append((pais, numero, jugadora, pase, minuto))  #Añade los datos generados a la lista
    return datos_generados                                              #Devuelve la lista de datos generados

def escribir_archivo(datos, nombre_archivo):
    """Escribe los datos en un archivo .txt. Tomando la lista que devuelve la funcion datos_generados """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:                #El parámetro encoding="utf-8" especifica que el archivo se abrirá con codificación UTF-8, lo que es útil para manejar correctamente caracteres especiales y no ASCII
        for pais, numero, jugadora, pase, minuto in datos:                      #Itera sobre cada uno de los elementos de la lista 
            datos_linea = f"{pais};{numero};{jugadora};{pase};{minuto}\n"       #Crea una cadena de texto formateada que representa una línea de datos en el archivo de texto
            archivo.write(datos_linea)                                          #Escribe los datos generados al archivo           

def main():
    """Contiene las variables basicas y las llamadas a las distintas funciones. Tambien se podra notar que cambiamos y agregamos jugadoras para que los registros sean mas realistas"""
    jugadores_olimpiadas = [
        ("Argentina", "Agustina Gorzelany", 11),
        ("Argentina", "Ana Luz Dodorico", 9),
        ("Argentina", "Sofia Toccalino", 20),
        ("Argentina", "Agostina Alonso", 10),
        ("Argentina", "Valentina Raposo", 8),
        ("Argentina", "Clara Barberi", 5),
        ("Argentina", "Delfina Thome", 4),
        ("Argentina", "Lara Casas", 7),
        ("Argentina", "Pilar Campoy", 16),
        ("Argentina", "Luciana Aymar", 15),
        ("Australia", "Jodie Kenny", 4),
        ("Australia", "Emily Chalker", 16),
        ("Australia", "Georgina Morgan", 3),
        ("Australia", "Jane Claxton", 8),
        ("Australia", "Savannah Fitzpatrick", 20),
        ("Australia", "Karri McMahon", 9),
        ("Australia", "Grace Stewart", 17),
        ("Australia", "Kaitlin Nobbs", 14),
        ("Australia", "Ambrosia Malone", 13),
        ("Australia", "Rosie Malone", 12),
        
        
    ]

    iteraciones = 50000                                                  # Numero de pases a generar
    nombre_archivo = "Pases.txt"                                         # Nombre del archivo de salida

    datos_generados = generar_datos(jugadores_olimpiadas, iteraciones)   # Esta variable almacena return de generar_datos
    escribir_archivo(datos_generados, nombre_archivo)                    # El llamado de esta funcion aprovecha la variable anterior
    print("Archivo guardado exitosamente")


main()                                                                   # Ejecuta la función 'main' para iniciar la generación y escritura de datos del desafío.