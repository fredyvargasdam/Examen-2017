class Piso:
    def __init__(self, codigo, poblacion, superficie, precio):
        self.__codigo = codigo
        self.__precio = precio
        self.__poblacion = poblacion
        self.__superficie = superficie

    def set_precio(self, precio):
        self.__precio = precio

    def get_datos(self):
        print("Piso: " + self.__codigo +
              "Población: " + self.__poblacion +
              "Precio: " + str(self.__precio) +
              "Superficie: " + str(self.__superficie))

    def get_poblacion(self):
        return self.__poblacion

    def get_precio(self):
        return self.__precio

    def get_codigo(self):
        return self.__codigo
