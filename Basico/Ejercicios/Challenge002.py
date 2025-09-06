""" 
Calcular el salario semanal de un empleado considerando las horas trabajadas y el pago por hora.    


"""
# Definición de constantes
nombre_empleado = input("Ingrese el nombre del empleado: ")
horas_trabajadas = int(input("Ingrese las horas trabajadas en la semana: "))
PAGO_HORA = 10 # Pago por hora
# Cálculo del salario semanal
salario = horas_trabajadas * PAGO_HORA
# Impresión del resultado   
print(f"El salario semanal de {nombre_empleado} es de {salario} dolares")