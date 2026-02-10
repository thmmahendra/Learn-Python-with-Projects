# Load existing items
# 1. Create a new item
# 2. List items
# 3. Mark items as complete
# 4. Save items

import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try: 
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        print("Failed to save")

def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No Tasks to display")
    else:
        print("Your To-Do List")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else ["Pending"]
            print(f"{idx + 1}.{task['description']} | {status}")

def create_tasks(tasks):
    description = input("Enter the tasks description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Tasks added.")
    else:
        print("Description cannot be empty.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number")
    except:
        print("Valid task number.")

def mark_task_incomplete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as incomplete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = False
            save_tasks(tasks)
            print("Task marked as Incomplete.")
        else:
            print("Invalid task number")
    except:
        print("Valid task number.")

def main():
    tasks = load_tasks()

    while True: 
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Complete Tasks")
        print("4. Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            mark_task_incomplete(tasks)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again")

main()

