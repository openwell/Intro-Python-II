# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, p_name, c_room):
        self.p_name = p_name
        self.c_room = c_room

    def __str__(self):
        return f'{self.p_name} \n {self.c_room}'

    def set_p_name(self, p_name):
        self.p_name = p_name

    def set_c_room(self, c_room):
        self.c_room = c_room
