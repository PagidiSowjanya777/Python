students = {}

while True:
    print("student management system")
    print("1.add a student")
    print("2.display students")
    print("3.search students")
    print("4.delete students")
    print("5.exit")
    choice = input("enter choice:")
    if choice == "1":
         roll = input("enter roll number:")
         name = input("enter name:")
         marks = float(input("enter marks:"))

         students[roll]={
             "name":name,
             "marks":marks
        }
         print("student added successfully")

    elif choice == "2":
        if not students:
            print("no record found")
        else:
            for roll,data in students.items():
                print("-----")
                print("roll")
                print("name",data["name"])
                print("marks",data["marks"])
    elif choice == "3":
         roll = input("Enter Roll Number: ")
         if roll in students:
            print(students[roll])
         else:
                print("Student Not Found")
    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Record Deleted Successfully!")
        else:
            print("Student Not Found")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
            
            




            
