"""This is the main file that runs the expenses program."""

import storage
from expenses import (
    list_expenses,
    total_expenses,
    expenses_by_category,
    add_expense,
    delete_expense,
    category_totals,
    highest_expense,
    search_by_description,
    average_expense,
)

MENU = """
Choose an option from the menu below:
1. Add an expense
2. List all expenses
3. Total expenses
4. Expenses by category
5. Delete expense
6. Category totals
7. Highest expense
8. Average expense
9. Search by description
10. Exit
"""

expenses = storage.load_expenses()

try:
    while True:
        print(MENU)
        choice = input("Enter your choice (1-10): ").strip()
        match choice:
            case "1":
                new = add_expense()
                expenses.append(new)
                storage.save_expenses(expenses)
                print("Expense added successfully!")
            case "2":
                if not expenses:
                    print("No expenses yet.")
                else:
                    list_expenses(expenses)
            case "3":
                total_expenses(expenses)
            case "4":
                expenses_by_category(expenses)
            case "5":
                deleted = delete_expense(expenses)
                if deleted is not None:
                    storage.save_expenses(expenses)
                    print(f"Deleted: {deleted['description']} - {deleted['amount']}")
            case "6":
                result = category_totals(expenses)
                if not result:
                    print("No expenses yet.")
                else:
                    for cat, total in result.items():
                        print(f"{cat}: {total}")
            case "7":
                highest = highest_expense(expenses)
                if highest is None:
                    print("No expenses yet.")
                else:
                    print(
                        f"Highest expense: {highest['description']} - {highest['amount']}"
                    )
            case "8":
                average_expense(expenses)
            case "9":
                search_by_description(expenses)
            case "10":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option from the menu.")
except (KeyboardInterrupt, EOFError):
    print("\nProgram interrupted by user. Goodbye!")
