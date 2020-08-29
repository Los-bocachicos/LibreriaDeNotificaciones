class NotificationType:
    def __init__(self, receivers=[]):
        self.receivers = receivers

    def send(self, message: str):
        raise NotImplementedError


class MailNotificator(NotificationType):
    
    def send(self, message: str):
        print("Sending mail: {}. To: ".format(message), self.receivers)


class SMSNotificator(NotificationType):
    
    def send(self, message: str):
        print("Sending SMS: {} to: ".format(message), self.receivers)


class FacebookNotificator(NotificationType):

    def send(self, message: str):
        print("Sending Facebook: {} to: ".format(message), self.receivers)


class CompanyNotificator(NotificationType):

    def send(self, message: str):
        print("Sending Company: {} to: ".format(message), self.receivers)


class Notificator:
    def __init__(self, notificators=[]):
        self.notificators = notificators

    def addNotificator(self, notificador: NotificationType):
        self.notificators.append(notificador)

    def removeNotificator(self, notificador: NotificationType):
        self.notificators.remove(notificador)

    def send(self, message: str):
        for n in self.notificators:
            n.send(message)
