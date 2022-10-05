# Silent Auction
# Dictionary and Nesting Tutorials
Number = 12345
Dictionary = {"Key": "Word", "KFC": "Chicken", Number: 123}
# print(Dictionary)
# print(Dictionary[Number])
# Dictionary are ordered from 3.7 onwards When we say that dictionaries are ordered, it means that the items have a
# defined order, and that order will not change. Unordered means that the items does not have a defined order,
# you cannot refer to an item by using an index. Changeable Dictionaries cannot have 2 keys with the same name

# add items to dictionary
Dictionary["My Key"] = "Add this to My Key"
# print(Dictionary)
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇 only the GRADES
for student in student_scores:  # student is the index
    student_grades[student] = student_scores[student]
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectation"
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
    elif student_scores[student] < 71:
        student_grades[student] = "Fail"
    else:
        print("Error")

# 🚨 Don't change the code below 👇
print(student_grades)
