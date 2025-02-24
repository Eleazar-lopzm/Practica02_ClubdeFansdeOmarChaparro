#manejocsv
import csv

def guardar_en_csv(archivo, datos):
    """
    Guarda una lista de datos en un archivo CSV.
    Parámetros:
        archivo (str): Ruta del archivo CSV.
        datos (list): Lista de datos a guardar.
    Abre el archivo en modo append 'a' (agregar), crea un objeto writer que va a escribir en una fila una lista de datos
    """
    with open(archivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(datos)


def leer_csv(archivo):
    """
    Lee todos los datos de un archivo CSV.
    Parámetros:
        archivo (str): Ruta del archivo CSV.
    Retorna:
        list: Lista de filas del archivo CSV.
    
    Abre el archivo en modo read, crea un reader para el archivo y nos regresa una lista de los datos
    """
    
    with open(archivo, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return list(reader)


def buscar_en_csv(archivo, id):
    """
    Busca una fila en un archivo CSV por su ID.
    Parámetros:
        archivo (str): Ruta del archivo CSV.
        id (str): ID a buscar.
    Retorna:
        list: Fila encontrada o None si no se encuentra.

    Abre el archivo en modo lectura y busca en cada columna si el id está
    """
    with open(archivo, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:  # El ID está en la primera columna
                return row
    return None


def eliminar_en_csv(archivo, id):
    """
    Elimina una fila de un archivo CSV por su ID.
    Parámetros:
        archivo (str): Ruta del archivo CSV.
        id (str): ID a eliminar.
    Abre el archivo en modo escritura 'w' filtra todas las filas que no sean la del id que queremos eliminar y clona las demas, y vuelve a escribir el archivo
    """
    filas = leer_csv(archivo)
    filas = [fila for fila in filas if fila[0] != id]  # Filtra las filas que no coincidan con el ID
    with open(archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(filas)


def editar_campo_csv(archivo, id, campo, nuevo_valor):
    """
    Edita un campo específico en una fila del archivo CSV.
    Parámetros:
        archivo (str): Ruta del archivo CSV.
        id (str): ID de la fila a editar.
        campo (str): Nombre del campo a editar (debe coincidir con el encabezado).
        nuevo_valor (str): Nuevo valor para el campo.
    """
    try:
        # Leer todas las filas del archivo
        filas = leer_csv(archivo)
        encabezados = filas[0]  # La primera fila contiene los encabezados
        datos = filas[1:]  # Las filas restantes contienen los datos

        # Buscar la fila que coincide con el ID
        for fila in datos:
            if fila[0] == id:  # El ID está en la primera columna
                # Obtener el índice del campo a editar
                indice_campo = encabezados.index(campo)
                # Actualizar el campo específico
                fila[indice_campo] = nuevo_valor
                break

        # Sobrescribir el archivo CSV con los datos actualizados
        with open(archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(encabezados)  # Escribir los encabezados
            writer.writerows(datos)  # Escribir los datos actualizados

        print(f"Campo '{campo}' actualizado con éxito.")
    except Exception as e:
        print(f"Error al editar el campo: {e}")