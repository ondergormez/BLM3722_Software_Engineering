import datetime
from person import Person


class Worker(Person):

    def __init__(self, person: Person, start_date: datetime.date, active_worker: bool, salary: int, worker_role: str):
        Person.__init__(self, person.name, person.surname, person.id_number, person.birthday, person.gender,
                        person.mobile_phone, person.phone, person.email, person.address, person.syst_priv)
        self.start_date = start_date
        self.active_worker = active_worker
        self.salary = salary
        self.worker_role = worker_role

    def __del__(self):
        f_str1 = f"{self.name} {self.surname}"
        print(f'{f_str1} was deleted')

    def update_salary(self, new_salary: float):
        self.salary = new_salary

    def end_contract(self):
        self.end_date = datetime.date.today()
        f_str1 = f"{self.name} {self.surname}"
        print(f'{f_str1} stopped working in Bir Lisan Bir İnsan at ' +
              f"{self.end_date}")
