class GPA:
    def calculate_gpa(marks, students):
        gpa_dict = {}
        for s in students:
            sid = s['id']
            total_marks = 0
            count = 0
            for key, value in marks.items():
                course_ID, student_ID = key
                if student_ID == sid:
                    total_marks += value
                    count += 1
            if count > 0:
                gpa = total_marks / count
                gpa_dict[sid] = gpa
            else:
                gpa_dict[sid] = None
        return gpa_dict
