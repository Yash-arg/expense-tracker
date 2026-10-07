import math


#----list Expenses----#
def list_expenses(expenses:list[dict])->None:
    for i in range(0,len(expenses)):
        print(f"{i+1}. {expenses[i]['date']}: {expenses[i]['category']} - {expenses[i]['description']} - ${expenses[i]['amount']}")

#----total expenses----#
def total_expenses(expenses:list[dict])->None:
    total=0
    for e in expenses:
      total+=e["amount"]
    print("Total expenses:", total)

#----expenses by category----#
def expenses_by_category(expenses:list[dict])->None:
  item=(input("Enter category to filter expenses: ").strip().lower())
  item_notfound=True
  for e in expenses: 
    if e["category"]==item:
      item_notfound=False
      print(f"{e['category']}: {e['amount']}")
  if item_notfound:
    print("No expenses found for the given category.")

#----add expense----#
def add_expense()->dict:
    date=input("Enter date (YYYY-MM-DD): ").strip()
    while True:
        description=input("Enter description: ").strip().lower()
        if description=="":
           print("Description cannot be empty. Please enter a valid description.")
        else:
            break
    while True:
        category=input("Enter category: ").strip().lower()
        if category=="":
           print("Category cannot be empty. Please enter a valid category.")
        else:
            break
    while True:
        try:
            amount=float(input("Enter amount: ").strip())
            if amount <= 0 or math.isnan(amount) or math.isinf(amount):
                print("Amount cannot be negative or infinite or NaN. Please enter a positive value.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue 
        new_expense={"amount": amount, "category": category, "description": description, "date": date}
        return new_expense

def delete_expense(expenses:list[dict])->dict:
    list_expenses(expenses)
    if not expenses:
                print("No expenses to delete.")
                return None
    print("Select the expense number to delete:")
    while True:
        try:
            expense_number=int(input().strip())
            if 1 <= expense_number <= len(expenses):
                deleted_expense = expenses.pop(expense_number - 1)
                return deleted_expense
            else:
                print("Invalid expense number. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid expense number.")
            continue