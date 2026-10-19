students = [
    {"id": 101, "name": "Neev", "marks": 85},
    {"id": 102, "name": "Meet", "marks": 75},
    {"id": 103, "name": "Chintu", "marks": 90}
]

student_id=int(input("Enter Student ID for Search :"))

found= False

for student in students :
    if student["id"] == student_id:
        print("Here is the Student Detail :")
        print("Id",student["id"])
        print("Name",student["name"])
        print("marks",student["marks"])
        found=True

if not found :
    print("Student Id is not found")