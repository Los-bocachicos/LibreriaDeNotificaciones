class TipoNotificacion:
    def __init__(self, destinatarios=[]):
        self.destinatarios = destinatarios

    def send(self, mensaje: str):
        raise NotImplementedError


class NotificadorCorreo(TipoNotificacion):
    
    def send(self, mensaje: str):
        print("Enviando Email: {}. To: ".format(mensaje), self.destinatarios)


class NotificadorSMS(TipoNotificacion):
    
    def send(self, mensaje: str):
        print("Enviando SMS: {} to: ".format(mensaje), self.destinatarios)


class NotificadorFacebook(TipoNotificacion):

    def send(self, mensaje: str):
        print("Enviando Facebook: {} to: ".format(mensaje), self.destinatarios)


class NotificadorEmpresa(TipoNotificacion):

    def send(self, mensaje: str):
        print("Enviando Empresarial: {} to: ".format(mensaje), self.destinatarios)


class Notificador:
    """
    
     1: Correo,
     2: Facebook,
     3: SMS,
     4: Empresa
    """
    def __init__(self, notificadores={}):
        fabrica = FabricaNotificadores()
        self.notificadores = fabrica.crearNotificadores(notificadores)

    def send(self, mensaje: str):
        """
         Envia el mensaje a todos los tipos de notificador de la lista
        """
        for n in self.notificadores:
            n.send(mensaje)


class FabricaNotificadores:

    def __init__(self):
        self.notificadoresExistentes = [NotificadorCorreo, NotificadorFacebook, NotificadorSMS, NotificadorEmpresa]

    def crearNotificadores(self, notificadores: {}) -> []:
        notificadoresCreados = []
        for key in notificadores.keys():
            destinatarios = notificadores.get(key)
            notificadorNuevo = self.notificadoresExistentes[key](destinatarios)
            notificadoresCreados.append(notificadorNuevo)
        return notificadoresCreados