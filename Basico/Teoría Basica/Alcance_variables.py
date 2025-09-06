
""" Alcance Local

def my_function():
    x = 10  # Variable local
    print("Valor de x dentro de la función:", x)
    
# Llamada a la función
my_function()

"""

""" Alcance Global
global_var=120
def my_var():
    print(global_var)  # Acceso a la variable global
    

my_var()  # Llamada a la función que imprime la variable global
"""
""" Alcance Global y Local"""
COUNT = 0
def my_funcion_3():
    global COUNT  # Declaramos que vamos a usar la variable global COUNT
    COUNT += 1  # Incrementamos el valor de COUNT
    print("Valor de COUNT dentro de la función:", COUNT)

my_funcion_3()  # Llamada a la función que incrementa COUNT

