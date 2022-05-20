import person
import student
import worker
import teacher
import course
import classroom
import school_branch
import datetime

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
course_list = ('English', 'German')
course_levels = ('A1', 'B1')
payment_infos = (4, 5)
student1 = student.Student(
    person1, course_list, course_levels, payment_infos)
# print(student1)

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
course_list = ('German', 'Russian')
course_levels = ('A1', 'B1')
payment_infos = (5, 3)
student2 = student.Student(
    person2, course_list, course_levels, payment_infos)
# print(student2)


name = 'Gregory'
surname = 'Ruslanov'
id_number = '12345454'
birthday = datetime.date(1991, 3, 11)
gender = 'Male'
mobile_phone = '05335433244'
phone = '02129865478'
email = 'ruslanov_russian@mymail.com'
address = '21/3, Bebek, İstanbul'
person3 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
start_date = datetime.date(2010, 3, 12)
worker_role = 'Teacher'
worker1 = worker.Worker(person3, start_date, True, 30000, worker_role)
available_days = ["Monday", "Friday", "Thursday"]
available_hours = (("15:00", "16:00"), ("12:00", "14:00"), ("09:00"))
language_skills = ("Russian")
available_branches = ("Maslak", "Levent")
teacher1 = teacher.Teacher(person3, worker1, language_skills,
                           available_branches, available_days, available_hours)
teacher1.set_available_times()

# print(teacher1)


name = 'Friedrich'
surname = 'Schütze'
id_number = '12345454'
birthday = datetime.date(1970, 2, 4)
gender = 'Male'
mobile_phone = '05334333244'
phone = '02129865658'
email = 'schützefried@mymail.com'
address = '12/2, Taksim, İstanbul'
person4 = person.Person(name, surname, id_number, birthday, gender,
                        mobile_phone, phone, email, address)
start_date = datetime.date(2010, 3, 12)
worker_role = 'Teacher'
worker2 = worker.Worker(person4, start_date, True, 40000, worker_role)
available_days = ["Wednesday"]
available_hours = (("15:00", "16:00", "17:00"))
language_skills = ("German")
available_branches = ("Maslak", "Levent")
teacher2 = teacher.Teacher(person4, worker2, language_skills,
                           available_branches, available_days, available_hours)
teacher2.set_available_times()


classroom_name = "A134"
classroom_capacity = 32
classroom1 = classroom.Classroom(classroom_name, classroom_capacity)

name = "Russian"
capacity = 32
student_count = 24
level = "Advanced"
course_teacher = teacher1
course_class1 = classroom_name
date = ("Monday", "12:00")
course1 = course.Course(name, capacity, level,
                        course_teacher, course_class1, date)
print(course1)
course1.add_student(student1)
course1.add_student(student2)
course1.show_students()
print(course1)
course1.delete_student(student1)
course1.show_students()
print(course1)
course1.add_student(student1)
course1.show_students()
print(course1)

name = "German"
capacity = 32
student_count = 24
level = "Advanced"
course_teacher = teacher1
course_class2 = classroom1.name
date = ("Monday", "13:00")
course2 = course.Course(name, capacity, level,
                        course_teacher, course_class2, date)


print(course2)
course2.add_student(student1)
course2.add_student(student2)
course2.show_students()
print(course2)
course2.delete_student(student1)
course2.show_students()
print(course2)
course2.add_student(student1)
course2.show_students()
print(course2)

# classroom1.add_course(course1)
# classroom1.add_course(course2)
# classroom1.show_courses()
# classroom1.delete_course(course1)
# classroom1.show_courses()

if (course1.check_course_time(course2)):
    print("ÇAKIŞMA")
else:
    print("ÇAKIŞMA YOK")


print(f"course1 id: {id(course1)}")
print(f"course2 id: {id(course2)}")
print(f"course1.student_list id: {id(course1.student_list)}")
print(f"course2.student_list id: {id(course2.student_list)}")
