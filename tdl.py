import json
tasks = []

def show_menu():
    print("\n To-Do List")
    print("1. show tasks")
    print("2.add task")
    print("3.delete task")
    print("4.mark task as done")
    print("5.exit")
    choice = input("choose action: ")
    return choice

def show_tasks():
    if not tasks:
        print("to-do list is empty")
    else:
        for i,task in enumerate(tasks,start=1):
            status = "✔" if task['completed'] else "✘"
            print(f'{i}. {task['title']} [{status}]')

def add_task():
    title = input('input the task title')
    tasks.append({"title": title, "completed": False})
    print(f"task '{title}' has been added")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Input the number of task for deleting."))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"task '{removed_task["title"]}' has been successfully deleted")
        else:
            print("task number is not correct")
    except ValueError:
        print("Please, type a correct number")

def complete_task():
    show_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Type the completed task number: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print(f"task '{tasks[task_number - 1]['title']}' marked as done.")
        else:
            print("task number is not correct")
    except ValueError:
        print("Please,type the correct number of the task")

def save_task():
    with open("tasks.json",'w', encoding="utf-8") as file:
        json.dump(tasks,file,ensure_ascii=False,indent=4)
        print("Tasks successfully saved!")

def load_task():
    try:
        with open("tasks.json","r",encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error while reading file. Starting from empty list.")
        return []

tasks = load_task()

while True:
    choice = show_menu()
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        save_task()
        print("Bye!")
        break
    else:
        print("choice is not correct.Try again")


