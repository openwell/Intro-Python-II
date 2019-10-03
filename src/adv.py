from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
print(room['outside'])
# Make a new player object that is currently in the 'outside' room.


def hunted_house():
    c_player = Player('Toni', 'outside')
    current_room = c_player.c_room
    print(current_room)
    print('hi')
    def init_room(r_name):
        new_room = room[r_name]
        return new_room
    def alt_room_player(room):
        nonlocal current_room
        current_room = room
        print(current_room)
        c_player.set_c_room(room)
    def room_checker(direction):
        direc = direction.lower()
        if current_room == 'outside' and direc == 'n':
            alt_room_player('foyer')
        elif current_room == 'foyer' and direc == 's' or direc == 'n' or direc == 'e':
            if direc == 's':
                alt_room_player('outside')
            elif direc == 'n':
                alt_room_player('overlook')
            elif direc == 'e':
                alt_room_player('narrow')
        elif current_room == 'overlook' and direc == 's':
            alt_room_player('foyer')
        elif current_room == 'narrow' and direc == 'w' or direc == 'n':
            if direc == 'w':
                alt_room_player('foyer')
            elif direc == 'n':
                alt_room_player('treasure')
        elif current_room == 'treasure' and direc == 's':
            alt_room_player('narrow')
        else:
            print(f'🚫 incorrect direction for {current_room} room')
    while True:
        print('Welcome to the Hunted House 😄')
        print(init_room(current_room))
        print('For Movement n for ⬆️, w for ➡️, s for ⬇️, w for ⬅️ , q to quit')
        direction = input('kindly input your instruction:❓')
        if direction.lower() == 'n':
            room_checker(direction)
        elif direction.lower() == 'w':
            room_checker(direction)
        elif direction.lower() == 'e':
            room_checker(direction)
        elif direction.lower() == 's':
            room_checker(direction)
        elif direction.lower() == 'q':
            print('bye')
            break
        else:
            print('🚫 incorrect input kindly enter another')


hunted_house()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
