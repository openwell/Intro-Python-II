# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, r_name, r_description):
        self.r_name = r_name
        self.r_description = r_description

    def __str__(self):
        return f'Welcome to {self.r_name} \n {self.r_description}'
    
