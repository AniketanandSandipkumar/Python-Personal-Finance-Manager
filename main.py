from src.file_manager import load_expenses
from src.menu import run_menu

def main():
    expenses = load_expenses()
    run_menu(expenses)

if __name__ == "__main__":
    main()
