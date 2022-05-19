from person import Person
from worker import Worker


class Teacher(Worker, Person):

    def __init__(self, person: Person, worker: Worker, languages: tuple = (), available_branches: tuple = (), available_days: tuple = (), available_hours: tuple = ()):
        Person.__init__(self, person.name, person.surname, person.id_number, person.birthday, person.gender,
                        person.mobile_phone, person.phone, person.email, person.address, person.syst_priv)
        Worker.__init__(self, person, worker.start_date,
                        worker.active_worker, worker.salary, worker.worker_role)
        self.languages = languages
        self.available_branches = available_branches
        self.available_days = available_days
        self.available_hours = available_hours

    def __str__(self):
        return (f"   Teacher Information\n" +
                f"----------------------------\n" +
                f"Name: {self.name}\n" +
                f"Surname: {self.surname}\n" +
                f"Mobile Phone: {self.mobile_phone}\n" +
                f"Phone: {self.phone}\n" +
                f"Email: {self.email}\n" +
                f"Languages: {self.languages}\n" +
                f"----------------------------\n")

    def __del__(self):
        f_str1 = f"{self.name} " + f"{self.surname}"
        print(f'{f_str1} was deleted')

    available_times = {
        'Monday': (),
        'Tuesday': (),
        'Wednesday': (),
        'Thursday': (),
        'Friday': (),
    }

    def set_available_times(self):
        tup_len = len(self.available_days)
        for key in range(tup_len):
            self.available_times[self.available_days[key]
                                 ] = self.available_hours[key]

    def get_available_times(self, day: str, hour: str) -> bool:
        if day in self.available_times:
            if hour in self.available_times[day]:
                return True
        else:
            return False
