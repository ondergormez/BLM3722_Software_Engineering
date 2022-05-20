import datetime


class Person():

    def __init__(self, name: str, surname: str, id_number: str, birthday: datetime.date, gender: str, mobile_phone: str, phone: str, email: str, address: str, syst_priv: bool = False):
        self.name = name
        self.surname = surname
        self.id_number = id_number
        self.birthday = birthday
        self.gender = gender
        self.mobile_phone = mobile_phone
        self.phone = phone
        self.email = email
        self.address = address
        self.syst_priv = syst_priv

    def set_mobile_phone(self, new_mobile_phone: str):
        self.mobile_phone = new_mobile_phone

    def get_contact_info(self) -> tuple:
        mobile_phone = self.mobile_phone
        phone = self.phone
        email = self.email
        address = self.address
        return (mobile_phone, phone, email, address)

    def __del__(self):
        f_str1 = f"{self.name} {self.surname}"

    def __eq__(self, other_object) -> bool:
        if isinstance(other_object, Person):
            if other_object.id_number == self.id_number:
                return True
        else:
            return False
