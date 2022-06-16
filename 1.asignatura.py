def asignatura():
    print(input("introduzca el nombre de la asignatura"))

def calificaciones():
    asig=input("introduzca el nombre de la asignatura")
    cali=int(input("introduce los cuatro calificaciones"))
    c1 = int(input("introduce el primer calificacion:"))
    c2 = int(input("introduce la segunda calificacion:"))
    c3 = int(input("introduce la tercera calificacion:"))
    c4 = int(input("introduce la cuarta calificacion:"))
    prom=(c1+c2+c3+c4)/4
    mensaje=None
    if 70 <=prom<= 100:
        mensaje="aprobado"
    else:
        mensaje="advertencia"
    print(f"nombre de la asignatura: {asig},promedio",{prom},mensaje)

