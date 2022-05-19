from student import Student
from course import Course

class Classroom():
    
    def __init__(self, name, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
    
    def __del__(self):
        f_str1 = f"{self.name}"
        print('Classroom' + f_str1 + ' was deleted')      
        
    course_list = []
        
    def add_course(self, course: Course):
        self.course_list.append(course)