
# Expense Tracker — Python

A simple command-line Expense Tracker built using Python. It lets you add, view, and clear expenses, and also shows a pie chart of your spending by category. All data is saved locally in a JSON file so nothing is lost when you close the program.

---

## Project Structure

| File | Description |
|------|-------------|
| `expense.py` | Main Python file with all functions and menu |
| `expenses.json` | Auto-generated file where expense data is stored |

---

##  Technologies Used

- Python 3
- JSON (for local data storage)
- OS module (for file handling)
- Matplotlib (for pie chart visualization)

---

##  Features

- **Add Expense** — Enter an amount and category (e.g. Food, Travel) and it gets saved
- **View Expenses** — Displays all recorded expenses with amount and category
- **Show Graph** — Generates a pie chart showing expense distribution across categories using Matplotlib
- **Clear All Expenses** — Deletes all saved data after confirmation
- **Persistent Storage** — Data is saved in `expenses.json` and reloaded every time the program runs

---

## How It Works

1. Run the program — a menu appears with 5 options
2. Choose **Add Expense** to log a new entry with amount and category
3. Choose **View Expenses** to see all entries listed
4. Choose **Show Graph** to see a pie chart of category-wise spending
5. Choose **Clear All** to wipe all data (asks for confirmation first)
6. Choose **Exit** to close the program

---

##  How to Run

1. Make sure Python 3 is installed
2. Install matplotlib if not already installed:
   ```
   pip install matplotlib
   ```
3. Run the file:
   ```
   python expense_tracker.py
   ```

---

##  Developed By

Tanisha Dyaga — Diploma in Computer Engineering
  
