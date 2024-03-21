
def costo_total_salpicon(frutas):
    costo_total = sum(fruta['precio_unitario'] * fruta['cantidad'] for fruta in frutas)
    return costo_total


def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x['precio_unitario'], reverse=True)
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta['fruta_id']}, Nombre: {fruta['nombre']}, Precio Unitario: ${fruta['precio_unitario']}, Cantidad: {fruta['cantidad']}")


def fruta_mas_barata(frutas):
    fruta_barata = min(frutas, key=lambda x: x['precio_unitario'])
    print(f"\nLa fruta más barata es: {fruta_barata['nombre']}, con un precio unitario de ${fruta_barata['precio_unitario']}")


def main():
    frutas = []
    cantidad = int(input("Ingrese la cantidad de frutas: "))
    for i in range(cantidad):
        print(f"\nIngrese los detalles de la fruta {i+1}:")
        fruta_id = i + 1
        nombre = input("Nombre de la fruta: ")
        precio_unitario = float(input("Precio unitario de la fruta: "))
        cantidad_fruta = int(input("Cantidad de esta fruta: "))
        fruta = {'fruta_id': fruta_id, 'nombre': nombre, 'precio_unitario': precio_unitario, 'cantidad': cantidad_fruta}
        frutas.append(fruta)

    print(f"\nEl costo total del salpicón es: ${costo_total_salpicon(frutas)}")
    print("\nFrutas ordenadas de mayor a menor costo:")
    mostrar_frutas_ordenadas(frutas)
    fruta_mas_barata(frutas)


main()
