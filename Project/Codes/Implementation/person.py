import datetime

class Person():

    def __init__(self, name:str, surname:str, birthday:datetime.date, gender:str, mobile_phone:str, phone:str, email:str, address:str, syst_priv:bool):                              
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.gender = gender
        self.mobile_phone = mobile_phone
        self.phone = phone
        self.email = email
        self.address = address
        self.syst_priv = syst_priv
        
    def __str__(self):
        f_str1 = 'Name: ' + f"{self.name}"
        f_str2 = 'Surname: ' + f"{self.surname}"
        f_str3 = 'Birthday: ' + f"{self.birthday.strftime('%Y-%m-%d')}"
        f_str4 = 'Gender: ' + f"{self.gender}"
        f_str5 = 'Mobile Phone: ' + f"{self.mobile_phone}"
        f_str6 = 'Phone: ' + f"{self.phone}"
        f_str7 = 'Email: ' + f"{self.email}"
        f_str8 = 'Address: ' + f"{self.address}"     
        f_str9 = 'System Privilege: ' + f"{self.syst_priv}"
        f_str10 = f_str1 + '\n' + f_str2 + '\n'  + f_str3 + '\n'  + f_str4 + '\n'  + f_str5 + '\n'  + f_str6 + '\n'  + f_str7 + '\n'  + f_str8 + '\n'  + f_str9
        return f_str10
    
    def set_mobile_phone(self, new_mobile_phone: str):
        self.mobile_phone = new_mobile_phone
    
    def get_contact_info(self) -> tuple:
        mobile_phone = self.mobile_phone
        phone = self.phone
        email = self.email
        address = self.address       
        return (mobile_phone, phone, email, address)
    
    def __del__(self):
        f_str1 = f"{self.name}" + ' ' + f"{self.surname}"
        print(f_str1 + ' was deleted')