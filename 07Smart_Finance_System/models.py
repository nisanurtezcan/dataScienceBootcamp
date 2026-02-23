from datetime import date

class Expense():
    def __init__(self, amount, category, date=date.today()):
        self.amount = float(amount)
        self.category = category
        self.date = date

    def __str__(self):
        return f"Amount: {self.amount}, Category: {self.category}, Date: {self.date}"


class Budget():
    def __init__(self, limit):
        self.limit = float(limit)
        self.expenses = [] 

    def add_expense(self, expense):
        self.expenses.append(expense)  

    def total_expense(self):
        return sum(expense.amount for expense in self.expenses)  

    def average_expense(self):
        if len(self.expenses) != 0:
            return self.total_expense() / len(self.expenses) 

    def is_limit_exceeded(self):
        if self.total_expense() > self.limit:
            print("Limit exceeded")
            return True 
        else:
            print("Limit is not exceeded")
            return False