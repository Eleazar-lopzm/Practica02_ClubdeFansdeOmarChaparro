#administracion/administracion_cliente.py
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
    
    def agregar_cliente(self, datos):
        return super().agregar(datos)
    
    def consultar_cliente(self, id):
        return super().consultar(id)
    
    def editar_cliente(self, id, campo, nuevo_valor):
        return super().editar(id, campo, nuevo_valor)
    
    def eliminar_cliente(self, id):
        return super().eliminar(id)
    
    def leer_cliente(self, archivo):
        return super().leer(archivo)