from room import Room
from player import Player
from item import Item
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


# Link items to rooms

item = {
    'book': Item("Book", "A piece to take notes"),
    'sword': Item("Sword", "A weapon to fight enemies"),
    'amulet': Item("Amulet", "A good luck charm"),
    'knife': Item("Knife", "a tool with a cutting edge or blade attached to a handle"),
    'laptop': Item("Laptop", "a computer that is portable and suitable for use while travelling."),
    'phone': Item("Phone", "system for transmitting voices over a distance using wire or radio"),
    'guitar': Item("Guitar", "a stringed musical instrument")
}


room['outside'].items = [
    item['book'],
    item['sword']
]

room['foyer'].items = [
    item['amulet'],
    item['knife'],
]

room['overlook'].items = [
    item['laptop'],
]

room['narrow'].items = [
    item['phone']
]

room['treasure'].items = [
    item['guitar']
]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
tom = Player("tom", room['outside'])
def printInstructions():
    print('**************************')
    print('* Please input direction to go or action to take')
    print('* Allowed directions are: \n'
            + '*  n to move north\n'
            + '*  s to move south\n'
            + '*  w to move west\n'
            + '*  e to move east')
    print('* Allowed actions are \n* `get item` or `take item` to pick an item\n'
            + '* `drop item` to put an item from your inventory into a room\n' 
            + '* i or inventory to show items in your inventory\n'
            + '* l or list to show items in current room\n'
            + '* where `item` is the name of the item you want to pick or drop')
    print('**************************')

print('\n  **Welcome to The Adventure Game\n')
printInstructions()
print(tom.getCurrentRoom())

while True:
    user_input = input('\nInput direction to go or action to do: ')
    splitted_user_input = user_input.split(' ')
    if len(splitted_user_input) == 2:
        if splitted_user_input[0] == 'take' or splitted_user_input[0] == 'get':
            # check if item exist in current room
            item_exist = False
            for i in tom.getCurrentRoom().items:
                if i.name.lower() == splitted_user_input[1].lower():
                    item_exist = True
            if item_exist:
                # add item to player inventory
                tom.items.append(item[splitted_user_input[1].lower()])
                item[splitted_user_input[1].lower()].on_take()
                # and remove from room
                tom.getCurrentRoom().items.remove(item[splitted_user_input[1].lower()])
            else:
                print(splitted_user_input[1].capitalize() + ' is not in this room')
        elif splitted_user_input[0] == 'drop':
            item_exist = False
            # check if item exist in player's inventory
            for i in tom.items:
                if i.name.lower() == splitted_user_input[1].lower():
                    item_exist = True
            if item_exist:
                # remove item from player inventory
                tom.items.remove(item[splitted_user_input[1].lower()])
                item[splitted_user_input[1].lower()].on_drop()
                # and add it to the room
                tom.getCurrentRoom().items.append(item[splitted_user_input[1].lower()])
            else:
                print(splitted_user_input[1].capitalize() + ' is not in your inventory')
        else:
            print('Wrong Input. Please use get, take or drop keyword with an item')
    elif user_input == "i" or user_input == "inventory":
        tom.printInventory()
    elif user_input == "l" or user_input == "list":
        print("\nItems in this room: " + tom.getCurrentRoom().items_str())
    elif user_input == "n":
        if hasattr(tom.getCurrentRoom(), 'n_to'):
            tom.setCurrentRoom(tom.getCurrentRoom().n_to)
            print(tom.getCurrentRoom())
        else:
            print(f"\nSorry there is nothing up north...\n")
    elif user_input == "w":
        if hasattr(tom.getCurrentRoom(), 'w_to'):
            tom.setCurrentRoom(tom.getCurrentRoom().w_to)
            print(tom.getCurrentRoom())
        else:
            print(f"\nSorry there is nothing to the west...\n")
    elif user_input == "s":
        if hasattr(tom.getCurrentRoom(), 's_to'):
            tom.setCurrentRoom(tom.getCurrentRoom().s_to)
            print(tom.getCurrentRoom())
        else:
            print(f"\nSorry there is nothing down south...\n")
    elif user_input == "e":
        if hasattr(tom.getCurrentRoom(), 'e_to'):
            tom.setCurrentRoom(tom.getCurrentRoom().e_to)
            print(tom.getCurrentRoom())
        else:
            print(f"\nSorry there is nothing to the east...\n")
    elif user_input == "q":
        print('\nThanks for playing... Come back for more fun\n')
        break
    else:
        print('Wrong Input!!!\n Please input direction to go or action to take')
        printInstructions()
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
