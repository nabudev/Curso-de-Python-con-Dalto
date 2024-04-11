#Se refiere a la forma de programar para que en un futuro, al querer agregar funcionalidades no tengamos que alterar el codigo existente.
#Creo un pequeño programita de notificaciones, con la particularidad de que puedo agregar varios medios para notificar (OCP)

class Notificador():
    def __init__(self, usuario, mensaje):
        self.usuario= usuario
        self.mensaje= mensaje
    
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por email a {self.usuario}")

class NotificarSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario}")
        
#puedo seguir agregando metodos de notificar, por ejemplo whatsapp
#de esta manera, creamos funcionalidades sin modificar la clase principal
