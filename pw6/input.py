def write_student(students, filename="students.txt"):
    with open(filename, 'w') as f:
        f.write("ID,Name,DoB\n")
        for student in students:
            f.write(f"{student['id']},{student['name']},{student['DoB']}\n")
    print(f"Student data written to {filename}")


def write_course(courses, filename="courses.txt"):
    with open(filename, 'w') as f:
        f.write("ID,Name\n")
        for course in courses:
            f.write(f"{course['id']},{course['name']}\n")
    print(f"Course data written to {filename}")


def write_mark(marks, filename="marks.txt"):
    with open(filename, 'w') as f:
        f.write("CourseID,StudentID,Mark\n")
        for (course_id, student_id), mark_value in marks.items():
            f.write(f"{course_id},{student_id},{mark_value}\n")
    print(f"Mark data written to {filename}")


def get_student_input():
    from domains import Student
    student_obj = Student()
    write_student(student_obj.student)
    return student_obj

def get_course_input():
    from domains import Course
    course_obj = Course()
    write_course(course_obj.course)
    return course_obj

def get_mark_input(courses, students):
    from domains import Mark
    mark_obj = Mark(courses, students)
    write_mark(mark_obj.mark)
    return mark_obj
