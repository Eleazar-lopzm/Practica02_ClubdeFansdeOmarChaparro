# clases/cliente.py
from .persona import Persona  # Importar la clase Persona

class Cliente(Persona):
    """
    Clase para representar un cliente. Hereda de Persona.
    Atributos adicionales:
        telefono (str): Número de teléfono del cliente.
    """
    def __init__(self, id_cliente, primer_nombre, segundo_nombre, ap_paterno, ap_materno, direccion, telefono):
        super().__init__(id_cliente, primer_nombre, segundo_nombre, ap_paterno, ap_materno, direccion)
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {super().__str__()}, Teléfono: {self.telefono}"