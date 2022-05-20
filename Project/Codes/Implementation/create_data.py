import person
import student
import worker
import teacher
import registrar
import information_system
import datetime

# Student1
name = 'Batuhan'
surname = 'Hangün'
id_number = '1111111'
birthday = datetime.date(1991, 8, 19)
gender = 'Male'
mobile_phone = '05336833244'
phone = '02129854478'
email = 'batuhan_hangun@mymail.com'
address = '59/5, Maslak, İstanbul'
person1 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
course_list = ['English', 'German']
course_levels = ['A1', 'B1']
payment_infos = [4, 5]
student1 = student.Student(
    person1, course_list, course_levels, payment_infos)

# Student2
name = 'Enes'
surname = 'Şanlı'
id_number = '2222222'
birthday = datetime.date(1991, 8, 19)
gender = 'Male'
mobile_phone = '05656833214'
phone = '02121234443'
email = 'esanli@esanli.com'
address = '45/3, Levent, İstanbul'
person2 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
course_list = ['German', 'Russian']
course_levels = ['A1', 'B1']
payment_infos = [5, 3]
student2 = student.Student(
    person2, course_list, course_levels, payment_infos)

# Student3
name = 'Yunus Emre'
surname = 'Selçuk'
id_number = '645643'
birthday = datetime.date(1973, 1, 5)
gender = 'Male'
mobile_phone = '05336765244'
phone = '021297654478'
email = 'yemreselcul@mymail.com'
address = '11/3, Bahçelievler, İstanbul'
person3 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
course_list = ['English', 'French']
course_levels = ['A1', 'B1']
payment_infos = [2, 1]
student3 = student.Student(
    person3, course_list, course_levels, payment_infos)

# Student4
name = 'Dennis'
surname = 'Ritchie'
id_number = '65434'
birthday = datetime.date(1945, 2, 8)
gender = 'Male'
mobile_phone = '05546731454'
phone = '021212654658'
email = 'ritchie_c@bell.labs.com'
address = '54/2, Florya, İstanbul'
person4 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
course_list = ['German', 'French']
course_levels = ['A1', 'B1']
payment_infos = [3, 5]
student4 = student.Student(
    person4, course_list, course_levels, payment_infos)

# Teacher1
name = 'Gregory'
surname = 'Ruslanov'
id_number = '12345546554'
birthday = datetime.date(1991, 3, 11)
gender = 'Male'
mobile_phone = '05335433244'
phone = '02129865478'
email = 'ruslanov_russian@mymail.com'
address = '21/3, Bebek, İstanbul'
person5 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
start_date = datetime.date(2010, 3, 12)
worker_role = 'Teacher'
worker1 = worker.Worker(person5, start_date, True, 30000, worker_role)
available_days = ["Monday", "Friday", "Thursday"]
available_hours = (("15:00", "16:00"), ("12:00", "14:00"), ("09:00"))
language_skills = ("Russian")
available_branches = ("Şişli", "Levent")
teacher1 = teacher.Teacher(person5, worker1, language_skills,
                           available_branches, available_days, available_hours)
teacher1.set_available_times()

# Teacher2
name = 'Friedrich'
surname = 'Schütze'
id_number = '1234312345454'
birthday = datetime.date(1970, 2, 4)
gender = 'Male'
mobile_phone = '053343653244'
phone = '021298657558'
email = 'schützefried@mymail.com'
address = '12/2, Taksim, İstanbul'
person6 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
start_date = datetime.date(2010, 3, 12)
worker_role = 'Teacher'
worker2 = worker.Worker(person6, start_date, True, 40000, worker_role)
available_days = ["Wednesday"]
available_hours = (("15:00", "16:00", "17:00"))
language_skills = ("German")
available_branches = ("Maslak", "Levent")
teacher2 = teacher.Teacher(person6, worker2, language_skills,
                           available_branches, available_days, available_hours)
teacher2.set_available_times()

# Teacher3
name = 'Jean'
surname = 'Jacque'
id_number = '1234545654554'
birthday = datetime.date(1970, 2, 4)
gender = 'Male'
mobile_phone = '053343653244'
phone = '021298657558'
email = 'schützefried@mymail.com'
address = '12/2, Taksim, İstanbul'
person7 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
start_date = datetime.date(2010, 3, 12)
worker_role = 'Teacher'
worker3 = worker.Worker(person7, start_date, True, 40000, worker_role)
available_days = ["Thursday", "Monday"]
available_hours = (("15:00", "16:00", "17:00"), ("09:00", "11:00"))
language_skills = ("French")
available_branches = ("Levent")
teacher3 = teacher.Teacher(person7, worker3, language_skills,
                           available_branches, available_days, available_hours)
teacher3.set_available_times()

# Teacher4
name = 'George'
surname = 'Micheal'
id_number = '1234545654554'
birthday = datetime.date(1965, 1, 3)
gender = 'Male'
mobile_phone = '053343653244'
phone = '021298657558'
email = 'georgemichael@mymail.com'
address = '12/2, Taksim, İstanbul'
person8 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
start_date = datetime.date(2010, 3, 12)
worker_role = 'Teacher'
worker4 = worker.Worker(person8, start_date, True, 40000, worker_role)
available_days = ["Monday", "Friday"]
available_hours = (("15:00", "17:00"), ("09:00"))
language_skills = ("English")
available_branches = ("Fatih")
teacher4 = teacher.Teacher(person8, worker4, language_skills,
                           available_branches, available_days, available_hours)
teacher4.set_available_times()

# Registrar1
name = 'Önder'
surname = 'Görmez'
id_number = '3333333'
birthday = datetime.date(1993, 2, 21)
gender = 'Male'
mobile_phone = '051236653244'
phone = '02129544878'
email = 'onder_gormez@mymail.com'
address = '66/2, Şişli, İstanbul'
person9 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
start_date = datetime.date(2010, 3, 12)
worker_role = 'Registrar'
worker5 = worker.Worker(person9, start_date, True, 40000, worker_role)
user_name = "ogormez"
user_password = "gormez*123-*"
registrar1 = registrar.Registrar(person9, worker5, user_name, user_password)

# SysAdmin1
name = 'Samuel'
surname = 'Jackson'
id_number = '3333333'
birthday = datetime.date(1960, 12, 21)
gender = 'Male'
mobile_phone = '051236653244'
phone = '02129544878'
email = 'SamuelJackson@mymail.com'
address = '66/2, Şişli, İstanbul'
person10 = person.Person(name, surname, id_number, birthday, gender,
                         mobile_phone, phone, email, address)
start_date = datetime.date(2010, 3, 12)
worker_role = 'Registrar'
worker6 = worker.Worker(person10, start_date, True, 40000, worker_role)
user_name = "jack_s"
user_password = "bad*546-mf*"
sysadmin1 = registrar.Registrar(person10, worker6, user_name, user_password)

# Init info. system
total_users = 10
total_branches = 0
information_system1 = information_system.InformationSystem(
    total_users, total_branches)

information_system1.student_list[0] = student1
information_system1.student_list[1] = student2
information_system1.student_list[2] = student3
information_system1.student_list[3] = student4

information_system1.worker_list[0] = worker1
information_system1.worker_list[1] = worker2
information_system1.worker_list[2] = worker3
information_system1.worker_list[3] = worker4
