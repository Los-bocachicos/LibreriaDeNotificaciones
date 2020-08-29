import notifications_library

sms_receivers = ["3148152196"]
facebook_receivers = ["elias", "carlos"]

sms_notificator = notifications_library.SMSNotificator(sms_receivers)
facebook_notificator = notifications_library.FacebookNotificator(facebook_receivers)

notificator = notifications_library.Notificator([sms_notificator, facebook_notificator])

notificator.send("Hola")