students = [
    {"id": 1, "name": "Neev", "marks": 100},
    {"id": 2, "name": "Meet", "marks": 96},
    {"id": 3, "name": "Rudra", "marks": 70},
    {"id": 4, "name": "Ammar", "marks": 69},
    {"id": 5, "name": "Krish", "marks": 98},
]



while True :
    print("1. Add Student ")
    print("2. Display Student Detail")
    print("3. Update Student Detail")
    print("4. Remove the Student")
    print("5. Sort the Student List")
    print("6. Student who got more than 80 marks")
    print("7. Exit program ")

    choice = int(input("Enter Your Choice :"))

   
    if choice == 1:

     id = int(input("Enter New Student ID: "))

     found = False

     for s in students: 
        if s["id"] == id:
            found = True
            break

     if found:
        print("Student ID Already Exists!")

     else:
        name = input("Enter Your Name: ")
        marks = int(input("Enter Your Marks: "))

        newstudent = {
            "id": id,
            "name": name,
            "marks": marks
        }

        students.append(newstudent)

        print("New Student Added Successfully!")

        print(students)

    elif choice == 2:
       id=int(input("Enter Student ID :"))

       found=False

       for s in students:
          if s["id"]==id:
             print("Student Detail is here !")
             print("Id :",s["id"])
             print("name :",s["name"])
             print("marks :",s["marks"])
             found=True

       if not found:
          print("Student ID Doesn't Exist")


    elif choice == 3:
        id = int(input("Enter Student Id :"))

        found=False

        for s in students:
           if s["id"]== id:
              marks=int(input("Enter New Marks :"))
              s["marks"]=marks
              print("Marks Updated")
              found=True     
              print(s)

        if not found:
           print("Student Not Found !")     


    elif choice == 4:
        id=int(input("Enter Student Id to remove:"))

        for s in students:
           if s["id"]==id:
              students.remove(s)
              print("Student remove succesfully !")

        print(students)


    elif choice == 5:
        students.sort(key=lambda s:s["marks"],reverse=True)

        print(students)


    elif choice == 6 :
       for s in students:
          if s["marks"]>=80:
             print(s)

    elif choice == 7:
       break

    else:
       print("Invalid Choice . Please Enter between 1 to 7 !")
       
                 
               

       