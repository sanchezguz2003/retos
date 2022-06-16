
import reto_uno

reto_uno.calificaciones()
while True:
    condicion= input("¿desea hacer otro registro? (S=si N=no):")
    reto_uno.calificaciones()
    if condicion == "n" or condicion == "N":
        break
print("fin ")
