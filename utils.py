import random
from datetime import datetime

myMessages = ["Hello!", "This is an important notification.", "Weather condition notification"]


def create_message():
    return random.choice(myMessages)

def get_time():
    return datetime.now()