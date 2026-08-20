from storage import TaskManager


def main():
    manager = TaskManager()

    print("="*50)
    print("To-Do List")
    print("="*50)

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the task: ")
            description = input("Enter the description of the task: ")
            start_date = input("Enter the start date of the task (YYYY-MM-DD): ")
            end_date = input("Enter the end date of the task (YYYY-MM-DD): ")
            manager.add_task(title, description, start_date, end_date)
            print("Task added successfully!")
        elif choice == "2":
            for task in manager.tasks:
                print(task)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()