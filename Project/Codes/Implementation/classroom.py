from student import Student
from course import Course


class Classroom():

    def __init__(self, name, capacity: int) -> None:
        self.name = name
        self.capacity = capacity

    def __del__(self):
        f_str1 = f"{self.name}"
        print(f'Classroom{f_str1} was deleted')

    course_list = []
    course_count = 0

    def add_course(self, course: Course):
        if(course.capacity <= self.capacity):
            self.course_list.append(course)
            self.course_count += 1

    def delete_course(self, course: Course):
        for course_ind in range(len(self.course_list)):
            temp_course = self.course_list[course_ind]
            if(temp_course.name == course.name):
                found_ind = course_ind
                break
            else:
                found_ind = -1
        if(found_ind > -1):
            del self.course_list[found_ind]
            self.course_count -= 1
        else:
            print('Course was not found\n')

    def show_courses(self):
        print("Course List\n-------------------------")
        for course_ind in range(self.course_count):
            temp_course = self.course_list[course_ind]
            print(
                f"Course: {temp_course.name} Capacity: {temp_course.student_count}/{self.capacity}")
        print('\n')
