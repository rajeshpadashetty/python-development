tasks = []


def add_task(name, time):
    name = name.strip()
    time = time.strip()
    task = {"name": name, "time": time, "status": "Pending"}
    tasks.append(task)
    print(f"Task '{name}' scheduled at {time} added successfully.")