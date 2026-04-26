import json
import os
import matplotlib.pyplot as plt

FILE_NAME = "expenses.json"

# Load data
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save data
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense():
    expenses = load_expenses()
    
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc): ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added!\n")

# View expenses
def view_expenses():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.\n")
        return
    
    print("\n📋 All Expenses:")
    for e in expenses:
        print(f"Amount: ₹{e['amount']}, Category: {e['category']}")
    print()

#clear expense
def clear_expenses():
    confirm = input("Are you sure you want to delete all data? (yes/no): ")
    
    if confirm.lower() == "yes":
        save_expenses([])   # empty list = clear file
        print("🗑️ All expenses cleared!\n")
    else:
        print("Cancelled.\n")

# Show graph
def show_graph():
    expenses = load_expenses()
    
    if not expenses:
        print("No data to display.\n")
        return
    
    category_totals = {}

    for e in expenses:
        category = e["category"]
        amount = e["amount"]
        
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # PIE CHART 👇
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()


# Main menu
def main():
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Graph")
        print("4. Clear All Expenses")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_graph()
        elif choice == "4":
            clear_expenses()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main() 