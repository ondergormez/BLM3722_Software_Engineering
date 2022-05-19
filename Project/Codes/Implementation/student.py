from person import Person

class Student(Person):
    
    def __init__(self, person: Person, courses: tuple = (), course_level: tuple = (), payment_infos: tuple = (int)):
        Person.__init__(self, person.name, person.surname, person.birthday, person.gender, person.mobile_phone, person.phone, person.email, person.address, person.syst_priv)
        self.courses = courses
        self.course_level = course_level
        self.payment_infos = payment_infos

    def __str__(self):
        f_str1 = 'Name: ' + f"{self.name}"
        f_str2 = 'Surname: ' + f"{self.surname}"
        f_str3 = 'Birthday: ' + f"{self.birthday.strftime('%Y-%m-%d')}"
        f_str4 = 'Gender: ' + f"{self.gender}"
        f_str5 = 'Mobile Phone: ' + f"{self.mobile_phone}"
        f_str6 = 'Phone: ' + f"{self.phone}"
        f_str7 = 'Email: ' + f"{self.email}"
        f_str8 = 'Address: ' + f"{self.address}"     
        f_str9 = 'System Privilege: ' + f"{self.syst_priv}"
        f_str10 = f_str1 + '\n' + f_str2 + '\n'  + f_str3 + '\n'  + f_str4 + '\n'  + f_str5 + '\n'  + f_str6 + '\n'  + f_str7 + '\n'  + f_str8 + '\n'  + f_str9
        return f_str10
    
    def get_course_list(self) ->  tuple:
        tuple_len = len(self.courses)
        return (self.courses, tuple_len)
    
    def __del__(self):
        f_str1 = f"{self.name}" + ' ' + f"{self.surname}"
        print(f_str1 + ' was deleted')