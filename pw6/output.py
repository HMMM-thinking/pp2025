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


def list_gpa(gpa_dict):
    print("GPA of students: ")
    for sid, gpa in gpa_dict.items():
        if gpa is not None:
            print(f"Student ID: {sid}, GPA: {gpa:.2f}")
        else:
            print(f"Student ID: {sid}, GPA: N/A")
