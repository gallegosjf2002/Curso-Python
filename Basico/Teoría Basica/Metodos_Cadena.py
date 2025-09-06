nombre_curso = "python"
cadena1 = nombre_curso.upper() # Convierte la cadena a mayúsculas
#print(cadena1)
nombre_curso = "PYTHON"
cadena2 = nombre_curso.lower() # Convierte la cadena a minúsculas
#print(cadena2)

mensaje = "       hola mundo       "
cadena3 = mensaje.strip()
#print(cadena3)  # Elimina los espacios en blanco al inicio y al final de la cadena

mensaje1 = "hola mundo"
cadena_buscar=mensaje1.find("mundo")  # Busca la subcadena "mundo" en mensaje1
#print(cadena_buscar)  # Devuelve la posición de la subcadena encontrada, o -1 si no se encuentra

cadena_buscar1 = mensaje1.index("mundo")  # Busca la subcadena "mundo" en mensaje1
#print(cadena_buscar1)  # Devuelve la posición de la subcadena encontrada, o lanza un error si no se encuentra

mensaje_bien = "Hola, mundo desde Python"
cadena_reemplarzar = mensaje_bien.replace("Python", "Java")  # Reemplaza "Python" por "Java"
#print(cadena_reemplarzar)  # Imprime la cadena con el reemplazo

palabra = ["manzana", "pera", "naranja"]

resultado = ", ".join(palabra)  # Une las palabras con una coma y un espacio
print(resultado)  # Imprime "manzana, pera, naranja"

