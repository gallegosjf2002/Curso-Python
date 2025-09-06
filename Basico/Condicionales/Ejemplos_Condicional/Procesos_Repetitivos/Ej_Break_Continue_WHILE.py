""" 
Hasta que ingrese el numero "0" salir del programa
"""


""" while True:
    numero = float(input("Introduzca un numero (0 para salir)= "))
    if numero == 0:
        break
    print(f"Ingresate {numero}")

"""


""" 
Solicitar numeros al usuario pero si el numero es negativo se ignora
"""
while True:
    numero = float(input("Introduce un numero positivo: "))
    if numero <0:
        print(f"El numero es negativo {numero}")
        continue
    if numero ==0:
        print("Saliendo del cuble...")
        break

















