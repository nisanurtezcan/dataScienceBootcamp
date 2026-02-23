class Notification():
    def __init__(self, message):
        self.message = message
    def send(self):
        return "."

class EmailNotification(Notification):
    def __init__(self, message):
        super().__init__(message)  # parent'ın __init__'i
    def send(self):
        return f"Email sent: {self.message}"


class SMSNotification(Notification):
    def __init__(self, message):
        super().__init__(message)  # parent'ın __init__'i
    def send(self):
        return f"SMS sent: {self.message}"
