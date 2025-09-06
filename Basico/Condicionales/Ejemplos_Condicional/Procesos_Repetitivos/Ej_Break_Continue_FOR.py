""" Buscamos un numero en una lista
"""
""" 
numeros = [1, 2 , 3 , 4 ,  5 , 6 , 7 , 8 , 11, 12, 23 , 34 , 455 , 423 , 45]

objectic=int(input("Ingrese el onjetivo: "))
for numero in numeros:
    if numero == objectic:
        print(f"Numero {objectic} encontrado")
        break
else:
    print("No existe ese numero en la lsita")"""
    
    
""" Ejemplo con CONTINUE

Imprime los numeros de una lista, pero salta los numeros pares
"""
numeros =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)



