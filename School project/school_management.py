class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

   
    def get_id(self):
        return self.__student_id

   
    def enroll_student(self):
        if self.__is_enrolled:
            print("Error: Student is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"{self.__name} enrolled successfully.")

    
    def drop_student(self):
        if not self.__is_enrolled:
            print("Error: Student is not enrolled.")
        else:
            self.__is_enrolled = False
            print(f"{self.__name} dropped successfully.")

    
    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"

        print("------------------------------")
        print("Student ID :", self.__student_id)
        print("Name       :", self.__name)
        print("Department :", self.__department)
        print("Status     :", status)
        print("------------------------------")


s1 = Student(101, "Rup Das", "CSE")
s2 = Student(102, "Rahim", "EEE", True)
s3 = Student(103, "Karim", "BBA")




while True:

    print("\n====== Student Management System ======")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if len(StudentDatabase.student_list) == 0:
            print("No students found.")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif choice == "2":

        sid = int(input("Enter Student ID: "))

        found = False

        for student in StudentDatabase.student_list:
            if student.get_id() == sid:
                student.enroll_student()
                found = True
                break

        if not found:
            print("Error: Invalid Student ID.")

    elif choice == "3":

        sid = int(input("Enter Student ID: "))

        found = False

        for student in StudentDatabase.student_list:
            if student.get_id() == sid:
                student.drop_student()
                found = True
                break

        if not found:
            print("Error: Invalid Student ID.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")