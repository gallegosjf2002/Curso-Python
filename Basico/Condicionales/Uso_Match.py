""" status=input("Ingrese el codigo status: ")
if status == "200":
    print("Solicitud exitosa")
elif status == "444":
    print("El recurso no fue encontrado")
elif status == "500":
    print("Error interno del server")
else:
    print("No valido")

"""

status=int(input("Ingrese el codigo del status: "))
match status:
    case 200:
        print("Solicitud exitosa")
    case 444 | 403 | 407: # | significa or
        print("El recurso no fue encontrado")
    case 500:
        print("Error interno del server")
    case _:
        print("No valido")



