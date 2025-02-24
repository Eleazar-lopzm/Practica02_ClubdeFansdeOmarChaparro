from administracion.administracion_cliente import AdministracionCliente
from administracion.administracion_emprendedor import AdministracionEmprendedor
from administracion.administracion_negocio import AdministracionNegocio

def menu_clientes(servicio_cliente):
    """
    Muestra un menú para gestionar clientes.
    """
    while True:
        print("\n--- Menú de Clientes ---")
        print("1. Agregar Cliente")
        print("2. Consultar Cliente")
        print("3. Eliminar Cliente")
        print("4. Editar Cliente")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_cliente(servicio_cliente)
        elif opcion == '2':
            consultar_cliente(servicio_cliente)
        elif opcion == '3':
            eliminar_cliente(servicio_cliente)
        elif opcion == '4':
            editar_cliente(servicio_cliente)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


            
def menu_principal():
    """
    Muestra un menú principal para interactuar con el sistema.
    """

    administracion_cliente = AdministracionCliente()
    administracion_emprendedor = AdministracionEmprendedor()
    administracion_negocio = AdministracionNegocio()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar Clientes")
        print("2. Gestionar Emprendedores")
        print("3. Gestionar Negocios")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_clientes(administracion_cliente)
        elif opcion == '2':
            menu_emprendedores(administracion_emprendedor)
        elif opcion == '3':
            menu_negocios(administracion_negocio)
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()