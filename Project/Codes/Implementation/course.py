from student import Student
from teacher import Teacher
import datetime

class Course():
    def __init__(self, name: str, capacity: int, 
                 level: str, course_teacher: Teacher, classroom: str, 
                 date: datetime.date
                 ) -> None:
        self.name = name
        self.capacity = capacity
        self.level = level
        self.course_teacher = course_teacher
        self.classroom = classroom
        self.date = date

    def __str__(self):
        f_string =( f"   Course Information\n"+
                    f"-------------------------\n"+
                    f"Course Name: {self.name}\nCapacity: {self.capacity}\n"+
                    f"Level: {self.level}\nTeacher: {self.course_teacher.name} {self.course_teacher.surname}\n"+
                    f"Classroom: {self.classroom}\nCourse Date: {self.date}\n"+
                    f"-------------------------\n") 
        return f_string

    def __del__(self):
        f_str1 = f"{self.name}"
        print('Course ' + f_str1 + ' was deleted')  
        
    def set_course_name(self, new_name: str):
        self.name = new_name
    
    student_list = []
    
    student_count = 0

    
    def add_student(self, new_student: Student):
        self.student_list.append(new_student)
        self.student_count += 1
        
    def get_student_list(self):
        return self.student_list
    
    def show_students(self):
        for student in range(self.student_count):
            print(self.student_list[student])