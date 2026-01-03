from collections import defaultdict
from src.expense import Expense
from src.utils import (
    get_valid_input,
    validate_amount,
    validate_date,
    validate_category
)

def add_expense(expenses):
    print("\nADD NEW EXPENSE")

    amount = get_valid_input("Enter amount: ", validate_amount)
    category = get_valid_input(
        "Enter category (Food/Transport/Entertainment/Shopping/Other): ",
        validate_category
    )
    date = get_valid_input("Enter date (YYYY-MM-DD): ", validate_date)
    description = input("Enter description: ")

    expense = Expense(amount, category, date, description)
    expenses.append(expense)

    print("Expense added successfully!")

def view_expenses(expenses):
    print("\nALL EXPENSES")

    if not expenses:
        print("No expenses recorded.")
        return

    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense}")

def search_expenses(expenses):
    keyword = input("Enter keyword to search (category or description): ").lower()
    results = []

    for expense in expenses:
        if keyword in expense.category.lower() or keyword in expense.description.lower():
            results.append(expense)

    if not results:
        print("No matching expenses found.")
        return

    print("\nSEARCH RESULTS:")
    for expense in results:
        print(expense)

def expense_summary(expenses):
    if not expenses:
        print("No expenses available.")
        return

    total = sum(exp.amount for exp in expenses)
    average = total / len(expenses)

    print("\nEXPENSE SUMMARY")
    print(f"Total Expenses: ₹{total:.2f}")
    print(f"Average Expense: ₹{average:.2f}")

def category_summary(expenses):
    if not expenses:
        print("No expenses available.")
        return

    category_totals = defaultdict(float)

    for exp in expenses:
        category_totals[exp.category] += exp.amount

    print("\nCATEGORY-WISE SUMMARY")
    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")

def monthly_report(expenses):
    if not expenses:
        print("No expenses available.")
        return

    monthly_totals = defaultdict(float)

    for exp in expenses:
        month = exp.date[:7]  # YYYY-MM
        monthly_totals[month] += exp.amount

    print("\nMONTHLY EXPENSE REPORT")
    for month, amount in sorted(monthly_totals.items()):
        print(f"{month}: ₹{amount:.2f}")

def budget_check(expenses):
    try:
        budget = float(input("Enter your monthly budget: ₹"))
    except ValueError:
        print("Invalid budget amount.")
        return

    total = sum(exp.amount for exp in expenses)

    print(f"\nTotal Expenses: ₹{total:.2f}")
    print(f"Budget Limit: ₹{budget:.2f}")

    if total > budget:
        print("Warning: You have exceeded your budget!!!")
    else:
        print(" You are within your budget.")

import os

def export_report(expenses, filename="reports/summary_report.txt"):
    if not expenses:
        print("No expenses available to export.")
        return

    # Ensure reports directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    total = sum(exp.amount for exp in expenses)

    with open(filename, "w", encoding="utf-8") as file:
        file.write("PERSONAL FINANCE SUMMARY\n")
        file.write("=" * 30 + "\n")
        file.write(f"Total Expenses: ₹{total:.2f}\n")
        file.write(f"Number of Transactions: {len(expenses)}\n")

    print(f"Report exported successfully to '{filename}'")