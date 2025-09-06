"""
Ejemplos varios de delaración de variables en Python.
"""
# asignacion simple

nombre = "Juan"
apellido = "Pérez"
edad = 30
sueldo = 2500.50
act_trabajo = True

# asignacion multiple

cant_prod,msj_bienv,estado = 10, "Producto enviado correctamente", True
#print(msj_bienv)
#print(cant_prod)

# Asignación el mismo valor a varias variables

x = i = z = 10
#print(x)
#print(i)
#print(z)

# Tipos de datos especiales (Estructura de datos)


"""
Listas (List)
Diccionariosn ()
Tuplas
Conjuntos
"""

cursos = ["Python", "Django", "Flask", ["Fastapi", "Pandas"], 20, 130, 150] #list {Elemento0, Elemento1, Elemento2} puede ser de n dimension
# Lista de dato immutable o mutable
#añadir elemento al finald de la lista
cursos.append("JavaScript") # Añadir un elemento al final de la lista

# Diccionario (dict) - Colección de pares clave-valor
empleado = {"Codigo":"200",    "Nombre":"Juan",    "Apellido":"Pérez"} #dict; Conjunto de datos mutable

#print(empleado["Codigo"]) # Acceso a un valor por su clave

# Tupla (tuple) - Colección ordenada e inmutable"

valores = (1, 2, 3, 4, 5) #tuple; Conjunto de datos inmutable
#valores.append(20) #No hay como añadir un elemento a una tupla, ya que es inmutable

# Conjunto (set) - Colección no ordenada de elementos únicos
numeros = {45,6,18,75, 55} #set; Conjunto de datos inmutable
#print(numeros)

