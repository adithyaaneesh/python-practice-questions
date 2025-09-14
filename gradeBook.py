#3. Make a Student Gradebook to enter marks for students and display averages, highest, and lowest marks.

student_grade = []
def add_mark():
    stud_name = str(input("Enter the student name: "))
    stud_mark = int(input("Enter the student mark: "))
    data = {
        "Name" : stud_name,
        "Mark" : stud_mark
    }
    student_grade.append(data)
    print("Mark added!!")

def display_student():
    if not student_grade:
        print("Not student mark entered!!")
    else:
        for i in range(len(student_grade)):
            print(f"{i+1}. {student_grade[i]['Name']} - {student_grade[i]['Mark']}")

def display_average():
    if not student_grade:
        print("No marks added!!")
    else:
        total = 0
        for i in range(len(student_grade)):
            total += student_grade[i]["Mark"]
        avg = total / len(student_grade)
        print(f"Average Mark: {avg:.2f}")

def display_highest():
    if not student_grade:
        print("No marks added!!")
    else:
        highest = student_grade[0]
        for i in range(len(student_grade)):
            if student_grade[i]["Mark"] > highest["Mark"]:
                highest = student_grade[i]
        print(f"Highest Mark: {highest['Name']} - {highest['Mark']}")

def display_lowest():
    if not student_grade:
        print("No marks added!!")
    else:
        lowest = student_grade[0]
        for i in range(len(student_grade)):
            if student_grade[i]["Mark"] < lowest["Mark"]:
                lowest = student_grade[i]
        print(f"Lowest Mark: {lowest['Name']} - {lowest['Mark']}")

def stud_grade():
    while True:
        print("\nStudent Grade Book")
        print("1.Add Mark")
        print("2.Students")
        print("3.Average Mark")
        print("4.Highest Mark")
        print("5.Lowest Mark")
        print("6.Exit")

        choice = int(input("Enter your choice: "))


        

        if choice == 1:
            add_mark()
        elif choice == 2:
            display_student()
        elif choice == 3:
            display_average()
        elif choice == 4:
            display_highest()
        elif choice == 5:
            display_lowest()
        elif choice == 6:
            print("Exiting from Grade Book *")
            break
        else:
            print("Invalid Choice")
stud_grade()
