class student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
  
  sorted_students = sorted(student_list,
                key=lambda student: student.cgpa,
                reverse=True)
  
  return sorted_students


Students = [
    Student("hari", "A123", 7.8),
    Student("srikanth", "A124", 8.9),
    Student("samuya", "A125", 9.1),
    Student("mahidhar", "A126", 9.9),
]
sorted_students = sort_student(students)


for student in sorted_student:
  print("Name:{},Roll Number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))
               