def decorador(funcion):
    def funcion_modificada():
        print("Hola Mundo")
        funcion()
    return funcion_modificada

@decorador
def saludo():
    print("Hola Nahuel")
    
saludo()