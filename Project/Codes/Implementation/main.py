from calendar import MONDAY
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
birthday = datetime.date(1991, 8, 19)
gender = 'Male'
mobile_phone = '05336833244'
phone = '02129854478'
email = 'batuhan_hangun@mymail.com'
address = '59/5, Maslak, İstanbul'
person1 = person.Person(name, surname, birthday, gender, mobile_phone, phone, email, address)

print(person1, '\n')
mp, p, eml, addrss = person1.get_contact_info()
print(mp, p, eml, addrss, '\n')

student1 = student.Student(person1, ('English', 'German'), ('A1', 'B1'), (4, 5))
print(student1)

# s1_course_list, total_courses = student1.get_course_list()
# print(s1_course_list)


# print(student1.payment_infos)
# start_date = datetime.date(1991, 8, 19)
# worker_role = 'Teacher'
# worker1 = worker.Worker(person1, start_date, True, 30000, worker_role)

# print('Old salary: ', worker1.salary)
# worker1.update_salary(50000)
# print('Old salary: ', worker1.salary)
# worker1.end_contract()
# print(worker1.end_date)


# available_days =  ("Monday", "Friday", "Thursday")
# available_hours = (("15:00", "16:00"), ("12:00", "14:00"), ("09:00"))
# language_skills = ("English")
# available_branches = ("Fatih", "Taksim")
# teacher1 = teacher.Teacher(person1, worker1, language_skills, available_branches, available_days, available_hours)


# teacher1.set_available_times()

# if teacher1.get_available_times("Friday", "12:00") == True:
#     print("SEKS\n")
# else:
#     print("NO SEKS\n")



# name = "English"
# capacity = 32
# student_count = 24
# level = "Advanced"
# course_teacher = teacher1
# classroom1 = 'A123'
# date = datetime.date(2022, 5, 15)
# course1 = course.Course(name, capacity, level, course_teacher, classroom1, date)

# print(course1)
