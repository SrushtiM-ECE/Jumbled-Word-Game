class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        print(f"Current Balance: {self.balance}")

print("=== Bank Account Simulator ===")

name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        amt = float(input("Enter amount: "))
        account.deposit(amt)

    elif choice == "2":
        amt = float(input("Enter amount: "))
        account.withdraw(amt)

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
