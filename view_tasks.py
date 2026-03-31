from .add_task import tasks

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} at {task['time']} - {task['status']}")