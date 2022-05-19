from person import Person

class Teacher(Person):
    
    def __init__(self, person: Person, languages: tuple = (), available_branches: tuple = (), available_days: tuple = (), available_hours: tuple = ()):
        Person.__init__(self, person.name, person.surname, person.birthday, person.gender, person.mobile_phone, person.phone, person.email, person.address, person.syst_priv)
        self.languages = languages
        self.available_branches = available_branches
        self.available_days = available_days
        self.available_hours = available_hours

    def __del__(self):
        f_str1 = f"{self.name}" + ' ' + f"{self.surname}"
        print(f_str1 + ' was deleted')        