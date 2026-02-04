# Expense Tracker using File Handling

FILENAME = "expenses.txt"

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    with open(FILENAME, "a") as f:
        f.write(f"{name},{amount}\n")

    print("Expense saved!\n")

def view_expenses():
    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()

        if not lines:
            print("No expenses found.\n")
            return

        print("\nExpenses:")
        for line in lines:
            name, amt = line.strip().split(",")
            print(f"{name} - {amt}")

        print()

    except FileNotFoundError:
        print("No expense file found.\n")

def analyze_expenses():
    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()

        amounts = [float(line.strip().split(",")[1]) for line in lines]

        print(f"Total Expense: {sum(amounts)}")
        print(f"Highest Expense: {max(amounts)}")
        print(f"Average Expense: {sum(amounts)/len(amounts):.2f}\n")

    except:
        print("No data to analyze.\n")

while True:
    print("=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Analyze Expenses")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        analyze_expenses()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid option\n")
