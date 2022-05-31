from classroom import Classroom


class SchoolBranch():

    def __init__(self, name: str, id_num: str, address: str,
                 public_transport: list, private_transport: list,
                 social_benefits: list, classroom_count: int = None):
        self.name = name
        self.address = address
        self.public_transport = public_transport
        self.private_transport = private_transport
        self.social_benefits = social_benefits
        self.classroom_list = []
        if(classroom_count == None):
            self.classroom_count = 0
        else:
            self.classroom_count = classroom_count
        if(id_num.isdigit()):
            self.id_num = id_num
        else:
            print("Invalid branch id format\n")
        print(f"New branch {self.name} created in {self.address}")

    def find_classroom(self, classroom: Classroom) -> int:
        found_ind = -1
        course_ind = 0
        while ((found_ind < 0) and (course_ind < self.classroom_count)):
            temp_course = self.classroom_list[course_ind]
            if(temp_course.name == classroom.name):
                print(
                    f"Classroom with same name was found at index {course_ind}\n")
                found_ind = course_ind
                return found_ind
            else:
                course_ind += 1
        return found_ind

    def add_classroom(self, new_classroom: Classroom):
        found_ind = SchoolBranch.find_classroom(self, new_classroom)
        if(found_ind == -1):
            self.classroom_list.append(new_classroom)
            self.classroom_count += 1
            print(
                f"{new_classroom.name} was added to {self.name} Branch")
            print(self.classroom_list)
        else:
            print(
                f"{new_classroom.name} does exist in {self.name} Branch so it couldn't be added")

    def delete_classroom(self, classroom: Classroom):
        for classroom_ind in range(len(self.classroom_list)):
            temp_course = self.classroom_list[classroom_ind]
            if(temp_course.name == classroom.name):
                found_ind = classroom_ind
                break
            else:
                found_ind = -1
        if(found_ind > -1):
            self.classroom_list.pop(found_ind)
            self.classroom_count -= 1
        else:
            print('Course was not found\n')

    def show_classrooms(self):
        print("\nClassroom List\n-------------------------------")
        for class_ind in range(self.classroom_count):
            temp_classroom = self.classroom_list[class_ind]
            f_str = f"Classroom: {temp_classroom.name} Capacity: {temp_classroom.capacity}"
            print(f_str)
        print("-------------------------------")
