class Expense:
    """
    Represents a single expense entry.
    """

    def __init__(self, amount, category, date, description):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.category} | ₹{self.amount:.2f} | {self.description}"

    def to_list(self):
        return [self.date, self.category, self.amount, self.description]