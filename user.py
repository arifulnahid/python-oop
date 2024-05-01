from abc import ABC

class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
    
    def show_profile(self):
        raise NotImplementedError



    

    
        


