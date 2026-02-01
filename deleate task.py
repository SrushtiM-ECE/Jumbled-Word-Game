# To-Do List Manager

tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(i, ".", task)
    print()

def delete_task():
    view_tasks()
    if tasks:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print("Removed:", removed, "\n")
        else:
            print("Invalid number!\n")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")
