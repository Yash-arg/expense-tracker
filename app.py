import storage
from expenses import list_expenses, total_expenses, expenses_by_category, add_expense,delete_expense

'''This is the main file that runs the expenses program.'''
expenses =storage.load_expenses()  
while True:
  try:
    print(f"Choose and option from the menu below:\n1.Add an expense\n2. List all expenses\n3. Total expenses\n4. Expenses by category\n5. Delete Expense\n6. Exit\n")
    choice = str(input("Enter your choice 1 2 3 4 5 6: \n"))
    match (choice):
      case "1":
        new = add_expense()
        expenses.append(new)
        storage.save_expenses(expenses)  
        print("Expense added successfully!")
      case "2":
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
        print("Exiting the program. Goodbye!")
        break
      case _:
        print("Invalid choice. Please select a valid option from the menu.")
  except KeyboardInterrupt:
      print("\nProgram interrupted by user.")
      break
