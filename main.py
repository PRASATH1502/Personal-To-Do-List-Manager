tasks = {}
def add_task(task, description, due_date):
    tasks[len(tasks) + 1] = {'task': task, 'description': description, 'due_date': due_date, 'completed': False}
def mark_task_completed(task_id):
    if task_id in tasks:
        tasks[task_id]['completed'] = True
    else:
        print("Task not found!")
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print("Task deleted successfully!")
    else:
        print("Task not found!")
def view_tasks(filter_option=None):
    if not tasks:
        print("No tasks found!")
        return
    filtered_tasks = {}
    if filter_option == 'completed':
        filtered_tasks = {task_id: task_info for task_id, task_info in tasks.items() if task_info['completed']}
    elif filter_option == 'pending':
        filtered_tasks = {task_id: task_info for task_id, task_info in tasks.items() if not task_info['completed']}
    else:
        filtered_tasks = tasks
    print("\n===== Tasks =====")
    for task_id, task_info in filtered_tasks.items():
        print(f"Task ID: {task_id}")
        print(f"Task: {task_info['task']}")
        print(f"Description: {task_info['description']}")
        print(f"Due Date: {task_info['due_date']}")
        print(f"Status: {'Completed' if task_info['completed'] else 'Pending'}")
        print("")
while True:
    print("\n===== To-Do List Manager =====")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. View Completed Tasks")
    print("6. View Pending Tasks")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        task = input("Enter the task: ")
        description = input("Enter the description: ")
        due_date = input("Enter the due date: ")
        add_task(task, description, due_date)
        print("Task added successfully!")
    elif choice == '2':
        task_id = int(input("Enter the task ID to mark as completed: "))
        mark_task_completed(task_id)
    elif choice == '3':
        task_id = int(input("Enter the task ID to delete: "))
        delete_task(task_id)
    elif choice == '4':
        view_tasks()
    elif choice == '5':
        view_tasks(filter_option='completed')
    elif choice == '6':
        view_tasks(filter_option='pending')
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
