from controllers.producto_controller import ProductoController

def seleccionar_opcion():
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("Opción inválida. Por favor, elige entre 1, 2 o 3.")


def mostrar_menu():
    controller = ProductoController()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad en inventario: "))
            controller.agregar_producto(nombre, precio, cantidad)
        elif opcion == "2":
            productos = controller.listar_productos()
            for producto in productos:
                print(producto)
        elif opcion == "3":
            controller.cerrar()
            break
        else:
            print("Opción inválida. Intente de nuevo.")
