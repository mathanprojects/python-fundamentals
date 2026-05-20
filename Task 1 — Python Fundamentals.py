# ---------------------------------------------------
# 1. Number Classifier
# ---------------------------------------------------
    
# Positive, Negative, Zero

def number_classifier(num):

    if num > 0:
        print("The number is Positive")

    elif num < 0:
        print("The number is Negative")

    else:
        print("The number is Zero")
        
number_classifier(0)

# Function to check odd or even

def check_number(num):

    if num % 2 == 0:
        print("The number is Even")

    else:
        print("The number is Odd")


check_number(10)

# ---------------------------------------------------
# 2. FizzBuzz
# ---------------------------------------------------

def fizzbuzz():

    for i in range(1, 51):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)


fizzbuzz()

# ---------------------------------------------------
# 3. List Operations
# ---------------------------------------------------

numbers = [12, 45, 7, 23, 89, 34, 56, 90, 11, 67]


def find_sum(nums):

    total = 0

    for i in nums:
        total = total + i

    return total


def find_average(nums):

    total = find_sum(nums)

    average = total / len(nums)

    return average


def find_max(nums):

    maximum = nums[0]

    for i in nums:

        if i > maximum:
            maximum = i

    return maximum


def find_min(nums):

    minimum = nums[0]

    for i in nums:

        if i < minimum:
            minimum = i

    return minimum



print("List :", numbers)

print("Sum :", find_sum(numbers))

print("Average :", find_average(numbers))

print("Maximum :", find_max(numbers))

print("Minimum :", find_min(numbers))

# ---------------------------------------------------
# 4. Word Frequency Counter
# ---------------------------------------------------

sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1

    else:
        frequency[word] = 1

print("\nWord Frequency:")

for word in frequency:
    print(word, ":", frequency[word])
    
# ---------------------------------------------------
# 5. Student Grade Book
# ---------------------------------------------------

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
