def addTask(tasks, newTask):
    tasks.append(newTask)

def removeTask(tasks, taskToRemove):
    tasks.remove(taskToRemove)

def checkTasks(tasks):
    print("All " + str(len(tasks)) + " tasks:")
    for x in range(len(tasks)):
        print(str(x+1) + ") " + tasks[x])

def toDoApp():
    tasks = []
    while (True):
        choice = input("What do u wish to do with your task list [add/remove/check] tasks: ")
        if (choice == "add"):
            newTask = input("Enter new task to add to the list: ")
            addTask(tasks, newTask)
        elif (choice == "remove"):
            taskToRemove = input("Enter task that you want to remove from the list: ")
            removeTask(tasks, taskToRemove)
        elif (choice == "check"):
            checkTasks(tasks)
        else:
            print("The only methods avalible are [add/remove/check]")
        exitChoice = input("Do you wish to exit or continue in app [c/e]: ")
        if (exitChoice == "e"):
            break
if __name__ == "__main__":
    toDoApp()
