my_student = {
    'name' : 'Rolf Smith',
    'grades' : [70, 88, 90, 99],
    'average' : None#something here
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


class Student :
    def __init__(self, new_name, new_grades): #__init__ called dunder init, dunder means Double UNDERscores
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

print(student_one.average()) #print(Student.average(student_one))


