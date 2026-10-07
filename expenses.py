#----list Expenses----#
def list_expenses(expenses):
    for i in range(0,len(expenses)):
        print(f"{i+1}. {expenses[i]['date']}: {expenses[i]['category']} - {expenses[i]['description']} - ${expenses[i]['amount']}")

#----total expenses----#
def total_expenses(expenses):
    total=0
    for e in expenses:
      total+=e["amount"]
    print("Total expenses:", total)

#----expenses by category----#
def expenses_by_category(expenses):
  item=(input("Enter category to filter expenses: ").strip().lower())
  item_notfound=True
  for e in expenses: 
    if e["category"]==item:
      item_notfound=False
      print(f"{e['category']}: {e['amount']}")
  if item_notfound:
    print("No expenses found for the given category.")

#----add expense----#
def add_expense():
   date=input("Enter date (YYYY-MM-DD): ").strip()
   description=input("Enter description: ").strip()
   category=input("Enter category: ").strip().lower()
   amount=float(input("Enter amount: ").strip())
   new_expense={"amount": amount, "category": category, "description": description, "date": date}
   return new_expense

def delete_expense(expenses):
    list_expenses(expenses)
    print("Select the expense number to delete:")
    expense_number=int(input().strip())
    if 1 <= expense_number <= len(expenses):
        deleted_expense = expenses.pop(expense_number - 1)
        return deleted_expense
    else:
        print("Invalid expense number. Please try again.")