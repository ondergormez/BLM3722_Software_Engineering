from person import Person
from student import Student
from worker import Worker
from teacher import Teacher
from course import Course
from classroom import Classroom
from registrar import Registrar
from systemAdmin import SystemAdmin
from school_branch import SchoolBranch
from information_system import InformationSystem
import datetime
import unittest


class TestId(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass ")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")

        # Öğrenci nesnesi oluşturma
        self.person1 = Person('Batuhan', 'Hangün', '1111111', datetime.date(
            1991, 8, 19), 'Male', '05336833244', '02129854478', 'batuhan_hangun@mymail.com', '59/5, Maslak, İstanbul')
        self.student1 = Student(
            self.person1, ('English', 'German'), ('A1', 'B1'), (4, 5))

        # Öğretmen nesnesi oluşturma
        self.person2 = Person('Gregory', 'Ruslanov', '12345546554', datetime.date(1991, 3, 11), 'Male',
                              '05335433244', '02129865478', 'ruslanov_russian@mymail.com', '21/3, Bebek, İstanbul')
        self.worker1 = Worker(self.person2, datetime.date(
            2010, 3, 12), True, 30000, 'Teacher')
        self.teacher1 = Teacher(self.person2, self.worker1, ["Russian"],
                                ["Şişli", "Levent"], ["Monday", "Thursday", "Friday"], [["15:00", "16:00"], ["12:00", "14:00"], ["09:00"]])
        self.teacher1.set_available_times()

        # Kayıt Görevlisi nesnesi oluşturma
        self.person3 = Person('Önder', 'Görmez', '3333333', datetime.date(1993, 2, 21), 'Male',
                              '051236653244', '02129544878', 'onder_gormez@mymail.com', '66/2, Şişli, İstanbul')
        self.worker2 = Worker(self.person3, datetime.date(
            2010, 3, 12), True, 40000, 'Registrar')
        self.registrar1 = Registrar(
            self.person3, self.worker2, "ogormez", "gormez*123-*")

        # Admin nesnesi oluşturma
        self.person4 = Person('Samuel', 'Jackson', '3333333', datetime.date(1960, 12, 21), 'Male',
                              '051236653244', '02129544878', 'SamuelJackson@mymail.com', '66/2, Şişli, İstanbul')
        self.worker3 = Worker(self.person4, datetime.date(
            2010, 3, 12), True, 40000, 'Admin')
        self.sysadmin1 = SystemAdmin(
            self.person4, self.worker3, "jack_s", "bad*546-mf*")

        # Classroom nesnesi oluşturma
        self.classroom1 = Classroom(
            "A134", 32, ["Monday", "Friday"], [["15:00", "17:00"], ["09:00"]])
        self.classroom1.set_available_times()

        # Şube nesnesi oluşturma ve class ekleme
        self.branch1 = SchoolBranch(
            "Maslak", "543463", "Ayazağa, 34/2", "41AT, 500T, 41ST", ["E6 Otoyolu", "E5 Otoyolu"], ["Langırt", "PS5"])
        self.branch1.add_classroom(self.classroom1)

        # Course nesnesi oluşturma
        self.course1 = Course("Russian", 32, level="A1")

        # Information System nesnesi oluşturma
        self.information_system1 = InformationSystem(
            10, 4)

        # Oluşturulan Information System nesnese öğretmen ekleme
        self.information_system1.teacher_list.append(self.teacher1)

    def tearDown(self):
        print("tearDown\n")

    def test_update_salary(self):
        print("test_update_salary")
        self.assertEqual(self.worker1.update_salary(40000), 40000)

    def test_update_id(self):
        print("test_update_id")
        self.assertEqual(self.student1.update_id("1111112"), "1111112")

    def test_coursename_update(self):
        print("test_coursename_update")
        self.course1.set_course_name("English")
        self.assertEqual(self.course1.name, "English")

    def test_set_mobile_phone(self):
        print("test_set_mobile_phone")
        self.person1.set_mobile_phone("05336833243")
        self.assertEqual(self.person1.mobile_phone, "05336833243")

    def test_get_contact_info(self):
        print("test_get_contact_info")
        self.assertEqual(self.person1.get_contact_info(
        ), ("05336833244", "02129854478", "batuhan_hangun@mymail.com", '59/5, Maslak, İstanbul'))

    def test_update_email(self):
        print("test_update_email")
        self.assertEqual(self.student1.update_email(
            "batuhanhangun@mymail.com"), "batuhanhangun@mymail.com")

    def test_get_course_list(self):
        print("test_get_course_list")
        tuple_len = len(self.student1.courses)
        self.assertEqual(self.student1.get_course_list(),
                         (self.student1.courses, tuple_len))

    def test_find_teacher(self):
        print("test_find_teacher")
        self.assertEqual(self.teacher1.find_teacher(self.information_system1.get_teacher_list(
        ), "Monday"), self.information_system1.get_teacher_list())

    def test_update_name(self):
        print("test_update_name")
        self.assertEqual(self.student1.update_name("Dogan"), "Dogan")

    def test_get_teacher_list(self):
        print("test_get_teacher_list")
        self.assertEqual(self.information_system1.get_teacher_list(),
                         self.information_system1.teacher_list)


if __name__ == '__main__':
    unittest.main()
