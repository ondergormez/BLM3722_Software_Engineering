from classroom import Classroom


class SchoolBranch():

    classroom_list = list[Classroom]
    classroom_count = 0

    def __init__(self, name: str, address: str,
                 public_transport: str, private_transport: str,
                 social_benefits: str, classrooms: classroom_list) -> None:
        self.name = name
        self.address = address
        self.public_transport = public_transport
        self.private_transport = private_transport
        self.social_benefits = social_benefits
        self.classrooms = classrooms

    def add_classroom(self, new_classroom: Classroom):
        for classroom_ind in range(len(self.classrooms)):
            temp_classroom = self.classrooms[classroom_ind]
            if(temp_classroom != self):
                self.classrooms.append(temp_classroom)
                self.classroom_count += 1

    def show_classrooms(self):
        for class_ind in range(len(self.classrooms)):
            temp_classroom = self.classrooms[class_ind]
            f_str = f"{temp_classroom.name} \n"
            print(f_str)
