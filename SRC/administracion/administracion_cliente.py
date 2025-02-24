from administracion.administracion_persona import AdministracionPersona

class AdministracionCliente(AdministracionPersona):
    """
    Admministracion específica para clientes.
    """
    def __init__(self):
        super().__init__('datos/clientes.csv', [
            'id_cliente', 'primer_nombre', 'segundo_nombre', 'apellido_paterno', 'apellido_materno',
            'calle', 'ciudad', 'codigo_postal', 'telefono'
        ])