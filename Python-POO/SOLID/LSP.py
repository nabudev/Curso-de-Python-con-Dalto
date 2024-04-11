#basicamente implica que las clases derivadas puedan ser sustituibles por sus clases principales
#class Ave:
#    def volar(self):
#        return "Estoy volando"
    
#class Pinguino(Ave):
#    def volar(self):
#        return "no puedo volar xd"

#def hacer_volar(ave = Ave):
#    return ave.volar()

#aqui hay un problema porque estamos NO pudiendo aplicar en una subclase lo de la clase padre
#print(hacer_volar(Pinguino()))
#output: no puedo volar xd

#el metodo correcto, aplicando LSP seria:
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"

class AveNoVoladora (Ave):
    pass

#basicamente se trata de que la clase padre tenga todo lo que cualquier ave pueda realizar y a partir de la necesidad ir creando las variantes de aves pero que puedan utilizar metodos de la clase principal Ave
