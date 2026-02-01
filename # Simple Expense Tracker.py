# Simple Expense Tracker

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (food/travel/study/etc): ")
    note = input("Enter note: ")

    expenses.append({
        "amount": amount,
        "category": category,
        "note": note
    })
    print("Expense added successfully!\n")

def show_summary():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total = sum(e["amount"] for e in expenses)
    print("\n--- Expense Summary ---")
    print("Total Spent:", total)

    category_total = {}
    for e in expenses:
        category_total[e["category"]] = category_total.get(e["category"], 0) + e["amount"]

    print("\nCategory-wise:")
    for cat, amt in category_total.items():
        print(cat, ":", amt)
    print()

while True:
    print("1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
