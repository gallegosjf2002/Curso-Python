""" 
if condition:
    pass
elif
    pass

x =float(((12+15)*5 - (3*4)**2)*(1.2))
if x > 0:
    print(f"x es postivo: {x}")
elif x < 0:
    print(f"x es negativo: {x}")
elif x == 0:
    print("x es cero")

x=-5
y=20
if x > 0:
    if y > 0:
        print("x y son positivos")
    else:
        print("x es positivo, y no lo es")
else:
    if y > 0:
        print("x no es positivo, y lo es")
    else:
        print("x y no son positivos")
        
x=-5
y=-15

if x > 0 or y > 0:
    print("Al menos uno de los números es positivo")
else:
    print("Ninguno de los números es positivo")

###################################################################################################
punt_obt= float(input("Ingrese la cantidad de puntos obtenidos: "))
if punt_obt >= 90:
    print("Aprobado con distinción")
elif punt_obt >= 75 and punt_obt < 90:
    print("Aprobado")
elif punt_obt < 75:
    print("Reprobado")
""" 

nota1=float(input("Ingrese la nota del primer examen: "))
nota2=float(input("Ingrese la nota del segundo examen: "))
nota3=float(input("Ingrese la nota del tercer examen: "))
promedio=(nota1+nota2+nota3)/3
if promedio >= 9.00:
    print(f"Aprobado con distinción {promedio:.2f}")
elif promedio >= 7.5:
    print(f"Aprobado con la nota {promedio:.2f}")  
else:
    print(f"Reprobado con la nota {promedio:.2f}")
    nota_sus=float(input("Ingrese la nota del examen de recuperación: "))
    promedio=(promedio+nota_sus)/2
    if promedio >= 7.5:
        print("Aprobado")
    else:
        print("Reprobado, repetir el curso")






