edad_persona = 22 #int 
nombre_producto = "Pantalon" #str
unidad = 1 #int
precio = 12.09781612891 #float
existencia = True #/False #bool

""" Concatenar"""
#Forma 1: Usando el operador +
cadena = nombre_producto + str(unidad) 
cadena2= str(precio)
tipo_dato = type(cadena2)
#print(type(cadena2)) #No es recomendable usarlo, ya que puede generar errores si no se convierte correctamente

#Forma 2: Usando print

#print(nombre_producto, precio) #Solo se necesita una coma para concatenar

#Forma 3: Usando una cadena formateada (f-string)

#print(f"Producto: {nombre_producto}, Precio: {round(precio,2)}") #f-string

""" Converitr a otro tpo de datos"""
total_prducto = "1900"
precio_1 = 10
cadena3 = int(total_prducto) * precio_1
#print(cadena3)  # Resultado: 19000

#Control de decimales
#Caso 1: Usando round
#print(f"Producto: {nombre_producto}, Precio: {round(precio,2)}") #Usamos round(var,numero de decimales) para controlar los decimales

#Caso 2: Usando format
print("Producto: {}, Precio: {:.2f}".format(nombre_producto, precio)) #Usamos format para controlar los decimales