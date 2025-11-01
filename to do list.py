# TO-DO LIST APPLICATION

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour To-Do List:")
        for i, t in enumerate(tasks, start=1):
            status = "✅ Done" if t['done'] else "❌ Not Done"
            print(f"{i}. {t['task']}  --> {status}")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        show_tasks()

    elif choice == '2':
        task = input("Enter new task: ")
        tasks.append({'task': task, 'done': False})
        print("✅ Task added successfully!")

    elif choice == '3':
        show_tasks()
        num = int(input("Enter task number to mark as done: "))
        if 0 < num <= len(tasks):
            tasks[num-1]['done'] = True
            print("✔ Task marked as done!")
        else:
            print("Invalid task number!")

    elif choice == '4':
        show_tasks()
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"🗑 Removed: {removed['task']}")
        else:
            print("Invalid task number!")

    elif choice == '5':
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")