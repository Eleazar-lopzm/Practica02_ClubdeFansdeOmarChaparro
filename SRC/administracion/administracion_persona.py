#administracion/administracion Persona
from manejocsv import guardar_en_csv, leer_csv, buscar_en_csv, eliminar_en_csv, editar_campo_csv

class AdministracionPersona:
    """
    Servicio base para operaciones comunes de objetos de tipo Persona.
    """
    def __init__(self, archivo_csv, encabezados):
        self.archivo_csv = archivo_csv
        self.encabezados = encabezados
    
    def agregar(self, datos):
        """
        Agrega una nueva persona al archivo CSV.
        Parámetros:
            datos (list): Lista de datos de la persona.
        """
        guardar_en_csv(self.archivo_csv, datos)

    def consultar(self, id):
        """
        Consulta una persona por su ID.
        Parámetros:
            id (str): ID de la persona a consultar.
        Retorna:
            list: Datos de la persona o None si no se encuentra.
        """
        return buscar_en_csv(self.archivo_csv, id)

    def eliminar(self, id):
        """
        Elimina una persona por su ID.
        Parámetros:
            id (str): ID de la persona a eliminar.
        """
        eliminar_en_csv(self.archivo_csv, id)

    def editar(self, id, campo, nuevo_valor):
        """
        Edita un campo específico de una persona.
        Parámetros:
            id (str): ID de la persona a editar.
            campo (str): Nombre del campo a editar.
            nuevo_valor (str): Nuevo valor para el campo.
        """
        editar_campo_csv(self.archivo_csv, id, campo, nuevo_valor)
    
    def leer(self, archivo):
        leer_csv(self.archivo_csv)