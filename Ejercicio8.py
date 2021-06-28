#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

class ejercicio8:
    def __init__(self):
        pass
    def NumMayor(self):
        print("")
        n1 = int(input("Ingrese primer numero entero: "))
        n2 = int(input("Ingrese segudo numero entero: "))
        n3 = int(input("Ingrese tercer numero entero: "))
        print()
        if n1 > n2 and n1 > n3:
            nM = n1
        else:
            if n2 > n3:
                nM = n2
            else:
                nM = n3
        print("El numero mayor es:", nM)
        print()
        
ejercicio = ejercicio8()
ejercicio.NumMayor()            
               