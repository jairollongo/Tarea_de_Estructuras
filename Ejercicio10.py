#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2.
#El aspirante que obtenga calificaciones mayores que 80 en ambos examenes es aceptado; caso contrario es rechazado.

class ejercicio10:
    def __init__(self):
        pass
    def variabes(self):
        C1:float(input("Ingrese calificacion1:" ))
        C2:float(input("Ingrese calificacion2: "))
        if(C1 >= 80) and (C2 >=80):
            print("aceptado")
        else:
            print("rechazado")
       
        
    
