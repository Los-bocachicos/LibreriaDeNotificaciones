import notifications_library

# Asocia un número con su tipo de notificador
number_notificator_association = {
    1: notifications_library.SMSNotificator,
    2: notifications_library.MailNotificator,
    3: notifications_library.FacebookNotificator,
    4: notifications_library.CompanyNotificator,
}

# Asocia un número con su nombre de tipo de notificador
number_notificator_name_association = {
    1: "SMS",
    2: "Email",
    3: "Facebook",
    4: "Empresarial",
}

# Muestra los tipos de notificador con su número
print("""
1. SMS
2. Email
3. Facebook
4. Empresarial

""")
notificators_type_raw = input("Elija los tipos de notificación.\nEscriba todos los números seleccionados sin ninguna separación:\n")

# Instancia el notificador
notificator = notifications_library.Notificator()

# Recorre todos los notificadores seleccionados, pide sus destinatarios y los agrega al notificador
for n in notificators_type_raw:
    receivers = input("Elija los destinatarios para {} separados por un espacio: ".format(number_notificator_name_association.get(int(n))))
    receivers = receivers.split(' ') # Convierte los destinatarios a una lista
    notificator_type = number_notificator_association.get(int(n))(receivers) # Instancia el tipo de notificador
    notificator.addNotificator(notificator_type) # Añade el notificador

message_raw = input("Esciba el mensaje a enviar: ")

# Envía el mensaje
notificator.send(message_raw)