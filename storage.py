import json

def save_expenses(expenses:list[dict])->None:
    with open("expenses.json","w") as f:
        json.dump(expenses,f,indent=4)

def load_expenses()-> list[dict]:
    try:
        with open("expenses.json","r") as f:
            loaded=json.load(f)
        return loaded
    except FileNotFoundError:
        print("Error: The file 'expenses.json' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: The file 'expenses.json' is not a valid JSON file and is corrupted.")
        return []