
students = [
    {"id": 101, "name": "Neev", "marks": 85},
    {"id": 102, "name": "Meet", "marks": 75},
    {"id": 103, "name": "Mintu", "marks": 90}
]

student_id = int(input("Enter student ID: "))

found = False

for student in students:
    if student["id"] == student_id:
        mark = int(input("Enter new marks: "))
        student["marks"] = mark
        found = True
        print("Marks updated .")


if not found:
    print("Student not found.")

print("Updated students list:")
print(students)
