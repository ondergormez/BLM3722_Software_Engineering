from decimal import Clamped
from classroom import Classroom
from person import Person
from worker import Worker
from course import Course
from student import Student
from teacher import Teacher
from school_branch import SchoolBranch
from information_system import InformationSystem
import getpass


class SystemAdmin(Worker, Person):

    def __init__(self, person: Person, worker: Worker, user_name: str, password: str):
        Person.__init__(self, person.name, person.surname, person.id_number, person.birthday, person.gender,
                        person.mobile_phone, person.phone, person.email, person.address, person.syst_priv)
        Worker.__init__(self, person, worker.start_date,
                        worker.active_worker, worker.salary, worker.worker_role)
        self.user_name = user_name
        self.password = password

    def add_new_branch(self, information_system: InformationSystem, new_branch: SchoolBranch):
        information_system.branch_list.append(new_branch)

    def add_classroom(self, branch: SchoolBranch, new_classroom: Classroom):
        branch.add_classroom(new_classroom)

    def add_new_course(self, information_system: InformationSystem, branch: SchoolBranch, classroom: Classroom, new_course: Course, day: str, hour: str):

        classroom_found = SchoolBranch.find_classroom(branch, classroom)

        if(classroom_found == -1):
            print(f"{classroom.name} was not in the {branch.name}")
        else:
            Classroom.add_course(classroom, new_course, day, hour)
            # # Available_days içinde dolu olmayanları çek ve yeni liste oluştur

    num_attempts = 5

    def login_to_system(self) -> bool:
        while self.num_attempts != 0:
            user_name = input('Username: ')
            user_password = getpass.getpass('Password: ')
            if(user_name == str(self.user_name) and user_password == str(self.password)):
                print('Welcome', self.name)
                return True
            else:
                self.num_attempts = self.num_attempts - 1
                error_message = f"{'Wrong username or password. Try again. Number of attempts until lockout: '}" f"{self.num_attempts}"
                print(error_message)
            print(f"{'Out of login attempts. Lockedout...'}")
        return False
