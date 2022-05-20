from student import Student
from course import Course


class Classroom():

    def __init__(self, name, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.course_list = []
        self.course_count = 0

    def __del__(self):
        f_str1 = f"{self.name}"
        print(f'Classroom{f_str1} was deleted')

    def find_course(self, course: Course) -> int:
        found_ind = -1
        course_ind = 0
        while found_ind < 0 and course_ind < self.course_count:
            temp_course = course.course_list[course_ind]
            if((temp_course == self.name)):
                print(
                    f"Course with same name was found at index {course_ind}\n")
                found_ind = course_ind
                return found_ind
            else:
                course_ind += 1
        return found_ind

    def add_course(self, new_course: Course):
        found_ind = Classroom.find_course(self, new_course)
        time_status = Classroom.check_course_time(self, new_course)

        if((found_ind == -1) and (time_status != True)):
            print(self.course_list)
            self.course_list.append(new_course)
            self.course_count += 1
            print(
                f"{new_course.name} was opened in {self.name} at {new_course.day} {new_course.hour}\n")
        else:
            print(
                f"{new_course.name} has already opened in {self.name}\n")
        self.course_list.append(new_course)
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
            self.course_list.pop(found_ind)
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

    def __eq__(self, other_object) -> bool:
        if isinstance(other_object, Classroom):
            if other_object.name == self.name:
                return True
        else:
            return False

    def __ne__(self, other_object) -> bool:
        return self.name != other_object.name
