from models.Piso import *

pisos = []
opc = menu()
if(opc == 1):
    alta(pisos)


def menu():
    opc = len(input(
        "1.-Alta nuevo piso\n 2.-Listado ciudades\n 3.-Modificar precio\n 4.-Salir"))
    return opc


def alta(pisos):
    while True:
        respuesta = int(input("Quieres añadir un nuevo piso: 1->Si 2->No"))
        if respuesta == 1:
            piso = Piso(input("Codigo: "),
                        input("Poblacion: "),
                        int(input("Superficie: ")),
                        float(input("Precio: ")))
            pisos.append(piso)
        else:
            break
