def leer_datos_del_archivo(el_archivo):
    """Abre y lee los datos de un archivo y los devuelve como una lista de listas. Manejamos excepciones por si el archivo no está disponible o si ocurre algún problema de permisos, entre otros."""    
    try:
        with open(el_archivo, "r", encoding="utf-8") as archivo:
            return [linea.strip().split(";") for linea in archivo] # Lee todas las lineas del archivo. Elimina los espacios en blanco al principio y al final de cada linea. Divide cada linea en una lista de elementos utilizando ";" como delimitador. Devuelve una lista de listas, donde cada sublista contiene los elementos de una linea del archivo, separados por ";".
    except FileNotFoundError:  # Captura el error si el archivo txt no fue encontrado.
        print(f"El archivo '{el_archivo}' no existe.")
        return []
    except Exception as e:  # Captura cualquier excepcion que ocurra durante la ejecución de un bloque de código
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []

def procesar_datos(lista):
    """Procesa y actualiza los datos de la lista de jugadoras y las agrupa por país."""
    lista_final = {}
    for pais, camiseta, nombre, pase, _ in lista:  # Inicializar el país y la jugadora si no existen, utilizamos _ para marcar de manera visual que ese dato no será utilizado en la función
        pais_dict = lista_final.setdefault(pais, {})  # Obtiene o crea el diccionario para el país
        jugadora = pais_dict.setdefault(nombre, {"numero": camiseta, "nombre": nombre, "cantidad_pases": 0, "pases_bien": 0, "pases_mal": 0})  # Obtiene o crea el diccionario para la jugadora (set default se usa cuando necesitas verificar que una key existe en el diccionario y obtener su valor, le da un valor predeterminado si la clave no existe.) FUENTE:https://www.w3schools.com/python/python_dictionaries_methods.asp

        if pase == "1":  # Actualizar estadísticas de pases
            jugadora["pases_bien"] += 1
        elif pase == "0":
            jugadora["pases_mal"] += 1

    return lista_final  # Devuelve un diccionario con los datos actualizados.

def contar_pases_y_efectividad(lista_final):
    """Recibe un diccionario con la informacion de las jugadoras: Calculando la suma de todos los pases buenos y malos que hicieron segun solicita el enunciado, el porcentaje de efectividad de los pases para cada jugadora y ordenando a la lista de jugadoras por país según su porcentaje de efectividad. Retorna el diccionario ya listo para ser impreso."""
    for pais, jugadoras in lista_final.items():
        for jugadora in jugadoras.values():
            jugadora["cantidad_pases"] = jugadora["pases_bien"] + jugadora["pases_mal"]           # Calcula la cantidad total de pases como lo solicita el enunciado
            jugadora["porcentaje"] = round((jugadora["pases_bien"] / jugadora["cantidad_pases"]) * 100, 2)                 # Calcula el porcentaje de efectividad de los pases y redondea a dos decimales
        
        # Convierte el diccionario de jugadoras de un país en una lista de diccionarios y ordena por porcentaje                       
        lista_final[pais] = sorted(jugadoras.values(), key=lambda x:x["porcentaje"], reverse=True)     # Procesa y ordena la lista de jugadoras por su porcentaje de efectividad de pases en orden descendente y las agrupa por pais.

    return lista_final           #Retorna lo solicitado en el desafio listo para ser impreso 

def main():
    """Función principal que coordina la lectura, procesamiento y presentación de los datos de pases de jugadoras(En la terminal). A su vez se encarga de llamar las diversas funciones."""
    nombre_archivo = "pases.txt"
    lista = leer_datos_del_archivo(nombre_archivo)
    if not lista:
        return
    lista_final = procesar_datos(lista)
    lista_final = contar_pases_y_efectividad(lista_final)
    print(lista_final)

main()        # Ejecuta la función 'main' para iniciar la generación y escritura de datos del desafío.