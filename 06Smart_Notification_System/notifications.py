class Notification:
    def __init__(self, message, created_at):
        self.message = message
        self.created_at = created_at
        if self.message.strip() == "":
            raise ValueError("No empty message allowed")  
    def __str__(self): 
        return f"Notification: {self.message}"

class EmailNotification(Notification):
    def send(self):
        print(f"Email is sent: {self.message}")

class SMSNotification(Notification):
    def send(self):
        print(f"SMS is sent: {self.message}")

class PushNotification(Notification):
    def send(self):
        print(f"Push notification is sent: {self.message}")


