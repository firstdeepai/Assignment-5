# Task 1: Create a Dictionary of Student Marks

'''Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''

Student = {}
Student["Deepak"] = 97
Student["Vishesh"] = 85
Student["Mohit"] = 48

find = input("Enter the student's name: ").capitalize()
if find in Student:
    print(f"{find}'s marks: {Student[find]}")
else:
    print("student not found.")