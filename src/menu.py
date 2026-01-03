from src.reports import (
    add_expense,
    view_expenses,
    search_expenses,
    expense_summary,
    category_summary,
    monthly_report,
    budget_check,
    export_report
)
from src.file_manager import save_expenses, backup_data
from src.visuals import plot_category_expenses, plot_monthly_expenses


def run_menu(expenses):
    while True:
        show_menu()
        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_expenses(expenses)

        elif choice == "4":
            expense_summary(expenses)

        elif choice == "5":
            category_summary(expenses)

        elif choice == "6":
            monthly_report(expenses)

        elif choice == "7":
            try:
                backup_data()
                print("Data backup successful!!")
            except Exception as e:
                print(f"Backup failed: {e}")

        elif choice == "8":
            save_expenses(expenses)
            print("Exiting... Data saved.")
            break

        elif choice == "9":
            plot_category_expenses(expenses)

        elif choice == "10":
            plot_monthly_expenses(expenses)

        elif choice == "11":
            budget_check(expenses)

        elif choice == "12":
            export_report(expenses)

        else:
            print("Invalid choice. Please try again.")


def show_menu():
    print("\n" + "=" * 40)
    print("     PERSONAL FINANCE MANAGER")
    print("=" * 40)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Expense Summary")
    print("5. Category-wise Summary")
    print("6. Monthly Report")
    print("7. Backup Data")
    print("8. Exit")
    print("9. Category-wise Expense Chart")
    print("10. Monthly Expense Chart")
    print("11. Budget Check")
    print("12. Export Summary Report")
