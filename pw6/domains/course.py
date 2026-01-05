class Course:
    def input_info(courses):
        y = int(input("Enter number of courses: \n"))
        print("Enter the course name and ID")
        for i in range(int(y)):
            course_name = input("")
            course_ID = int(input(""))
            course = {
                'id': course_ID,
                'name': course_name
            }
            courses.append(course)
    
    def __init__(self):
        self.course = []
        Course.input_info(self.course)
