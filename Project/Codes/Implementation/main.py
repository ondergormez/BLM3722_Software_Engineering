import person
import datetime

name = 'Batuhan'
surname = 'Hangün'
birthday = datetime.datetime(1991, 8, 19)
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

