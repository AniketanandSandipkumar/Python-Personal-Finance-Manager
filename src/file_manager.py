import csv
import os
from src.expense import Expense

def load_expenses(filename="data/expenses.csv"):
    expenses = []

    if not os.path.exists(filename):
        return expenses

    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expense = Expense(
                amount=row["Amount"],
                category=row["Category"],
                date=row["Date"],
                description=row["Description"]
            )
            expenses.append(expense)

    return expenses

def save_expenses(expenses, filename="data/expenses.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

        for expense in expenses:
            writer.writerow(expense.to_list())

def backup_data(source="data/expenses.csv", backup="data/expenses_backup.csv"):
    if not os.path.exists(source):
        raise FileNotFoundError("No data file found to backup.")

    with open(source, "r", encoding="utf-8") as src, open(backup, "w", encoding="utf-8") as bk:
        bk.write(src.read())

def restore_data(backup="data/expenses_backup.csv", target="data/expenses.csv"):
    if not os.path.exists(backup):
        raise FileNotFoundError("No backup file found.")

    with open(backup, "r", encoding="utf-8") as bk, open(target, "w", encoding="utf-8") as tgt:
        tgt.write(bk.read())
