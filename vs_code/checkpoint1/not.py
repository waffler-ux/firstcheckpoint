import numpy as np
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))
marks_array = np.zeros((num_students, num_subjects))
student_names = []
for i in range(num_students):
    name = input(f"\nEnter the name for Student {i+1}: ")
    student_names.append(name)
    for r in range(num_subjects):
        mark = float(input(f"  Enter marks for Subject {r+1}: "))
        marks_array[i, r] = mark
        total_marks = np.sum(marks_array, axis=1)
        max_possible_marks = num_subjects * 100
percentages= (total_marks / max_possible_marks) * 100
grades = []
for pct in percentages:
    if pct >= 90:
        grades.append("A+")
    elif pct >= 80:
        grades.append("A")
    elif pct >= 70:
        grades.append("B+")
    elif pct >= 60:
        grades.append("B")
    elif pct >= 50:
        grades.append("C")
    else:
        grades.append("F")
        print("\n"+"=")
print(f"{'Student Name':<15} | {'Total Marks':<12} | {'Percentage (%)':<15} | {'Grade':<5}")
print("-" )

for i in range(num_students):
    print(f"{student_names[i]:<15} | {total_marks[i]:<12.2f} | {percentages[i]:<15.2f} | {grades[i]:<5}")
print("="*60)