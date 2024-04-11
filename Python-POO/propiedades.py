class Persona:
    def __init__(self, nombre, edad):
        self.__nombre= nombre
        self._edad= edad
      
      
    #creamos un property para poder acceder al valor protegido    
    @property
    def nombre(self):
        return self.__nombre
    
    
    #creamos un setter para poder modificar el valor protegido
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre= new_nombre
        
    #para eliminar valores
    @nombre.deleter
    def nombre(self):
        del self.__nombre
        
        
nabu= Persona("Nahuel", 21)

nombre= nabu.nombre
print(nombre)

#agarro el valor de la variable nombre, lo modifico y lo muestro
nabu.nombre= "nabu"
nombre= nabu.nombre
print(nombre)

#eliminando el nombre nabu 
del nabu.nombre

print("hola")
