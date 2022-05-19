from person import Person


class Student(Person):

    def __init__(self, person: Person, courses: tuple = (), course_level: tuple = (), payment_infos: tuple = (int)):
        Person.__init__(self, person.name, person.surname, person.id_number, person.birthday, person.gender,
                        person.mobile_phone, person.phone, person.email, person.address, person.syst_priv)
        self.courses = courses
        self.course_level = course_level
        self.payment_infos = payment_infos

    def __str__(self):
        return (f"   Student Information\n" +
                f"----------------------------\n" +
                f"Name: {self.name}\n" +
                f"Surname: {self.surname}\n" +
                f"Gender: {self.gender}\n" +
                f"Mobile Phone: {self.mobile_phone}\n" +
                f"Phone: {self.phone}\n" +
                f"Email: {self.email}\n" +
                f"----------------------------\n")

    def get_course_list(self) -> tuple:
        tuple_len = len(self.courses)
        return (self.courses, tuple_len)

    def __del__(self):
        f_str1 = f"{self.name} {self.surname}"
        print(f'{f_str1} was deleted')

    def __eq__(self, other_object) -> bool:
        if isinstance(other_object, Student):
            if other_object.id_number == self.id_number:
                return True
        else:
            return False

    def display_student(self):
        f_str = f"{self.name} {self.surname} {self.id_number}"
        print(f_str)
