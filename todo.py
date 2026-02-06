# Load existing items
# 1. Create a new item
# 2. List items
# 3. Mark items as complete
# 4. Save items

def load_tasks():
    pass

def save_tasks():
    pass

def view_tasks():
    pass

def create_tasks():
    pass

def mark_task_complete():
    pass

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Complete Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            create_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again")

main()

