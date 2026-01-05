class Student:
    def input_info(students):
        x = int(input("Enter number of student: "))
        print("Enter the student ID, name and DoB")
        for i in range(int(x)):
            ID = int(input(""))
            name = input("")
            DoB = input("")
            student = {
                'id': ID,
                'name': name,
                'DoB': DoB
            }
            students.append(student)
    
    def __init__(self):
        self.student = []
        Student.input_info(self.student)
