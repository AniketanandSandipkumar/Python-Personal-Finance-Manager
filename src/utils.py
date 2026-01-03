VALID_CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Shopping",
    "Other"
]

def validate_amount(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        raise ValueError("Amount must be a positive number.")

from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

def validate_category(category):
    category = category.title()
    if category not in VALID_CATEGORIES:
        raise ValueError(
            f"Category must be one of: {', '.join(VALID_CATEGORIES)}"
        )
    return category

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        try:
            return validation_func(user_input)
        except ValueError as e:
            print(f"Error: {e}")

