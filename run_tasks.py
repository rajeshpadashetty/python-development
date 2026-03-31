from datetime import datetime
from .add_task import tasks
import time

def run_tasks():
    print("Scheduler started...")

    while True:
        now = datetime.now().strftime("%H:%M")
        for task in tasks:
            if task["time"] == now and task["status"] == "Pending":
                print(f"Running task: {task['name']}")
                task["status"] = "Completed"
        time.sleep(5)
                            

       