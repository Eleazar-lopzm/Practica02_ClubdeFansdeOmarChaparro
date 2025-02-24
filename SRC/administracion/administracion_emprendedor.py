from administracion.administracion_persona import AdministracionPersona

class AdministracionEmprendedor(AdministracionPersona):
    """
    Administracion específico para emprendedores.
    """
    def __init__(self):
        super().__init__('datos/emprendedores.csv', [
            'id_emprendedor', 'primer_nombre', 'segundo_nombre', 'apellido_paterno', 'apellido_materno',
            'calle', 'ciudad', 'codigo_postal', 'negocio'
        ])