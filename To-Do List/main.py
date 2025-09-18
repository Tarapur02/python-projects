def task():
    print("Welcome To the To-Do List..")
    task_list = []
    total_task = int(input("How many tasks do you want to add initially? : "))

    for i in range(1, total_task + 1):
        tasks = input(f"Enter task {i}: ")
        task_list.append(tasks)
    print(f"The tasks are: {task_list}")

    while True:
        operation = input("\nEnter \n 1 = Add \n 2 = Update \n 3 = Delete \n 4 = View \n 5 = Exit\nChoice: ")

        if operation == "1":
            new_task = input("Enter the new task to add: ")
            task_list.append(new_task)
            print("New task added")
            print(f"{task_list}")

        elif operation == "2":
            old_task = input("Enter the task you want to update: ")
            if old_task in task_list:
                new_task = input("Enter the new task: ")
                ind = task_list.index(old_task)
                task_list[ind] = new_task
                print(f"Updated To-Do List: {task_list}")
            else:
                print("Task not found")

        elif operation == "3":
            del_task = input("Enter the task you want to delete: ")
            if del_task in task_list:
                task_list.remove(del_task)
                print(f" Updated To-Do List: {task_list}")
            else:
                print("Task not found")

        elif operation == "4":
            print(f" Your To-Do List: {task_list}")

        elif operation == "5":
            print(" Completed all tasks. Exiting...")
            break

        else:
            print("Invalid Input")

task()
