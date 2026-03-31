from schedule.add_task import add_task
from schedule.view_tasks import view_tasks
from schedule.run_tasks import run_tasks

def menu():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Run Scheduler")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter task name: ")
            time = input("Enter time (HH:MM): ")
            add_task(name, time)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            run_tasks()

        elif choice == "4":
            break

        else:
            print("Invalid choice")

menu()