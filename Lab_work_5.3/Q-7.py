
students = [
    {"id": 101, "name": "Amit", "marks": 85},
    {"id": 102, "name": "Ravi", "marks": 75},
    {"id": 103, "name": "Neha", "marks": 90}
]

print("Student that got above 80 Marks :")

for student in students:
    if student["marks"]>80:
        print(student)