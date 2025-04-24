def welcomeMessage():
    print("||=========================================================||")
    print("|| Welcome to the To-Do List App! Let's organise your day! ||")
    print("||=========================================================||")
    helpMenu()


def helpMenu():
    print("\n--- To-Do List App Features ---")
    print("0. Show Help Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Switch Tasks Order")
    print("5. Quit")


def userInput():
    while True:
        user_input = input("\nWhat would you like to do? (enter a command number of your choice 0-5): ")
    
        if not user_input.isdigit():
            print("Please enter a valid number and try again!")
        else:
            user_input = int(user_input)
            if user_input < 0 or user_input > 5:
                print("Invalid choice of a number. Please try again.")
            else:
                return user_input


def addCommand(task_list):
    task = input("Enter the task: ")
    
    if len(task) == 0:  
        print("Empty tasks are not supposed to appear in Your To-Do List! Try adding something else.")
    else:
        print(f'Task "{task}" was successfully added to the list!')
        task_list.append(task)

   
def viewCommand(task_list):
    if len(task_list) == 0:
        print("There are no tasks in the list at the moment. Create one right now!")
        return
    else:
        print("\nYour To-Do List for today:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}) {task}")

def removeCommand(task_list):
    if len(task_list) == 0:
        print("There are no tasks in the list at the moment. Create one right now!")
    
    if len(task_list) != 0:
        viewCommand(task_list)
        task_number = input("\nEnter the task number to remove: ")

        if task_number.isdigit():
            task_number = int(task_number)
            if 1 <= task_number <= len(task_list):
                removed_task = task_list.pop(task_number - 1)
                print(f'Task "{removed_task}" was successfully removed from the list!')
            else:
                print("Invalid task number. Please try again.")
        else:
            print("Invalid task number. Please try again.")


def switchCommand(task_list):
    if len(task_list) == 0:
        print("There are no tasks in the list at the moment. Create one right now!")
        return
    if len(task_list) == 1:
        viewCommand(task_list)
        print("\nThere is no point in switching when there is only one task in the list! Please, try something else.")
    else:
        viewCommand(task_list)
        
        first_task = input("\nEnter the first task number: ")
        if not first_task.isdigit() or not (1 <= int(first_task) <= len(task_list)):
            print("Invalid task number. Please try again.")
            return
        
        second_task = input("Enter the second task number: ")
        if not second_task.isdigit() or not (1 <= int(second_task) <= len(task_list)):
            print("Invalid task number. Please try again.")
            return
        
        first_task = int(first_task)
        second_task = int(second_task)
            
        if first_task != second_task:
            task_list[first_task - 1], task_list[second_task - 1] = task_list[second_task - 1], task_list[first_task - 1]
            print("Tasks' positions were successfully switched!")
        else:
            print("There is no point in switching the task with itself! Please, try something else.")


def todoApp():
    task_list = []
    welcomeMessage()
    
    while True:
        user_input = userInput()
        
        if user_input == 0:
            helpMenu()
        elif user_input == 1:
            addCommand(task_list)
        elif user_input == 2:
            viewCommand(task_list)
        elif user_input == 3:
            removeCommand(task_list)
        elif user_input == 4:
            switchCommand(task_list)
        elif user_input == 5:
            print("\nThank you for using the To-Do List App. Goodbye!")
            break

todoApp()

