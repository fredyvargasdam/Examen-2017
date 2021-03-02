from models.Piso import *

# Devuelve un numero entero con la eleccion del usuario


def menu():
    opc = int(input(
        "1.-Alta nuevo piso\n 2.-Listado ciudades\n 3.-Modificar precio\n 4.-Salir\n"))
    return opc

# Verificar si el codigo introducido ya se encuentra registrado


def codigo_registrado(pisos, piso):
    resultado = False
    for indice in range(len(pisos)):
        print(pisos[indice].get_codigo())
        print(piso.get_codigo())
        if pisos[indice].get_codigo() == piso.get_codigo():
            resultado = True
            break
    return resultado

# Alta de un nuevo piso


def alta(pisos):
    while True:
        respuesta = int(input("Quieres añadir un nuevo piso: 1->Si 2->No: "))
        if respuesta == 1:
            piso = Piso(input("Codigo: "),
                        input("Poblacion: "),
                        int(input("Superficie: ")),
                        float(input("Precio: ")))
            if codigo_registrado(pisos, piso):
                print("Lo sentimos mucho pero el piso ya se encuentra registrado.")
            else:
                pisos.append(piso)
        else:
            break

# Listar todos los pisos


def listado_ciudades(pisos):
    print("**********Listado de todos los pisos registrados*********")
    print(len(pisos))
    for indice in range(len(pisos)):
        pisos[indice].get_datos()

# Devuelve True si la ciudad ya se encuentra registrada


def ciudad_registrada(pisos, ciudad_selecionada):
    for indice in range(len(pisos)):
        if pisos[indice].get_poblacion() == ciudad_selecionada:
            return True

    return False

# Total de ciudades registrados


def total_ciudades(pisos, ciudad_selecionada):
    total = 0
    for indice in range(len(pisos)):
        if pisos[indice].get_poblacion() == ciudad_selecionada:
            total += 1
    return total

# Modificar el precio de los pisos de una determinada ciudad


def modificar_precio(pisos):
    ciudad_selecionada = input("Poblacion: ")
    total = 0

    if ciudad_registrada(pisos, ciudad_selecionada):
        total_pisos = total_ciudades(pisos, ciudad_selecionada)
        nuevo_precio = float(input("Porcentaje a subir: "))
        for indice in range(len(pisos)):
            if pisos[indice].get_poblacion() == ciudad_selecionada:
                pisos[indice].get_datos()
                modificar = int(
                    input("Desea modificar el precio de este piso 1->Si 2->No: "))
                if(modificar == 1):
                    nuevo_precio = (
                        nuevo_precio*pisos[indice].get_precio()/100) + float(pisos[indice].get_precio())
                    pisos[indice].set_precio(nuevo_precio)
                    total += 1

        print("Se han modificado " + str(total) + "de " + str(total_pisos))


# Main
pisos = []
while True:
    opc = menu()
    if(opc == 1):
        alta(pisos)
    elif(opc == 2):
        listado_ciudades(pisos)
    elif(opc == 3):
        modificar_precio(pisos)
    elif(opc == 4):
        break
