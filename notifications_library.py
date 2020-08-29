class NotificationType:
    def __init__(self, receivers=[]):
        self.receivers = receivers

    def send(self, message: str):
        raise NotImplementedError


class MailNotificator(NotificationType):
    
    def send(self, message: str):
        print("Enviando Email: {}. To: ".format(message), self.receivers)


class SMSNotificator(NotificationType):
    
    def send(self, message: str):
        print("Enviando SMS: {} to: ".format(message), self.receivers)


class FacebookNotificator(NotificationType):

    def send(self, message: str):
        print("Enviando Facebook: {} to: ".format(message), self.receivers)


class CompanyNotificator(NotificationType):

    def send(self, message: str):
        print("Enviando Empresarial: {} to: ".format(message), self.receivers)


class Notificator:
    def __init__(self, notificators=[]):
        self.notificators = notificators

    def addNotificator(self, notificator: NotificationType):
        """
         Añade un tipo de notificador a la lista
        """
        self.notificators.append(notificator)

    def removeNotificator(self, notificator: NotificationType):
        """
         Elimina un tipo de notificador de la lista
        """
        self.notificators.remove(notificator)

    def send(self, message: str):
        """
         Envia el mensaje a todos los tipos de notificador de la lista
        """
        for n in self.notificators:
            n.send(message)
