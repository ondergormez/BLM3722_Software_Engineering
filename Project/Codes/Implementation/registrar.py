from person import Person
from worker import Worker
from course import Course
from student import Student
import getpass


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

    def add_new_student_to_branch(self, new_student: Student, branch_student_list: list):
        branch_student_list.append(new_student)

    def add_student_to_course(self, new_student: Student, course: Course):
        Course.add_student(course, new_student)

    def register_payment(self, student: Student, course_name: str):
        student.payment_infos[student.courses == course_name] += 1

    num_attempts = 5

    def login_to_system(self) -> bool:
        while self.num_attempts != 0:
            user_name = input('Username: ')
            # input('Password: ')
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
