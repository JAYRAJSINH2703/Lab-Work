students = [
    {"id": 101, "name": "Neev", "marks": 85},
    {"id": 102, "name": "Meet", "marks": 75},
    {"id": 103, "name": "Montu", "marks": 90}
]

Student_id=int(input("Enter Your student ID:"))
name=input("Enter Your Name :")
marks=int(input("Enter Your Marks :"))


student={
    "id":Student_id,
    "name":name,
    "marks":marks
}

students.append(student)


print("Updated Student List :")

print(students)