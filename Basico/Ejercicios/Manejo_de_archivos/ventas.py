def mostrar_reportes_ventas():
    print("Reporte de ventas del dia:")
    try:
        with open("Ventas.txt", "r") as archivo:
            contenido = archivo.readlines() # Lee todas las lineas del archivo
            if contenido:
                for linea in contenido:
                    print(linea.strip())
            else:
                print("No hay el archvo de ventas")
    except FileNotFoundError:
        print("El archivo no existe. Asegúrate de haber registrado ventas antes de generar el reporte.")

mostrar_reportes_ventas()
