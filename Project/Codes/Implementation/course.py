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

    def __del__(self):
        f_str1 = f"{self.name}"
        print(f'Course {f_str1} was deleted')

    def set_course_name(self, new_name: str):
        self.name = new_name

    student_list = []

    student_count = 0

    def add_student(self, new_student: Student):
        self.student_list.append(new_student)
        self.student_count += 1

    def delete_student(self, student: Student):
        for student_ind in range(len(self.student_list)):
            temp_stud = self.student_list[student_ind]
            if(temp_stud.id_number == student.id_number):
                found_ind = student_ind
                break
            else:
                found_ind = -1
        if(found_ind > -1):
            del self.student_list[found_ind]
            self.student_count -= 1
        else:
            print('Student was not found\n')

    def get_student_list(self):
        return self.student_list

    def show_students(self):
        print("Student List\n-------------------------")
        for student in range(self.student_count):
            Student.display_student(self.student_list[student])
        print('\n')

    def __str__(self):
        return f"Course Information\n-------------------------\nCourse Name: {self.name}\nCapacity: {self.student_count}/{self.capacity}\nLevel: {self.level}\nTeacher: {self.course_teacher.name} {self.course_teacher.surname}\nClassroom: {self.classroom}\nCourse Date: {self.date}\n-------------------------\n"
