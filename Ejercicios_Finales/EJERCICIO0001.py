""" Escribir un algoritmo que calcule la propina y el valor total a pagar con el iva de un restaurante"""
def name(precio, propina):
    IVA=0.12
    total = precio + (precio*IVA) + propina
    return total

precio = float(input("Ingrese el valor de su consumo=> "))
propina = float(input("Ingrese el valor de su propina=> "))
valor_total = name(precio, propina)

print(f"El valor de total de su consumo es {valor_total:.2f}")
with open("Ventas_restaurante.txt", "a", encoding='utf-8') as file:
    file.write(f"El valor de total de su consumo es {valor_total:.2f} \n")
    
