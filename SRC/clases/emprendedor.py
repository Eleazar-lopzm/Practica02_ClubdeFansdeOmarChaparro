from .persona import Persona  # Importar la clase Persona

class Emprendedor(Persona):
    """
    Clase para representar un emprendedor. Hereda de Persona.
    Atributos adicionales:
        negocio (str): Nombre del negocio del emprendedor.
    """
    def __init__(self,id_emprendedor, primer_nombre, segundo_nombre, ap_paterno, ap_materno, direccion, negocio):
        super().__init__(id_emprendedor,primer_nombre, segundo_nombre, ap_paterno, ap_materno, direccion)
        self.negocio = negocio

    def __str__(self):
        return f"Emprendedor: {super().__str__()}, Negocio: {self.negocio}"