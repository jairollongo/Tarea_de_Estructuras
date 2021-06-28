#En una tienda se ofrece un descuento del 15% sobre el total de la compra y
# un cliente desea saber cuánto deberá pagar finalmente por su compra.
'''Ejercicio2'''
class Tarea:
    def __init__(self):
        pass
def ejecutar():
    TC = float(input("Ingrese total de la compra: "))
    D = TC*0.15
    CP = TC - D
    print("Su cantidad a pagar es: ")
    print (CP,"$")

ejecutar()
     
    