import math
from datetime import datetime


# ----list expenses----#
def list_expenses(expenses: list[dict]) -> None:
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']}: {e['category']} - {e['description']} - {e['amount']}")


# ----total expenses----#
def total_expenses(expenses: list[dict]) -> None:
    total = 0
    for e in expenses:
        total += e["amount"]
    print("Total expenses:", total)


# ----expenses by category----#
def expenses_by_category(expenses: list[dict]) -> None:
    item = input("Enter category to filter expenses: ").strip().lower()
    item_notfound = True
    for e in expenses:
        if e["category"] == item:
            item_notfound = False
            print(f"{e['category']}: {e['amount']}")
    if item_notfound:
        print("No expenses found for the given category.")


# ----add expense----#
def add_expense() -> dict:
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Please use the format YYYY-MM-DD.")
    while True:
        description = input("Enter description: ").strip().lower()
        if description:
            break
        print("Description cannot be empty. Please enter a valid description.")
    while True:
        category = input("Enter category: ").strip().lower()
        if category:
            break
        print("Category cannot be empty. Please enter a valid category.")
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue
        if amount <= 0 or math.isnan(amount) or math.isinf(amount):
            print("Amount must be a positive number.")
            continue
        break
    return {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date,
    }


# ----delete expense----#
def delete_expense(expenses: list[dict]) -> dict | None:
    if not expenses:
        print("No expenses to delete.")
        return None
    list_expenses(expenses)
    while True:
        try:
            expense_number = int(input("Select the expense number to delete: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid expense number.")
            continue
        if 1 <= expense_number <= len(expenses):
            return expenses.pop(expense_number - 1)
        print("Invalid expense number. Please try again.")


# ----category totals----#
def category_totals(expenses: list[dict]) -> dict[str, float]:
    total = {}
    for e in expenses:
        cat = e["category"]
        total[cat] = total.get(cat, 0) + e["amount"]
    return total


# ----highest expense----#
def highest_expense(expenses: list[dict]) -> dict | None:
    if not expenses:
        return None
    highest = expenses[0]
    for e in expenses:
        if e["amount"] > highest["amount"]:
            highest = e
    return highest


# ----average expense----#
def average_expense(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses yet.")
        return
    total = 0
    for e in expenses:
        total += e["amount"]
    avg = total / len(expenses)
    print(f"Average of all the expenses: {avg:.2f}")


# ----search by description----#
def search_by_description(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses yet.")
        return
    des = input("Enter a description to search for: ").strip().lower()
    if not des:
        print("Search text cannot be empty.")
        return
    found = False
    for e in expenses:
        if des in e["description"].lower():
            found = True
            print(f"{e['description']} - category: {e['category']} - amount: {e['amount']}")
    if not found:
        print("No expense matches this description.")