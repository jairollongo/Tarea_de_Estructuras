#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero,
# obtenga el resultado de la siguiente función:
class ejercicio9:
    def __init__(self):
        pass
    def Variables(self):
        num = float(input("Ingrese primera variable" ))
        V = float(input("Ingrese segunda variable" ))
        print()
        if num==1:
            resp=(100*V)
        elif num == 2:
            resp=pow(100^V)
        elif num == 3:
            resp=(100/V)
        else:
            resp=0
        print("Su resultado es: ", resp)
        print()
            
resultado = ejercicio9()
resultado.Variables() 

        
                
