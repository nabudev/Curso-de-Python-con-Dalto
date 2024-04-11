class Persona:
    def __init__(self, nombre, edad):
        self.__nombre= nombre
        self.__edad= edad
    
    #creamos la funcion get
    def get_nombre(self):
        return self.__nombre
    
    #creamos la funcion set
    def set_nombre(self, new_nombre):
        self.__nombre= new_nombre
    
yo= Persona ("Nahuel", 21)

nombre= yo.get_nombre()                      #lo que hacemos aqui es basicamente crear el objeto con sus parametros,
print(nombre)                                #con get sacamos el nombre, con set lo modificamos y con get nuevamente sacamos el nombre nuevo

yo.set_nombre("Alberto")

nombre= yo.get_nombre()
print(nombre)

