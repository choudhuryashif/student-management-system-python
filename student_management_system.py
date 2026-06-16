class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

students = []
while True:


 print("----------Student Management System Menu----------")
 print("1. Add student")
 print("2. View students")
 print("3. Exit")


 choice=input("Select your option (1-3):")
 if choice == "1":
        student_name = input("Enter student name : ")
        age = input("Enter age : ")
        s1 = Student(student_name,age)
        students.append(s1)
        print("Added successfully !")

 elif choice == "2":
       if len(students) == 0:
            print("📌 No students found.")

       else: 
        print("\n----- Students -----")

        for i, student in enumerate(students, start=1):
                print(i, ". Name:", student.name,
                      "| Course:", student.course)

 elif choice == "3":
       print("Good By! Thanks for using Student Management System")
       break
 else:
       print("❌ Invalid choice! Please select 1, 2 or 3.")