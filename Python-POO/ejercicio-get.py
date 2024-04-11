#accediendo a atributos privados con get

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre= nombre
        self.__edad= edad
    
    #creamos la funcion get
    def get_nombre(self):
        return self.__nombre
    
yo= Persona("Nahuel", 21)

print(yo.get_nombre())