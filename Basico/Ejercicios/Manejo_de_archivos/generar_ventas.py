""" Sistema de registro de ventas
- Guardar cada venta con detlles de producto, cantidad y precio.
en un archivo de texto.
-Mostrar en un reporte
-Cada vez que se realice una venta, registarlo en el archivo "Ventas.txt


"""
def registrar_venta(producto, cantidad, precio):
    with open("Ventas.txt", "a") as archivo:  #a para agregar al final del archivo
        total = cantidad * precio
        archivo.write(f"Producto: {producto}, Cantidad: {cantidad}, Precio: {precio}, Total: {total} \n" )
    print(f"Venta registrada: {producto}, {cantidad} unidades ,${precio} cada una, Total: {total:.2f}")


registrar_venta("Lapiz", 3, 0.50)
registrar_venta("Cuaderno", 2, 1.50)
registrar_venta("Borrador", 5, 0.25)
registrar_venta("Lapiz", 3, 0.50)
registrar_venta("Cuaderno", 2, 1.50)
registrar_venta("Borrador", 5, 0.25)
registrar_venta("Lapiz", 3, 0.50)
registrar_venta("Cuaderno", 2, 1.50)
registrar_venta("Borrador", 5, 0.25)














