class MiClase():
    def __init__(self):
        #Atributo privado: usar _
        #Atributo muy privado: usar __
        #la forma de darle a entender a python que le estamos pasando un atributo privado es self."_"
        self.__atributo_privado= "valor"
        
        
objeto = MiClase()

print(objeto.__atributo_privado)
