class Persona():
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    
    #metodos especiales
    
    def __str__(self):
        return f'Persona(nombre= {self.nombre}, edad= {self.edad})'
    
    def __repr__ (self):
        return f'Persona ("{self.nombre}", {self.edad})'
    
    def __add__(self, otro):
        nuevo_valor= self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)
    
nahuel= Persona("nahuel", 21)
gabi= Persona("gabigol", 21)
jere= Persona("jerex", 21)

nueva_persona= nahuel + gabi + jere
print(nueva_persona.edad)