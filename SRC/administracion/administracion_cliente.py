# administracion/administracion_cliente.py
from administracion.administracion_persona import AdministracionPersona

class AdministracionCliente(AdministracionPersona):
    """
    Administración específica para clientes.
    """
    def __init__(self):
        super().__init__('datos/clientes.csv', [
            'id_cliente', 'primer_nombre', 'segundo_nombre', 'apellido_paterno', 'apellido_materno',
            'calle', 'ciudad', 'codigo_postal', 'telefono'
        ])

    def generar_id_cliente(self):
        # Leer los clientes existentes
        clientes = super().leer(self.archivo_csv)

        # Si ya existen clientes, generar el id_cliente basado en el máximo ID actual
        if clientes:
            # Extraemos el id_cliente de los clientes existentes y buscamos el máximo
            ids_existentes = [int(cliente[0]) for cliente in clientes]  # Convertimos los ids a enteros
            nuevo_id = max(ids_existentes) + 1  # El nuevo ID será el máximo + 1
        else:
            # Si no hay clientes, el primer id será 1
            nuevo_id = 1
        
        return nuevo_id
    
    def agregar_cliente(self):
        # Generar automáticamente un nuevo id_cliente
        id_cliente = self.generar_id_cliente()

        primer_nombre = input("Ingrese el primer nombre: ")
        segundo_nombre = input("Ingrese el segundo nombre: ")
        apellido_paterno = input("Ingrese el apellido paterno: ")
        apellido_materno = input("Ingrese el apellido materno: ")
        calle = input("Ingrese la calle: ")
        ciudad = input("Ingrese la ciudad: ")
        codigo_postal = input("Ingrese el código postal: ")
        telefono = input("Ingrese el teléfono: ")

        # Crear la lista de datos del cliente
        datos_cliente = [id_cliente, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, calle, ciudad, codigo_postal, telefono]

        # Llamar al método de la clase base para agregar el cliente
        return super().agregar(datos_cliente)
    
    def consultar_cliente(self):
        # Solicitar el ID del cliente a consultar dentro del método
        id_cliente = input("Ingrese el ID del cliente a consultar: ")
        cliente = super().consultar(id_cliente)
        if cliente:
            print(cliente)
        else:
            print("Cliente no encontrado.")
    
    def editar_cliente(self):
        # Solicitar el ID del cliente a editar dentro del método
        id_cliente = input("Ingrese el ID del cliente a editar: ")
        
        # Buscar el cliente y obtener sus datos
        cliente = super().consultar(id_cliente)
        if not cliente:
            print("Cliente no encontrado.")
            return
        
        # Solicitar el campo a editar
        print("\nCampos disponibles para editar: ")
        print("1. Primer Nombre")
        print("2. Segundo Nombre")
        print("3. Apellido Paterno")
        print("4. Apellido Materno")
        print("5. Calle")
        print("6. Ciudad")
        print("7. Código Postal")
        print("8. Teléfono")
        print("9. Dirección (Calle, Ciudad, Código Postal)")
        
        campo = input("Ingrese el número del campo a editar: ")

        # Según el campo, se edita el valor correspondiente
        if campo == '9':  # Si es dirección
            calle = input(f"Ingrese la nueva calle (actual: {cliente[5]}): ")
            ciudad = input(f"Ingrese la nueva ciudad (actual: {cliente[6]}): ")
            codigo_postal = input(f"Ingrese el nuevo código postal (actual: {cliente[7]}): ")
            # Actualizamos los datos en la lista
            cliente[5] = calle
            cliente[6] = ciudad
            cliente[7] = codigo_postal
        elif campo == '1':
            nuevo_valor = input(f"Ingrese el nuevo primer nombre (actual: {cliente[1]}): ")
            cliente[1] = nuevo_valor
        elif campo == '2':
            nuevo_valor = input(f"Ingrese el nuevo segundo nombre (actual: {cliente[2]}): ")
            cliente[2] = nuevo_valor
        elif campo == '3':
            nuevo_valor = input(f"Ingrese el nuevo apellido paterno (actual: {cliente[3]}): ")
            cliente[3] = nuevo_valor
        elif campo == '4':
            nuevo_valor = input(f"Ingrese el nuevo apellido materno (actual: {cliente[4]}): ")
            cliente[4] = nuevo_valor
        elif campo == '5':
            nuevo_valor = input(f"Ingrese la nueva calle (actual: {cliente[5]}): ")
            cliente[5] = nuevo_valor
        elif campo == '6':
            nuevo_valor = input(f"Ingrese la nueva ciudad (actual: {cliente[6]}): ")
            cliente[6] = nuevo_valor
        elif campo == '7':
            nuevo_valor = input(f"Ingrese el nuevo código postal (actual: {cliente[7]}): ")
            cliente[7] = nuevo_valor
        elif campo == '8':
            nuevo_valor = input(f"Ingrese el nuevo teléfono (actual: {cliente[8]}): ")
            cliente[8] = nuevo_valor
        else:
            print("Opción no válida.")
            return

        # Llamar al método de la clase base para actualizar los datos del cliente
        return super().editar(id_cliente, campo, cliente)
    
    
    def eliminar_cliente(self):
        # Solicitar el ID del cliente a eliminar dentro del método
        id_cliente = input("Ingrese el ID del cliente a eliminar: ")
        return super().eliminar(id_cliente)
    
    def leer_cliente(self): 
        # Llamar al método 'leer' de la clase base con la ruta ya configurada
        clientes = super().leer('datos/clientes.csv')

        if clientes:
            print("Clientes leidos del CSV:")
            for cliente in clientes:
                print(cliente)
        else:
            print("No se encontraron mas clientes o el archivo esta vacio")
        
