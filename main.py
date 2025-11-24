# ───────────────────────────────────────────────
# Student Expense Manager - Simple Console App
# ───────────────────────────────────────────────

import json
import os

DATA_FILE = "expenses_data.json"

# Load previous data if exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
        transactions = data.get("transactions", [])
        balance = data.get("balance", 0)
else:
    transactions = []
    balance = 0

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump({"transactions": transactions, "balance": balance}, file, indent=4)

def add_income():
    global balance
    amount = float(input("Enter income amount: ₹"))
    source = input("Source (Parents, Scholarship, Job etc.): ")
    balance += amount
    transactions.append({"type": "income", "amount": amount, "detail": source})
    save_data()
    print(f"Income added successfully! Current balance: ₹{balance}\n")

def add_expense():
    global balance
    amount = float(input("Enter expense amount: ₹"))
    purpose = input("Expense category (Food, Travel, Books, etc.): ")

    if amount > balance:
        print("\n⚠ Not enough balance! Expense cancelled.\n")
        return

    balance -= amount
    transactions.append({"type": "expense", "amount": amount, "detail": purpose})
    save_data()
    print(f"Expense recorded! Current balance: ₹{balance}\n")

def view_balance():
    print(f"\n Current Balance: ₹{balance}\n")

def view_history():
    print("\n Transaction History:")
    if not transactions:
        print("No transactions yet.\n")
        return

    for t in transactions:
        sign = "+" if t["type"] == "income" else "-"
        print(f"• {sign} ₹{t['amount']} ({t['detail']})")

    print()

def menu():
    while True:
        print("Student Expense Manager")
        print("1 Add Income")
        print("2 Add Expense")
        print("3 View Balance")
        print("4 View All Transactions")
        print("5 Exit")
        
        choice = input("\nSelect an option (1-5): ")
        print()

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_balance()
        elif choice == "4":
            view_history()
        elif choice == "5":
            print(" Exiting... Stay mindful with money!")
            break
        else:
            print(" Invalid choice, try again")
menu()
