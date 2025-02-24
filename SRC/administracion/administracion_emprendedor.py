#administracion/administracion_emprendedor
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
    
    def agregar_emprendedor(self, datos):
        return super().agregar(datos)
    
    def consultar_emprendedor(self, id):
        return super().consultar(id)
    
    def eliminar_emprendedor(self, id):
        return super().eliminar(id)
    
    def editar_emprendedor(self, id, campo, nuevo_valor):
        return super().editar(id, campo, nuevo_valor)
    
    def leer_emprendedor(self,archivo):
        return super().leer(archivo)