#clases/negocio.py
from .direccion import Direccion

class Negocio:
    """
    Clase para representar un negocio.
    Atributos:
        id_negocio (str): Identificador único del negocio.
        nombre (str): Nombre del negocio.
        direccion (Direccion): Dirección del negocio.
    """
    def __init__(self, id_negocio, nombre, direccion):
        self.id_negocio = id_negocio
        self.nombre = nombre
        self.direccion = direccion
        

    def __str__(self):
        return f"Negocio ID: {self.id_negocio}, Nombre: {self.nombre}, Dirección: {self.direccion}"