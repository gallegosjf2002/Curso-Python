""" Crear un programa que determine si un numero es par o impar
numero = float((input("Ingrese el número: ")))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")


"""


""" Aplicar un descuento a un producto dependiendo de su precio

"""
nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el valor del precio: "))

if precio_producto >= 100:
    descuento = precio_producto * 0.10
    precio_nuevo = precio_producto - descuento
    print(f"El precio de {nombre_producto} tiene un descuento del 10%, entonces el precio es de {precio_nuevo:.2f} ")
elif 50 <= precio_producto < 100:
    descuento = precio_producto * 0.05
    precio_nuevo = precio_producto - descuento
    print(f"El precio de {nombre_producto} tiene un descuento del 5%, entonces el precio es de {precio_nuevo:.2f} ")
else:
    print(f"No es agreedor a ningun descuento, el producto {nombre_producto} tiene un precio de {precio_producto:.2f}")



