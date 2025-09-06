nombre_curso = "Python para principiantes"
precio_curso = 29.99
horas_curso = 10
estado_curso = True


#print("Hello mundo, desde Python")
#print("Mi nombre es: ", "Juan")
cadena = f"El curso es {nombre_curso} el precio es {precio_curso} y dura {horas_curso} horas"


#print("El curso es ", nombre_curso," el precio es ", precio_curso, " y tiene una duracion de ", horas_curso, " horas")

#print(cadena)

""" Funcion input
nombre = input("Ingrese su nombre: ")"
frase = input("Ingrese una frase: ") #Ingresa en string, siempre devuelve un string
print(f"La frase ingresada es: {frase}")
print(f"El tipo de dato de la frase es:{type(frase)}")
numero = int(input("Ingrese un numero: ")) #Ingresa en int
print(f"El numero ingresado es: {numero}")
print(f"El tipo de dato del número es: {type(numero)}")
numero_decimal = float(input("Ingrese un numero decimal: ")) #Ingresa en float
print(f"El numero decimal ingresado es: {numero_decimal}")
print(f"El tipo de dato del número decimal es_ {type(numero_decimal)}")
"""
""" Función format
sintaxis:
"cadena de texto {}".format(valor)
"""

nombre_usuario= "Juan"
saludo = "Hola, {}".format(nombre_usuario)

print(saludo)

CONST = 3.1415916
cadena_constante = "El valor de la constante es: {:.4f}".format(CONST)
print(cadena_constante)