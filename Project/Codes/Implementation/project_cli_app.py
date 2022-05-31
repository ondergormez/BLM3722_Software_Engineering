import helper_functions
import person
import student
import worker
import teacher
import registrar
import systemAdmin
import information_system
import course
import classroom
import school_branch
import datetime
import getpass

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

student_list = [student1, student2, student3, student4]
helper_functions.print_student_list(student_list)

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
available_days = ["Monday", "Thursday", "Friday"]
available_hours = [["15:00", "16:00"], ["12:00", "14:00"], ["09:00"]]
language_skills = ["Russian"]
available_branches = ["Şişli", "Levent"]
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
available_hours = [["15:00", "16:00", "17:00"]]
language_skills = ["German"]
available_branches = ["Maslak", "Levent"]
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
available_hours = [["15:00", "16:00", "17:00"], ["09:00", "11:00"]]
language_skills = ["French"]
available_branches = ["Levent"]
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
available_hours = [["15:00", "17:00"], ["09:00"]]
language_skills = ["English"]
available_branches = ["Fatih"]
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
user_password = "gormez*123"
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
worker_role = 'SystemAdmin'
worker6 = worker.Worker(person10, start_date, True, 40000, worker_role)
user_name = "jack_s"
user_password = "badmf1994"
sysadmin1 = systemAdmin.SystemAdmin(
    person10, worker6, user_name, user_password)

welcome_message_1 = f"{'Welcome to Bir Lisan Bir İnsan Automation System'}"
len_welcome_message = len(welcome_message_1)
helper_functions.print_star(len_welcome_message)
print(welcome_message_1)
helper_functions.print_star(len_welcome_message)
info_message_1 = f"{'Please select an operation'}"
print(info_message_1)
helper_functions.print_main_menu()
helper_functions.print_star(len_welcome_message)
correct_operation = False
while not correct_operation:
    operation_type = input("Selected operation: ")
    # System admin
    if operation_type == str(1):
        correct_operation = True
        print('Please login with your system admin username and password: ')
        login_status = sysadmin1.login_to_system()
        if login_status == True:
            info_message_2 = f"{'Select an operation to continue'}"
            print(info_message_2)
            helper_functions.print_system_admin_menu()
            correct_operation = False
            while not correct_operation:
                operation_type = input("Selected operation: ")
                if operation_type == str(1):
                    correct_operation = True
                    branch_name_new = input("Branch name: ")
                    branch_address_new = input("Branch address: ")
                    id_num_new = input("Branch ID number: ")
                    public_transport_new = input("Branch public transport: ")
                    private_transport_new = input("Branch private transport: ")
                    social_benefits_new = input("Branch social activities: ")
                    branch_newbranch = school_branch.SchoolBranch(
                        branch_name_new, id_num_new, branch_address_new, public_transport_new, private_transport_new, social_benefits_new)
                else:
                    print('Wrong operation type. Try again.')
    # Registrar
    elif operation_type == str(2):
        correct_operation = True
        print('Please login with your course registrar username and password: ')
        login_status = registrar1.login_to_system()
        if login_status == True:
            info_message_2 = f"{'Select an operation to continue'}"
            print(info_message_2)
            helper_functions.print_course_registrar_menu()
            correct_operation = False
            while not correct_operation:
                operation_type = input("Selected operation: ")
                if operation_type == str(1):
                    correct_operation = True
                    student_name_new = input("Name: ")
                    student_surname_new = input("Surname: ")
                    student_id_num_new = input("ID number: ")
                    student_birthday_new = input("Student birthday: ")
                    student_gender_new = input("Gender: ")
                    student_mobile_phone_new = input("Mobile phone: ")
                    student_phone_new = input("Phone: ")
                    student_email_new = input("E-mail address: ")
                    student_address_new = input("Address: ")
                    person_new__ = person.Person(student_name_new, student_surname_new, student_id_num_new, student_birthday_new, student_gender_new,
                                                 student_mobile_phone_new, student_phone_new, student_email_new, student_address_new)
                    student_course_new = input("Course name: ")
                    student_course_level = input("Level: ")
                    payment_info_new = input("Payment info: ")
                    student_new__ = student.Student(
                        person_new__, student_course_new, student_course_level, payment_info_new)
                    registrar1.add_new_student_to_branch(
                        student_new__, student_list)
                    helper_functions.print_student_list(student_list)
                else:
                    print('Wrong operation type. Try again.')
    else:
        print('Wrong operation type. Try again.')
