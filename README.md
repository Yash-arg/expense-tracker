# Expense Tracker

A command-line expense tracker written in Python. Add, view, search and analyse your expenses from a simple menu. All data is saved to a JSON file, so it is still there the next time you run the app.

## Requirements

- Python 3.10 or newer
- No external packages (only the Python standard library)

## How to run

```bash
git clone https://github.com/Yash-arg/expense-tracker.git
cd expense-tracker
python app.py
```

## Features

- Add an expense with date, description, category and amount
- List all expenses
- Show total spending
- Filter expenses by category
- Delete an expense
- Category-wise totals
- Highest expense
- Average expense
- Search expenses by description
- Data saved automatically to `expenses.json`

### Input validation

- Dates must be in `YYYY-MM-DD` format and be real dates
- Description and category cannot be empty
- Amount must be a positive number
- Invalid menu choices and expense numbers are rejected with a clear message
- A missing or corrupted `expenses.json` does not crash the app; it starts with an empty list
- Ctrl+C exits cleanly

## Example

```
Choose an option from the menu below:
1. Add an expense
2. List all expenses
...
10. Exit

Enter your choice (1-10): 1
Enter date (YYYY-MM-DD): 2026-10-09
Enter description: Lunch
Enter category: Food
Enter amount: 250
Expense added successfully!

Enter your choice (1-10): 2
1. 2026-10-09: food - lunch - 250.0
```

## Project structure

```
expense-tracker/
├── app.py            # Menu and user interaction
├── expenses.py       # Expense features (add, list, delete, totals, search)
├── storage.py        # Load and save expenses to JSON
├── expenses.json     # Saved expense data
├── requirements.txt  # No external dependencies
└── README.md
```

## Known limitations

- Single user only
- Data is stored in a local JSON file, not a database
- No monthly summary or date filtering yet