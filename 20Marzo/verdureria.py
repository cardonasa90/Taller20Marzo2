import random

productos = []

def generar_id():
    return random.randint(1, 100)

def registrar_producto():
    producto = {}
    producto["id"] = generar_id()
    producto["nombre"] = input("Nombre del producto: ")
    producto["precio_unitario"] = float(input("Precio unitario del producto: "))
    producto["ubicacion"] = input("Ubicación en la tienda (A, B, C, D): ").upper()
    producto["descripcion"] = input("Descripción del producto: ")
    producto["casa"] = input("De que finca proviene? (Boyaca,Pasto,Guajira): ")
    producto["referencia"] = input("Referencia (código alfanumérico): ")
    producto["pais_origen"] = input("Departamento de Origen del producto: ")
    producto["unidades_compradas"] = int(input("Número de unidades compradas del producto: "))
    producto["garantia_extendida"] = input("¿Producto con garantía extendida? (True/False): ").lower() == "true"
    productos.append(producto)

def mostrar_productos_bodega():
    print("Productos en bodega:")
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio unitario: {producto['precio_unitario']}, Descripción: {producto['descripcion']}")

def buscar_producto_por_nombre():
    nombre_buscado = input("Nombre del producto a buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio unitario: {producto['precio_unitario']}, Descripción: {producto['descripcion']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

def modificar_unidades_compradas():
    nombre_buscado = input("Nombre del producto a modificar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            nuevas_unidades = int(input("Nuevo número de unidades compradas: "))
            if nuevas_unidades <= producto["unidades_compradas"]:
                producto["unidades_compradas"] = nuevas_unidades
                print("Unidades modificadas exitosamente.")
            else:
                print("Error: El nuevo número de unidades compradas no puede ser mayor al número inicial.")
            return
    print("Producto no encontrado.")

def eliminar_producto_por_nombre():
    nombre_buscado = input("Nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            confirmacion = input(f"¿Estás seguro de eliminar el producto '{producto['nombre']}'? (Sí/No): ").lower()
            if confirmacion == "si" or confirmacion == "s":
                productos.remove(producto)
                print("Producto eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return
    print("Producto no encontrado.")

opcion = 100
while opcion != 6:
    print("\n***Administrador de Stop de verduras ***")
    print("1. Registrar Producto")
    print("2. Mostrar Productos en Bodega")
    print("3. Buscar Producto por Nombre")
    print("4. Modificar Unidades Compradas de un Producto")
    print("5. Eliminar Producto por Nombre")
    print("6. Finalizar")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        mostrar_productos_bodega()
    elif opcion == 3:
        buscar_producto_por_nombre()
    elif opcion == 4:
        modificar_unidades_compradas()
    elif opcion == 5:
        eliminar_producto_por_nombre()
    elif opcion == 6:
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
