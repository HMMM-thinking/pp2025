class Mark:
    def check_cid(course):
        while True:
            try:
                mark_ID = int(input("Enter course ID: "))
            except ValueError:
                print("Invalid ID.Try again.")
                continue
            if any(c['id'] == mark_ID for c in course):
                return mark_ID
            else:
                print(f"Course ID {mark_ID} not found.Try again.\n")

    def check_mark(mark, course_id, student):
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
                    mark[(course_id, sid)] = mark_value
                    break
                else:
                    print("Mark must be between 0 and 20")
    
    def input_info(mark, course, student):
        if not course:
            print("You must enter courses first!\n")
            return
        
        print("Available courses")
        for c in course:
            print(f"ID: {c['id']}, Name: {c['name']}")
        
        while True:
            course_id = Mark.check_cid(course)
            Mark.check_mark(mark, course_id, student)

            another = input("Enter mark for another course? (yes/no): ").lower()
            if another not in ['yes', 'y']:
                break

    def __init__(self, course, student):
        self.mark = {}
        Mark.input_info(self.mark, course, student)
