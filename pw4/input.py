def get_student_input():
    from domains import Student
    return Student()

def get_course_input():
    from domains import Course
    return Course()

def get_mark_input(courses, students):
    from domains import Mark
    return Mark(courses, students)

