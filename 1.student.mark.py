student = []
course = []
mark = {}

def input_student():
    x = int(input("Enter the number of students: "))
    print("Enter student ID, name, and date of birth: ")
    for i in range(x):
        ID = int(input(""))
        name = input("")
        DoB = input("")
        student.append({'ID': ID, 'name': name, 'DoB': DoB})

def input_course():
    y = int(input("Enter the number of courses: \n"))
    print("Enter course name and ID: ")
    for i in range(y):
        course_name = input("")
        course_ID = int(input(""))
        course.append({'ID': course_ID, 'name': course_name})

def input_mark():
    if not course:
        print("You must enter courses first!\n")
        return
    
    print("Available courses")
    for c in course:
        print(f"ID: {c['ID']}, Name: {c['name']}")
    while True:
        try:
            mark_ID = int(input("Enter course ID: "))
        except ValueError:
            print("Invalid ID. Try again.")
            continue
        found = False
        for c in course:
            if c['ID'] == mark_ID:
                found = True
                break
        if found:
            break
        else:
            print(f"Course ID {mark_ID} not found. Try again.\n")

    print("Enter marks for students")
    for s in student:
        sid = s['ID']
        while True:
            try:
                mark_value = float(input(f"Mark for student {sid}: "))
            except ValueError:
                print("Invalid mark. Enter a number.")
                continue
            if 0 <= mark_value <= 20:
                mark[(mark_ID, sid)] = mark_value
                break
            else:
                print("Mark must be between 0 and 20")

def list_student():
    print("List of students: \n")
    for s in student:
        print(f"ID: {s['ID']}, Name: {s['name']}, DoB: {s['DoB']}")

def list_course():
    print("List of courses: \n")
    for c in course:
        print(f"ID: {c['ID']}, Name: {c['name']}")

def showcase_mark():
    course_ID = int(input("Course ID to show marks: \n"))
    print(f"Marks for course ID {course_ID}: \n")
    for s in student:
        sid = s['ID']
        if (course_ID, sid) in mark:
            print(f"Student ID: {sid}, Mark: {mark[(course_ID, sid)]}")
        else:
            print(f"Student ID: {sid}, Mark: Not available")
            return

def main():
    input_student()
    input_course()
    input_mark()
    list_student()
    list_course()
    showcase_mark()

if __name__ == "__main__":
    main()