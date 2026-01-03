import matplotlib.pyplot as plt
from collections import defaultdict

def plot_category_expenses(expenses):
    category_totals = defaultdict(float)

    for exp in expenses:
        category_totals[exp.category] += exp.amount

    if not category_totals:
        print("No data available for visualization.")
        return

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure()
    plt.bar(categories, amounts)
    plt.title("Category-wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.show()


def plot_monthly_expenses(expenses):
    monthly_totals = defaultdict(float)

    for exp in expenses:
        month = exp.date[:7]
        monthly_totals[month] += exp.amount

    if not monthly_totals:
        print("No data available for visualization.")
        return

    months = list(monthly_totals.keys())
    amounts = list(monthly_totals.values())

    plt.figure()
    plt.plot(months, amounts, marker="o")
    plt.title("Monthly Expenses Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")
    plt.show()
