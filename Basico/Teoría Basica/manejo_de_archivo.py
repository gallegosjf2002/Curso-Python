""" 
'r': Modo lectura (read), por defecto
'w': Modo escritura (write), crea el archivo si no existe o lo trunca si ya existe
'a': Modo adición (append), agrega contenido al final del archivo, crea el archivo si no existe
'b': Modo binario, se usa junto con otros modos para manejar archivos binarios, por ejemplo, 'rb' para leer en binario o 'wb' para escribir en binario
'x': Modo exclusivo de creación (exclusive creation), crea un nuevo archivo, falla si el archivo ya existe
't': Modo texto (text), por defecto, se usa para manejar archivos de texto, por ejemplo, 'rt' para leer en texto o 'wt' para escribir en texto


Ejemplos:
with open("Basico\información.txt", 'r', encoding='utf-8') as file:
    contenido = file.read()
    print(contenido) 
"""


with open("Nueva_info.txt", "w", encoding='utf-8') as file:
    file.write("Esta es una nueva línea de información.\n")
    file.write("Agregando más contenido al archivo.\n")






