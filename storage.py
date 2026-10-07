import json

def save_expenses(expenses):
    with open("expenses.json","w") as f:
        json.dump(expenses,f,indent=4)

def load_expenses():
    with open("expenses.json","r") as f:
        loaded=json.load(f)
    return loaded