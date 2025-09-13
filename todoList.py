#1. Create a To-Do List App where users can add, view, mark done, and delete tasks.

tasks = []

def show_tasks():
    print("Your Todo List here!!")
    if not tasks:
        print("No tasks yet!")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def add_tasks():
    task = input("Enter the task: ")
    tasks.append(task)

def mark_done():
    show_tasks()
    num = int(input("Task number you want to mark done: ")) -1
    if 0 <= num < len(tasks):
        tasks[num] += "***"

def delete_task():
    show_tasks()
    num = int(input("Task number you want to delete: ")) -1
    if 0 <= num < len(tasks):
        tasks.pop(num)


def todoList():
    while True:
        print("\n1. Add Task")
        print("2. Mark Done")
        print("3. Delete Task")
        print("4. View Task")
        print("5. Exit")


        choice = input("Enter the choice: ")
        if choice == "1":
            add_tasks()
        elif choice == "2":
            mark_done()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            print("All Done")
            break
        else:
            print("Invalid choice!")
todoList()


#2. Build a Contact Book to store, view, update, and delete contact names and numbers.
#3. Make a Student Gradebook to enter marks for students and display averages, highest, and lowest marks.
#4. Design a Library Book Tracker to add, issue, return, and view books.
#5. Create a Python program that replaces certain words in a text with emojis.
#6. Make a Quiz App with multiple choice questions and scoring.
#7. Build a Shopping Cart System to add/remove items and calculate total cost.