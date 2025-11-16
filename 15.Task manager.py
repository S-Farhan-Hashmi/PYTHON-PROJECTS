print("Welcome to TaskManager360")
task=[]
category=[]
status=[]
def add():
    a=input("Enter the task name :  ").lower()
    if a in task:
        print("This task already exist,try again")
    else:
        task.append(a)
    b=input("Enter category of the task:  ").lower()
    category.append(b)
    c=input("Enter status of the task(completed or pending) : ")
    status.append(c)
def view():
    print(f"\nYou have {len(task)} tasks.")
    for i in range(len(task)):
        print("\n--- Task", i + 1, "---")
        print("Task:",task[i])
        print("Category:",category[i])
        print("Status:",status[i])
def edit():
    while True:
        a=input("Enter task which u want to change :   ").lower()
        if a in task:
            print("continue to mention what u want to change")
            break
        else:
            print("No task with that name exist please try again")
    print("type task to change task name \n type category to change category \n type status to change status \n type delete to delete task")
    b=input("Enter what u want to change : ").lower()
    c=task.index(a)
    if b=="task":
        d=input("Enter new task name : ").lower()
        task[c]=d
        print("updated task")
    elif b=="category":
        e=input("Enter new category : ").lower()
        category[c]=e
        print("updated category")
    elif b=="status":
        f=input("Enter new status :  ").lower()
        status[c]=f
        print("updated status")
    elif b=="delete":
        del task[c]
        del category[c]
        del status[c]
        print("deleted successfully")
    else:
        print("invalid change please try again")
def main():
    print("Enter what u want to do ")
    print("Enter add to add new task")
    print("Enter view to view tasks")
    print("Enter edit to edit existing task  ")
    print("Enter exit to exit from the portal ")
    while True:
        a=input("Enter what you want to perform : ")
        if a=="add":
            add()
        elif a=="view":
            view()
        elif a=="edit":
            edit()
        elif a=="exit":
            print("thanks for using TaskManager360 , please visit again")
            break
        else:
            print("Invalid input,please enter valid input") 
main()

