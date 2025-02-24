#main
from administracion.administracion_cliente import AdministracionCliente
from administracion.administracion_cliente import agregar_cliente, consultar_cliente, eliminar_cliente, editar_cliente, leer_cliente
from administracion.administracion_emprendedor import AdministracionEmprendedor
from administracion.administracion_emprendedor import agregar_emprendedor, consultar_emprendedor, eliminar_emprendedor, editar_emprendedor, leer_emprendedor

from administracion.administracion_negocio import AdministracionNegocio
from administracion.administracion_negocio import agregar_negocio, consultar_emprendedor, eliminar_emprendedor, editar_emprendedor, leer_negocio


def menu_clientes():
    """
    Muestra un menú para gestionar clientes.
    """
    while True:
        print("\n--- Menú de Clientes ---")
        print("1. Agregar Cliente")
        print("2. Consultar Cliente")
        print("3. Eliminar Cliente")
        print("4. Editar Cliente")
        print("5. Leer Lista Clientes")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_cliente()
        elif opcion == '2':
            consultar_cliente()
        elif opcion == '3':
            eliminar_cliente()
        elif opcion == '4':
            editar_cliente()
        elif opcion == '5':
            leer_cliente()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_emprendedores():
    """
    Muestra un menú para gestionar clientes.
    """
    while True:
        print("\n--- Menú de Emprendedores ---")
        print("1. Agregar Emprendedor")
        print("2. Consultar Emprendedor")
        print("3. Eliminar Emprendedor")
        print("4. Editar Emprendedor")
        print("5. Leer Lista Emprendedores")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_emprendedor()
        elif opcion == '2':
            consultar_emprendedor()
        elif opcion == '3':
            eliminar_emprendedor()
        elif opcion == '4':
            editar_emprendedor()
        elif opcion == '5':
            leer_emprendedor()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_negocios():
    """
    Muestra un menú para gestionar clientes.
    """
    while True:
        print("\n--- Menú de Negocios ---")
        print("1. Agregar Negocios")
        print("2. Consultar Negocios")
        print("3. Eliminar Negocios")
        print("4. Editar Negocios")
        print("5. Leer Lista Negocios")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_cliente()
        elif opcion == '2':
            consultar_cliente()
        elif opcion == '3':
            eliminar_cliente()
        elif opcion == '4':
            editar_cliente()
        elif opcion == '5':
            leer_negocio()
        elif opcion == '6':
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