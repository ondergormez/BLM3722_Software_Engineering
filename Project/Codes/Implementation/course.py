from student import Student
from teacher import Teacher
import datetime


class Course():

    student_list = list()
    student_count = 0

    def __init__(self, name: str, capacity: int,
                 level: str, course_teacher: Teacher, classroom: str,
                 date: tuple = ()
                 ) -> None:
        self.name = name
        self.capacity = capacity
        self.level = level
        self.course_teacher = course_teacher
        self.classroom = classroom
        self.day = date[0]
        self.hour = date[1]

    def __del__(self):
        f_str1 = f"{self.name}"
        print(f'Course {f_str1} was deleted')

    def set_course_name(self, new_name: str):
        self.name = new_name

    def find_student(self, student: Student) -> int:
        found_ind = -1
        student_ind = 0
        while found_ind < 0 and student_ind < self.student_count:
            temp_stud = self.student_list[student_ind]
            if(temp_stud.id_number == student.id_number):
                print(f"Found at index {student_ind}")
                found_ind = student_ind
                return found_ind
            else:
                student_ind += 1
        return found_ind

    def add_student(self, new_student: Student):
        found_ind = Course.find_student(self, new_student)

        if(found_ind == -1):
            self.student_list.append(new_student)
            self.student_count += 1
            print(
                f"{new_student.name} {new_student.surname} was added to {self.name}")
            print(self.student_list)
        else:
            print(
                f"{new_student.name} {new_student.surname} has already enrolled to this class\n")

    def delete_student(self, student: Student):
        found_ind = Course.find_student(self, student)
        # for student_ind in range(len(self.student_list)):
        #     temp_stud = self.student_list[student_ind]
        #     if(temp_stud.id_number == student.id_number):
        #         found_ind = student_ind
        #         break
        #     else:
        #         found_ind = -1
        if(found_ind > -1):
            self.student_list.pop(found_ind)
            self.student_count -= 1
            print(
                f"{student.name} {student.surname} was removed from {self.name} \n")
        else:
            print(f"{student.name} {student.surname} was not found\n")

    def get_student_list(self):
        return self.student_list

    def show_students(self):
        f_str = f"\nStudent List: {self.name}\n-------------------------"
        print(f_str)
        for student in range(self.student_count):
            Student.display_student(self.student_list[student])
        print("-------------------------")
        print('\n')

    def __str__(self):
        return f"Course Information\n-------------------------\nCourse Name: {self.name}\nCapacity: {self.student_count}/{self.capacity}\nLevel: {self.level}\nTeacher: {self.course_teacher.name} {self.course_teacher.surname}\nClassroom: {self.classroom}\nCourse Date: {self.day} {self.hour}\n-------------------------\n"

    def __eq__(self, other_object) -> bool:
        if isinstance(other_object, Course):
            if other_object.name == self.name:
                return True
        else:
            return False

    def check_course_time(self, other_object) -> bool:
        if isinstance(other_object, Course):
            if (other_object.day == self.day) and (other_object.hour == self.hour):
                return True
        else:
            return False
