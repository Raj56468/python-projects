tasks = {}

def add_task(task):
    if task in tasks:
        print(f"task '{task}' already exist")
    else:
        tasks[task] = False
        print(f"task added")


def completed_task(task):
    if task in tasks:
        tasks[task] = True
        print(f"task completed")
    else:
        print("task not found")

def show_tasks():
    for task, completed in tasks.items():
        status = "completed" if completed else "pending"
        print(f"{task}: {status}")

if __name__ == "__main__":
    while True:
        action = input("choose an action (add, complete, show, exit): ").lower()
        if action == "add":
            task = input("enter a task: ")
            add_task(task)
        elif action == "complete":
            task = input("enter a task to complete: ")
            completed_task(task)
        elif action == "show":
            show_tasks()
        elif action == "exit":
            break
        else:
            print("invalid action")