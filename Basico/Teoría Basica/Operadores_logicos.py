""" 
Operadores relacionales
Este módulo define una clase `OperadoresLogicos` que contiene métodos para realizar operaciones lógicas básicas:
- Igualdad: a == b
- Desigualdad: a != b
- Mayor que: a > b
- Menor que: a < b
- Mayor o igual que: a >= b
- Menor o igual que: a <= b

Operadores lógicos
Este módulo define una clase `OperadoresLogicos` que contiene métodos para realizar operaciones lógicas básicas:
- AND: a and b // True si ambos son verdaderos
- OR: a or b // True si al menos uno es verdadero
- NOT: not a // Invierte el valor de verdad de a

"""
# Igualdad
nombre_persona = "Juan"
nombre_empleado = "Juan"

respuesta= nombre_persona == nombre_empleado  # True si son iguales, False si son diferentes
#print(respuesta) #True porque la comparación es sensible a mayúsculas y minúsculas

# Desigualdad
loggin_usuario = False

respuesta2=  True != loggin_usuario  # True si son diferentes, False si son iguales
#print(respuesta2) #True porque son diferentes

# And

licencia= True
edad = 16  
puede_conducir = licencia and (edad >= 18)  # True si ambos son verdaderos
#print(puede_conducir)  # True porque licencia es True y edad es mayor

# or

licencia= True
edad = 16  
puede_conducir = licencia or (edad >= 18)  # True si uno es verdaderos
#print(puede_conducir)  # True porque licencia es True y edad es mayor

"""EJEMPLO"""
a=10
b=20
c=10

print(a == b)  # False, porque 10 no es igual a 20
print(a == c)  # True, porque 10 es igual a 10
print(a != b)  # True, porque 10 es diferente de 20
print(a > b)   # False, porque 10 no es mayor que 20
print(a < b)   # True, porque 10 es menor que 20
print(a >= c)  # True, porque 10 es mayor o igual a 10
print(a <= c)  # True, porque 10 es menor o igual a 10
print(a < b and a == c)  # True, porque 10 es menor que 20 y 10 es igual a 10
print(a < b or a == c)   # True, porque 10 es menor que
