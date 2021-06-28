#'''Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa,
# sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble 
# de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que 
# se paga por una hora normal y el resto al triple'''
class Tarea7:
    def __init__(self):
        pass
    def calcularJornada(self):
         ht, he, het=0,0,0
         ph, phe, pt, ph8=0,0,0,0
         ht = int(input("Ingrese horas trabajadas: "))
         ph = float(input("Ingrese valor hora: "))
         if ht > 40:
             he = ht-40     
             if he > 8:
                 het = he-8
                 ph8 = 8*ph*2
                 ph8 =het*ph*3
             else:
                 ph8 = he*ph*2
             pt = 40*ph+phe+ph8
         else:
             pt = ht*ph
         print("Sobretiempo<8:{} Sobretiempo>8:{} Jornada:{} ".format(ph8,phe,pt))    
            
tarea = Tarea7()
tarea.calcularJornada()
            
            