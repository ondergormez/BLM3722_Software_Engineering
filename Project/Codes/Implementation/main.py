import person
import student
import worker
import datetime

name = 'Batuhan'
surname = 'Hangün'
birthday = datetime.date(1991, 8, 19)
gender = 'Male'
mobile_phone = '05336833244'
phone = '02129854478'
email = 'batuhan_hangun@mymail.com'
address = '59/5, Maslak, İstanbul'
syst_priv = True
person1 = person.Person(name, surname, birthday, gender, mobile_phone, phone, email, address, syst_priv)

print(person1, '\n')
mp, p, eml, addrss = person1.get_contact_info()
print(mp, p, eml, addrss, '\n')

student1 = student.Student(person1, ('English', 'German'), ('A1', 'B1'), (4, 5))

s1_course_list, total_courses = student1.get_course_list()
print(s1_course_list)


print(student1.payment_infos)
start_date = datetime.date(1991, 8, 19)
woker_role = 'Teacher'
worker1 = worker.Worker(person1, start_date, True, 30000, woker_role)

print(worker1.salary)
worker1.update_salary(50000)
print(worker1.salary)
worker1.end_contract()
print(worker1.end_date)
