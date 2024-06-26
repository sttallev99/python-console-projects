import json
from datetime import datetime


def add_task(tasks, task):
    """
    Adds a new task to the task list.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task (dict): The task to be added.

    Returns:
    list of dict: Updated list of tasks.
    """
    tasks.append(task)
    return tasks


def remove_task(tasks, task_id):
    """
    Removes a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be removed.

    Returns:
    list of dict: Updated list of tasks.
    """
    task = None
    for curr_task in tasks:
        if curr_task["id"] == task_id:
            task = curr_task
            break

    try:
        if task == None:
            raise Exception
        else:
            tasks.remove(task)
            return tasks
    except Exception as e:
        print("Not found task with the given id. Try again...")


def update_task(tasks, task_id, updated_task):
    """
    Updates an existing task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    updated_task (dict): The updated task details.

    Returns:
    list of dict: Updated list of tasks.
    """
    is_found = False
    for curr_task in tasks:
        if curr_task["id"] == task_id:
            is_found = True
            task_id = tasks.index(curr_task)
            tasks[task_id] = updated_task

    try:
        if not is_found:
            raise Exception
        else:
            return tasks
    except Exception as e:
        print("Not found task to update with the given id.Try again...")


def get_task(tasks, task_id):
    """
    Retrieves a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be retrieved.

    Returns:
    dict: The task with the specified ID, or None if not found.
    """
    for curr_task in tasks:
        if curr_task["id"] == task_id:
            return curr_task

    return "Not found task with the given id.Try again..."


def set_task_priority(tasks, task_id, priority):
    """
    Sets the priority of a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    priority (str): The new priority level.

    Returns:
    list of dict: Updated list of tasks.
    """

    is_found = False
    for curr_task in tasks:
        if curr_task["id"] == task_id:
            curr_task["priority"] = priority
            is_found = True
            return tasks
    try:
        if not is_found:
            raise Exception
    except Exception as e:
        print("Not found task with the given id.Try again...")

def set_task_deadline(tasks, task_id, deadline):
    """
    Sets the deadline for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    deadline (str): The new deadline.

    Returns:
    list of dict: Updated list of tasks.
    """
    is_found = False
    for curr_task in tasks:
        if curr_task["id"] == task_id:
            curr_task["deadline"] = deadline
            is_found = True
            return tasks

    try:
        if not is_found:
            raise Exception
    except Exception as e:
        print("Not found task with the given id.Try again...")


def mark_task_as_completed(tasks, task_id):
    """
    Marks a task as completed.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be marked as completed.

    Returns:
    list of dict: Updated list of tasks.
    """
    is_found = False
    for curr_task in tasks:
        if curr_task["id"] == task_id:
            is_found = True
            try:
                if not curr_task["completed"]:
                    curr_task["completed"] = True
                    return tasks
                else:
                    raise Exception("Cannot close already closed task.Try again with other task...")
            except Exception as e:
                print(str(e))

    try:
        if not is_found:
            raise Exception("Not found task with the given id.Try again...")
    except Exception as e:
        print(str(e))


def set_task_description(tasks, task_id, description):
    """
    Sets the description for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    description (str): The new description.

    Returns:
    list of dict: Updated list of tasks.
    """
    is_found = False
    for curr_task in tasks:
        if curr_task["id"] == task_id:
            is_found = True
            try:
                if description != "":
                    curr_task["description"] = description
                    return tasks
                else:
                    raise Exception("Description cannot be empty.Try again...")
            except Exception as e:
                print(str(e))
                return {
                    "tasks": tasks,
                    "error_message": str(e)
                }
    try:
        if not is_found:
            raise Exception("Not found task with the given id.Try again...")
    except Exception as e:
        print(str(e))
        return tasks


def search_tasks_by_keyword(tasks, keyword):
    """
    Searches tasks by a keyword in the description.

    Parameters:
    tasks (list of dict): The current list of tasks.
    keyword (str): The keyword to search for.

    Returns:
    list of dict: Tasks that contain the keyword in their description.
    """
    filtered_tasks = []
    for curr_task in tasks:
        if keyword in curr_task["description"]:
            filtered_tasks.append(curr_task)

    return filtered_tasks


def filter_tasks_by_priority(tasks, priority):
    """
    Filters tasks by priority.

    Parameters:
    tasks (list of dict): The current list of tasks.
    priority (str): The priority level to filter by.

    Returns:
    list of dict: Tasks with the specified priority.
    """
    filtered_tasks = []
    for curr_task in tasks:
        if curr_task["priority"] == priority:
            filtered_tasks.append(curr_task)

    return filtered_tasks


def filter_tasks_by_status(tasks, status):
    """
    Filters tasks by their completion status.

    Parameters:
    tasks (list of dict): The current list of tasks.
    status (bool): The completion status to filter by.

    Returns:
    list of dict: Tasks with the specified completion status.
    """
    return list(filter(lambda task: task["completed"] == status, tasks))


def filter_tasks_by_deadline(tasks, deadline):
    """
    Filters tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.
    deadline (str): The deadline to filter by.

    Returns:
    list of dict: Tasks with the specified deadline.
    """
    return list(filter(lambda task: task["deadline"] == deadline, tasks))


def count_tasks(tasks):
    """
    Returns the total number of tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The total number of tasks.
    """
    return len(tasks)


def count_completed_tasks(tasks):
    """
    Returns the number of completed tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of completed tasks.
    """
    return len(list(filter(lambda task: task["completed"], tasks)))


def count_pending_tasks(tasks):
    """
    Returns the number of pending tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of pending tasks.
    """
    return len(list(filter(lambda task: not task["completed"], tasks)))


def generate_task_summary(tasks):
    """
    Generates a summary report of all tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    dict: A summary report containing total, completed, and pending tasks.
    """
    all_tasks = len(tasks)
    completed_tasks = len(list(filter(lambda task: task["completed"], tasks)))
    pending_tasks = len(list(filter(lambda task: not task["completed"], tasks)))

    return {
        "all": all_tasks,
        "completed": completed_tasks,
        "pending": pending_tasks
    }


def save_tasks_to_file(tasks, file_path):
    """
    Saves the task list to a file.

    Parameters:
    tasks (list of dict): The current list of tasks.
    file_path (str): The path to the file where tasks will be saved.

    Returns:
    None
    """
    # result = ""
    # for curr_task in tasks:
    #     curr_result = ""
    #     for k, v in curr_task.items():
    #         if k == "id":
    #             curr_result = f"{k} : {v}\n"
    #         else:
    #             curr_result += f"\t{k} : {v}\n"
    #     result += curr_result
    #
    file1 = open(file_path, "a")
    for curr_task in tasks:
        file1.write(str(curr_task) + "\n")
    file1.close()

    return tasks


def load_tasks_from_file(file_path):
    """
    Loads the task list from a file.

    Parameters:
    file_path (str): The path to the file where tasks are saved.

    Returns:
    list of dict: The loaded list of tasks.
    """
    file1 = open(file_path, "r")
    loaded_tasks = file1.readlines()
    file1.close()
    loaded_tasks = list(map(lambda task: eval(task[:len(task) - 1]), loaded_tasks))

    return loaded_tasks


def sort_tasks_by_deadline(tasks):
    """
    Sorts tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """


def sort_tasks_by_priority(tasks):
    """
    Sorts tasks by their priority.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """


def print_menu():
    """
    Prints the user menu.
    """
    menu = """
    Task Manager Menu:
    1. Add Task
    2. Remove Task
    3. Update Task
    4. Get Task
    5. Set Task Priority
    6. Set Task Deadline
    7. Mark Task as Completed
    8. Set Task Description
    9. Search Tasks by Keyword
    10. Filter Tasks by Priority
    11. Filter Tasks by Status
    12. Filter Tasks by Deadline
    13. Count Tasks
    14. Count Completed Tasks
    15. Count Pending Tasks
    16. Generate Task Summary
    17. Save Tasks to File
    18. Load Tasks from File
    19. Sort Tasks by Deadline
    20. Sort Tasks by Priority
    21. Exit
    """
    print(menu)


def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task = {
                'id': int(input("Enter task ID: ")),
                'description': input("Enter task description: "),
                'priority': input("Enter task priority (low, medium, high): "),
                'deadline': input("Enter task deadline (YYYY-MM-DD): "),
                'completed': False
            }
            tasks = add_task(tasks, task)
            print("Task added successfully.")
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            tasks = remove_task(tasks, task_id)
            if isinstance(tasks, list):
                print("Task removed successfully.")
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
            except ValueError as e:
                print("task id need to be a number")
                continue
            updated_task = {
                'description': input("Enter new task description: "),
                'priority': input("Enter new task priority (low, medium, high): "),
                'deadline': input("Enter new task deadline (YYYY-MM-DD): ")
            }
            tasks = update_task(tasks, task_id, updated_task)
            if isinstance(tasks, list):
                print("Task updated successfully.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to get: "))
            except ValueError as e:
                print("task id need to be a number")
                continue
            task = get_task(tasks, task_id)
            print("Task details:", task)
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to set priority: "))
            except ValueError:
                print("task id need to be a number")
                continue
            priority = input("Enter new priority (low, medium, high): ")
            tasks = set_task_priority(tasks, task_id, priority)
            if isinstance(tasks, list):
                print("Task priority set successfully.")
        elif choice == '6':
            try:
                task_id = int(input("Enter task ID to set deadline: "))
            except ValueError as e:
                print("task id need to be a number")
                continue
            deadline = input("Enter new deadline (YYYY-MM-DD): ")
            tasks = set_task_deadline(tasks, task_id, deadline)
            if isinstance(tasks, list):
                print("Task deadline set successfully.")
        elif choice == '7':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
            except ValueError as e:
                print("task id need to be a number")
                continue
            tasks = mark_task_as_completed(tasks, task_id)
            if isinstance(tasks, list):
                print("Task marked as completed.")
        elif choice == '8':
            try:
                task_id = int(input("Enter task ID to set description: "))
            except ValueError as e:
                print("task id need to be a number")
                continue
            description = input("Enter new description: ")
            tasks = set_task_description(tasks, task_id, description)
            if isinstance(tasks, list):
                print("Task description set successfully.")
            else:
                tasks = tasks["tasks"]
        elif choice == '9':
            keyword = input("Enter keyword to search: ")
            found_tasks = search_tasks_by_keyword(tasks, keyword)
            print("Tasks found:", found_tasks)
        elif choice == '10':
            try:
                priority = input("Enter priority to filter by (low, medium, high): ")
                if priority != "low" and priority != "medium" and priority != "high":
                    raise Exception("Priority field need to be one ot these: (low, medium, high).Try again...")
            except Exception as e:
                print(str(e))
                continue
            filtered_tasks = filter_tasks_by_priority(tasks, priority)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '11':
            status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'
            filtered_tasks = filter_tasks_by_status(tasks, status)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '12':
            deadline = input("Enter deadline to filter by (YYYY-MM-DD): ")
            filtered_tasks = filter_tasks_by_deadline(tasks, deadline)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '13':
            total_tasks = count_tasks(tasks)
            print("Total number of tasks:", total_tasks)
        elif choice == '14':
            completed_tasks = count_completed_tasks(tasks)
            print("Number of completed tasks:", completed_tasks)
        elif choice == '15':
            pending_tasks = count_pending_tasks(tasks)
            print("Number of pending tasks:", pending_tasks)
        elif choice == '16':
            summary = generate_task_summary(tasks)
            print("Task Summary:", summary)
        elif choice == '17':
            file_path = input("Enter file path to save tasks: ")
            save_tasks_to_file(tasks, file_path)
            print("Tasks saved to file.")
        elif choice == '18':
            file_path = input("Enter file path to load tasks from: ")
            tasks = load_tasks_from_file(file_path)
            print("Tasks loaded from file.")
        elif choice == '19':
            tasks = sort_tasks_by_deadline(tasks)
            print("Tasks sorted by deadline.")
        elif choice == '20':
            tasks = sort_tasks_by_priority(tasks)
            print("Tasks sorted by priority.")
        elif choice == '21':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

