class Student:
    def input_info(students):
        x = int(input("Enter number of student: "))
        print("Enter the student ID, name and DoB")
        for i  in range(int(x)):
            ID = int(input(""))
            name = input("")
            DoB = input("")
            student = {
                'id' : ID,
                'name' : name,
                'DoB' : DoB
            }
            students.append(student)
    
    def __init__(self):
        self.student = []
        Student.input_info(self.student)

class Course:
    def input_info(courses):
        y = int(input("Enter number of courses: \n"))
        print("Enter the course name and ID")
        for i in range(int(y)):
            course_name = input("")
            course_ID = int(input(""))
            course = {
                'id' : course_ID,
                'name' : course_name
            }
            courses.append(course)
    
    def __init__(self):
        self.course = []
        Course.input_info(self.course)

class Mark:
    def input_info(mark, course, student):
        if not course:
            print("You must enter courses first!\n")
            return
        
        print("Available courses")
        for c in course:
            print(f"ID: {c['id']}, Name: {c['name']}")
        while True:
            try:
                mark_ID = int(input("Enter course ID: "))
            except ValueError:
                print("Invalid ID.Try again.")
                continue
            found = False
            for c in course:
                if c['id'] == mark_ID:
                    found = True
                    break
            if found:
                break
            else:
                print(f"Course ID {mark_ID} not found.Try again.\n")

        print("Enter marks for students")
        for s in student:
            sid = s['id']
            while True:
                try:
                    mark_value = float(input(f"Mark for student {sid}: "))
                except ValueError:
                    print("Invalid mark.Enter a number")
                    continue
                if 0 <= mark_value <= 20:
                    mark[(mark_ID, sid)] = mark_value
                    break
                else:   
                    print("Mark must be between 0 and 20")

    def __init__(self, course, student):
        self.mark = {}
        Mark.input_info(self.mark, course, student)

def list_student(students):
    print("List of students: ")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['DoB']}")

def list_course(courses):
    print("List of courses: ")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def list_mark(marks):
    print("List of marks: ")
    for key, value in marks.items():
        course_ID, student_ID = key
        print(f"Course ID: {course_ID}, Student ID: {student_ID}, Mark: {value}")

Student_obj = Student()
Course_obj = Course()  
Mark_obj = Mark(Course_obj.course, Student_obj.student)
list_student(Student_obj.student)
list_course(Course_obj.course)
list_mark(Mark_obj.mark)