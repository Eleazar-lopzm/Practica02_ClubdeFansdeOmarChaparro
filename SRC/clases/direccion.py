class Direccion:
    """
    Clase para representar una dirección.
    Atributos:
        calle (str): Nombre de la calle.
        ciudad (str): Ciudad de residencia.
        num_ext (str): Numero Exterior.
        num_int (str): Numero interior
        codigo_postal (str): Código postal.
    """
    def __init__(self, calle,num_ext, num_int, ciudad, codigo_postal):
        self.calle = calle
        self.num_ext = num_ext
        self.num_int = num_int
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal

    def __str__(self):
        return f"{self.calle},{self.num_ext},{self.num_int}, {self.ciudad}, {self.codigo_postal}"