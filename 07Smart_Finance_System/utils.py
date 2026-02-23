from models import Expense
from datetime import date
import random

def get_user_expenses():
    expenses = []
    categories = []
    while True:
        expense_input = input("Enter the expense (0 to stop): ")
        if expense_input == "0":
            break
        try:
            expense = int(expense_input)
            category = input("Enter its category: ")
            expenses.append(expense)
            categories.append(category)
        except ValueError:
            print("Please enter the values properly.")

    return expenses, categories

    


def generate_random_notification():
    notificationList = [
        "You are approaching your spending limit!",
        "You’ve spent a lot this month!",
        "Check your budget"
    ]
    return f"{random.choice(notificationList)} - Sent: {date.today()}"

