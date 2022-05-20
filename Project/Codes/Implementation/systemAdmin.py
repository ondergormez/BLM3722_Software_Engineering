from classroom import Classroom
from person import Person
from worker import Worker
from course import Course
from student import Student
from school_branch import SchoolBranch
from information_system import InformationSystem


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

    def add_new_course(self, branch: SchoolBranch, classroom: Classroom, new_course: Course):
        classroom_found = SchoolBranch.find_classroom(self, classroom)

        if(classroom_found == -1):
