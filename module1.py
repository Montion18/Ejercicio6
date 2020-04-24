from FECHAHORA import FechaHora
def op0():
    print("Saliendo")
def op1(a,b):
    print("Opcion 1: \n")
    suma=hora1+hora2
    test.AdelantarHora(suma)
    test.Mostrar()
    print("---------------------")

def op2(a,b):
    print("Opcion2: \n")
    resta=hora1-hora2
    test.AdelantarHora(resta)
    test.Mostrar()
    print("---------------------")
   


def op3(a,b):
    print("Opcion3: \n")
    comparacion=hora1>hora2
    if comparacion==True:
        print("El mayor es %d\n" % a)
    else: print("El mayor es %d\n" % b)
    print("---------------------")


switcher= {
    0:op0,
    1:op1,
    2:op2,  
    3:op3      
    }
def switch(op,a,b):
    func=switcher.get(op,lambda: print("opcion incorrecta"))
    func(a,b)

if __name__ == '__main__':
    bandera=False
    a=int(input("Ingrese la primera hora: "))
    b=int(input("Ingrese la segunda hora: "))
    while a>24 or b>24:
        a=int(input("Ingrese la primera hora en formato 24 horas: "))
        b=int(input("Ingrese la segunda hora en formato 24 horas: "))
    hora1=FechaHora(1,1,2020,a,0,0)
    hora2=FechaHora(1,1,2020,b,0,0)
    test=FechaHora(1,1,2020,0,0,0)
        
    while not bandera:
        print("1.Sumar hora\n")
        print("2.Restar hora\n")
        print("3.Distingir mayor\n")
        op=int(input("SELECCIONE UNA OPCION\n"))
        switch(op,a,b)
        bandera=int(op)==0


