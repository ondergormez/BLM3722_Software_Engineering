from classroom import Classroom 
class SchoolBranch():
    
    def __init__(self, name: str, address: str, 
                 public_transport: str, private_transport: str, 
                 social_benefits: str, classrooms: str) -> None:
                self.name = name
                self.address = address 
                self.public_transport = public_transport
                self.private_transport = private_transport
                self.social_benefits = social_benefits
                self.classrooms = classrooms       
