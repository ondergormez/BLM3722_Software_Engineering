from student import Student
from teacher import Teacher
import datetime

class Course():
    def __init__(self, name: str, capacity: int, student_count: int, 
                 level: str, course_teacher: Teacher, classroom: str, 
                 date: datetime.date, student_list: tuple = (Student)
                 ) -> None:
        self.name = name
        self.capacity = capacity
        self.student_count = student_count
        self.level = level
        self.course_teacher = course_teacher
        self.classroom = classroom
        self.date = date
        self.student_list = student_list

    def __del__(self):
        f_str1 = f"{self.name}"
        print('Course' + f_str1 + ' was deleted')  
        
    def set_course_name(self, new_name: str):
        self.name = new_name
    
    def get_student_list(self):
        return self.student_list
    
    def show_students(self):
        for student in range(self.student_count):
            print(self.student_list(student))