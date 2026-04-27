tasks = []

def add_task(task_name):
    """Add a task to the tracker."""
    new_task = {"name": task_name, "done": False}
    tasks.append(new_task)
    print(f' Added:{task_name}')

def find_tasks(keyword):
    """Search tasks by keyword and return matching results."""
    results = []
    for task in tasks:
        if keyword.lower() in task["name"].lower():
            results.append(task)
    return results

def complete_task(task_number):
    """Mark a task as completed based on its number."""
    index = task_number - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f' Completed: {tasks[index]["name"]}')
    else:
        print("Invalid task number.")

def show_tasks():
    """Display all tasks with their status"""
    if len(tasks) == 0:
        print("No tasks found.")
        return
    print("\n YOUR TO-DO LIST")
    print(" " + "-" * 30)
    for i in range(len(tasks)):
        status = "Done" if tasks[i]["done"] else " "
        print(f" {i + 1}. [{status}] {tasks[i]['name']}")
        print()

def show_menu():
    """Display the menu options."""
    print("  ╔══════════════════════════╗")
    print("  ║    TO-DO LIST TRACKER    ║")
    print("  ╠══════════════════════════╣")
    print("  ║  1. Add a task           ║")
    print("  ║  2. Complete a task      ║")
    print("  ║  3. Search tasks         ║")
    print("  ║  4. View all tasks       ║")
    print("  ║  5. Quit                 ║")
    print("  ╚══════════════════════════╝")
 
def main():
    print("\n Welcome to the TO-DO List Tracker!")
    print("  Keep track of your tasks and stay organized.\n")

    running = True
    while running:
        show_menu()
        choice = input("\n Enter your choice (1-5):").strip()
        if choice == "1":
            name = input("  Enter Task Name:").strip()
            if name != "":
                add_task(name)
            else:
                print("  Task name cannot be empty.")
        elif choice == "2":
            show_tasks()
            if len(tasks) > 0:
                try:
                    task_num = int(input("  Enter Task Number to Complete:").strip())
                    complete_task(task_num)
                except ValueError:
                    print("  Invalid input. Please enter a number.")
        elif choice == "3":
            keyword = input("  Enter search keyword: ").strip()
            matches = find_tasks(keyword)
            if len(matches) > 0:
                print(f'\n Found {len(matches)} matching task(s):')
                for match in matches:
                    status = "done" if match["done"] else "not done"
                    print(f' - {match["name"]} [{status}]')
            else:
                print("  No matching tasks found.")
                print()
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            print("  Goodbye! Stay productive!")
            running = False
        else:
            print("  Invalid choice. Please enter a number between 1 and 5.")

main()