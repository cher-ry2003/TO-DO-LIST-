import datetime

class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.completed_tasks = {}
        self.task_id_counter = 1

    def add_task(self, description, due_date=None, priority=None):
        task_id = self.task_id_counter
        task = {"description": description, "due_date": due_date, "priority": priority}
        self.tasks[task_id] = task
        self.task_id_counter += 1
        print(f"Task '{description}' added with ID: {task_id}")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("\n--- To-Do List ---")
            for task_id, task in self.tasks.items():
                print(
                    f"ID: {task_id}, Description: {task['description']}, "
                    f"Due Date: {task['due_date']}, Priority: {task['priority']}"
                )

    def complete_task(self, task_id):
        if task_id in self.tasks:
            completed_task = self.tasks.pop(task_id)
            self.completed_tasks[task_id] = completed_task
            print(f"Task '{completed_task['description']}' marked as completed.")
        else:
            print(f"Task with ID {task_id} not found in the to-do list.")

    def update_task(self, task_id, new_description=None, new_due_date=None, new_priority=None):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task["description"] = new_description if new_description else task["description"]
            task["due_date"] = new_due_date if new_due_date else task["due_date"]
            task["priority"] = new_priority if new_priority else task["priority"]
            print(f"Task '{task['description']}' updated successfully.")
        else:
            print(f"Task with ID {task_id} not found in the to-do list.")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Task '{removed_task['description']}' removed from the to-do list.")
        else:
            print(f"Task with ID {task_id} not found in the to-do list.")

    def display_completed_tasks(self):
        if not self.completed_tasks:
            print("No completed tasks.")
        else:
            print("\n--- Completed Tasks ---")
            for task_id, task in self.completed_tasks.items():
                print(
                    f"ID: {task_id}, Description: {task['description']}, "
                    f"Due Date: {task['due_date']}, Priority: {task['priority']}"
                )


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Display Completed Tasks")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")
            priority = input("Enter priority (optional): ")
            todo_list.add_task(description, due_date, priority)

        elif choice == "2":
            todo_list.display_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.complete_task(task_id)

        elif choice == "4":
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description (press Enter to keep the existing): ")
            new_due_date = input("Enter new due date (optional, format: YYYY-MM-DD, press Enter to keep the existing): ")
            new_priority = input("Enter new priority (optional, press Enter to keep the existing): ")
            todo_list.update_task(task_id, new_description, new_due_date, new_priority)

        elif choice == "5":
            task_id = int(input("Enter task ID to remove: "))
            todo_list.remove_task(task_id)

        elif choice == "6":
            todo_list.display_completed_tasks()

        elif choice == "0":
            print("Exiting the To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 6.")


if __name__ == "__main__":
    main()
