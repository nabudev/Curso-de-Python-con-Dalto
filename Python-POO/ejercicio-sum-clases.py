class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre= nombre
        self.fuerza= fuerza
        self.velocidad= velocidad
        
    def __repr__(self):
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})'
    
    def __add__(self, new_pj):
        nuevo_nombre= self.nombre + "-" + new_pj.nombre
        nueva_fuerza= round(((self.fuerza + new_pj.fuerza)/2)**1.3)
        nueva_velocidad= round(((self.velocidad + new_pj.velocidad)/2)**1.3)
        return Personaje (nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
goku= Personaje("Goku", 29, 57)
vegetta= Personaje("Vegetta", 23, 43)
#podemos seguir creando objetos y sumandolos
gogeta= goku + vegetta
print(gogeta)

