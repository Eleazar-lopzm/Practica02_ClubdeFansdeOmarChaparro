from manejocsv import guardar_en_csv, leer_csv, buscar_en_csv, eliminar_en_csv, editar_campo_csv

class AdministracionNegocio:
    """
    Administracion para operaciones comunes de Negocio.
    """
    def __init__(self):
        self.archivo_csv = 'datos/negocios.csv'
        self.encabezados = [
            'id_negocio', 'nombre', 'calle', 'ciudad', 'codigo_postal', 'rubro'
        ]

    def agregar(self, datos):
        """
        Agrega un nuevo negocio al archivo CSV.
        Parámetros:
            datos (list): Lista de datos del negocio.
        """
        guardar_en_csv(self.archivo_csv, datos)

    def consultar(self, id):
        """
        Consulta un negocio por su ID.
        Parámetros:
            id (str): ID del negocio a consultar.
        Retorna:
            list: Datos del negocio o None si no se encuentra.
        """
        return buscar_en_csv(self.archivo_csv, id)

    def eliminar(self, id):
        """
        Elimina un negocio por su ID.
        Parámetros:
            id (str): ID del negocio a eliminar.
        """
        eliminar_en_csv(self.archivo_csv, id)

    def editar(self, id, campo, nuevo_valor):
        """
        Edita un campo específico de un negocio.
        Parámetros:
            id (str): ID del negocio a editar.
            campo (str): Nombre del campo a editar.
            nuevo_valor (str): Nuevo valor para el campo.
        """
        editar_campo_csv(self.archivo_csv, id, campo, nuevo_valor)