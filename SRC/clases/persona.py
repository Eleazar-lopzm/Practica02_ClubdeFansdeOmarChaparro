# clases/persona.py
from .direccion import Direccion  # Importar la clase Direccion

class Persona:
    """
    Clase Persona => base para representar una persona.
    Atributos:
        id (str): Identificador único de la persona.
        primer_nombre (str): Primer nombre de la persona.
        segundo_nombre (str): Segundo nombre de la persona.
        ap_paterno(str): Apellido Paterno de la persona.
        ap_materno (str): Segundo apellido de la persona.
        direccion (Direccion): Objeto de tipo Direccion.
    """
    def __init__(self, id, primer_nombre, segundo_nombre, ap_paterno, ap_materno, direccion):
        self.id = id
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.ap_paterno= ap_paterno
        self.ap_materno = ap_materno
        self.direccion = direccion

    def __str__(self):
        nombre_completo = f"{self.primer_nombre} {self.segundo_nombre} {self.ap_paterno} {self.ap_materno}"
        return f"ID: {self.id}, Nombre: {nombre_completo}, Dirección: {self.direccion}"