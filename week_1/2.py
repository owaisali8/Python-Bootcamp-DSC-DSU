def average(x):
    return sum(x)/len(x)


user_records = int(input("How many student records do you want to save: "))
student_list = {}
student_marks = []
total = 0
for i in range(user_records):
    roll_number = input("Enter roll number:")
    name = input("Enter name: ")
    age = input("Enter age: ")
    marks = int(input("Enter marks: "))
    while marks < 0 or marks > 100:
        print("Marks range should be between 0 and 100")
        marks = int(input("Enter correct marks: "))
    student_marks.append(marks)
    student_list[roll_number] = [name, age, marks]

print('\n')
print("{:<15} {:<15} {:<15} {:<15}".format(
    'Roll Number', 'Name', 'Age', 'Marks'))
print()
for k, v in student_list.items():
    name, age, marks = v
    print("{:<15} {:<15} {:<15} {:<15}".format(k, name, age, marks))

print("\nAverage: ", average(student_marks))
print("Highest: ", max(student_marks))
print("Lowest: ", min(student_marks))
