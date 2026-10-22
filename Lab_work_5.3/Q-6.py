students = [
    {"id": 101, "name": "Amit", "marks": 85},
    {"id": 102, "name": "Ravi", "marks": 75},
    {"id": 103, "name": "Neha", "marks": 90}
]


students.sort(key=lambda s:s["marks"],reverse=True)

print(students)