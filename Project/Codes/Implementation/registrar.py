from person import Person
from worker import Worker


class Registrar(Worker, Person):

    def __init__(self, person: Person, worker: Worker, user_name: str, password: str):
        Person.__init__(self, person.name, person.surname, person.id_number, person.birthday, person.gender,
                        person.mobile_phone, person.phone, person.email, person.address, person.syst_priv)
        Worker.__init__(self, person, worker.start_date,
                        worker.active_worker, worker.salary, worker.worker_role)
        self.user_name = user_name
        self.password = password

    def __del__(self):
        f_str1 = f"{self.name} {self.surname}"
        print(f'{f_str1} was deleted')
