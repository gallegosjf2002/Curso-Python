""" 
0001. Calcular el precio total de un producto con  IVA 
"""
PRECIO_PRODUCTO = 100.0  # Precio del producto sin IVA
IVA = 0.15 # Tasa de IVA
precio_con_iva = (PRECIO_PRODUCTO  + PRECIO_PRODUCTO*IVA )

print(f"El precio total del producto con IVA es: {precio_con_iva}, dolares")

""" Para un producto cualquiera"""
nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
IVA = 0.15 # Tasa de IVA
precio_con_iva = precio_producto + float(precio_producto)*float(IVA)
print(f"El precio total del {nombre_producto} con IVA es: {precio_con_iva:.2f} dolares")