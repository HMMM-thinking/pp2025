from domains import Student, Course, Mark, GPA
from output import list_student, list_course, list_mark, list_gpa

def main():
    student_obj = Student()
    course_obj = Course()
    mark_obj = Mark(course_obj.course, student_obj.student)
    
    gpa_dict = GPA.calculate_gpa(mark_obj.mark, student_obj.student)
    
    list_student(student_obj.student)
    list_course(course_obj.course)
    list_mark(mark_obj.mark)
    list_gpa(gpa_dict)


if __name__ == "__main__":
    main()