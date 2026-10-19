
students = [
    {"id": 101, "name": "Amit", "marks": 85},
    {"id": 102, "name": "Ravi", "marks": 75},
    {"id": 103, "name": "Neha", "marks": 90}
]

student_id = int(input("Enter student ID to remove: "))

found = False

for student in students:
    if student["id"] == student_id:
        students.remove(student)
        found = True
        print("Student removed ")
        

if not found:
    print("Student not found.")

print("Updated students list:")
print(students)
