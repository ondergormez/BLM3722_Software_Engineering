from person import Person

class Student(Person):
    
    def __init__(self, person: Person, courses: tuple = (), course_level: tuple = (), payment_infos: tuple = (int)):
        Person.__init__(self, person.name, person.surname, person.birthday, person.gender, person.mobile_phone, person.phone, person.email, person.address, person.syst_priv)
        self.courses = courses
        self.course_level = course_level
        self.payment_infos = payment_infos

    def __str__(self):
         return    ( f"   Student Information\n"+
                     f"----------------------------\n"+
                     f"Name: {self.name}\n"+
                     f"Surname: {self.surname}\n"+
                     f"Gender: {self.gender}\n"+
                     f"Mobile Phone: {self.mobile_phone}\n"+
                     f"Phone: {self.phone}\n"+
                     f"Email: {self.email}\n"+
                     f"----------------------------\n")       
    
    def get_course_list(self) ->  tuple:
        tuple_len = len(self.courses)
        return (self.courses, tuple_len)
    
    def __del__(self):
        f_str1 = f"{self.name}" + ' ' + f"{self.surname}"
        print(f_str1 + ' was deleted')