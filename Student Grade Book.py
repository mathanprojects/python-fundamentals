# Student Grade Book

students = {
    "Arun": 95,
    "Bala": 82,
    "Charan": 67,
    "Divya": 45,
    "Esha": 76
}

def find_topper(data):

    topper = ""
    highest = 0

    for name in data:

        if data[name] > highest:
            highest = data[name]
            topper = name

    print("Topper :", topper)
    print("Highest Mark :", highest)

def class_average(data):

    total = 0

    for mark in data.values():
        total = total + mark

    average = total / len(data)

    print("Class Average :", average)

def print_grades(data):

    print("\nStudent Grades:")

    for name, mark in data.items():

        if mark >= 90:
            grade = "A"

        elif mark >= 70:
            grade = "B"

        elif mark >= 50:
            grade = "C"

        else:
            grade = "F"

        print(name, ":", mark, "-", grade)


find_topper(students)

class_average(students)

print_grades(students)