# Important imports 
from room import Room
from character import Enemy 
from character import Friend
from item import Item

# Add a truth condition to ...?
dead = False

# Setting up the rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("Ballroom")
ballroom.set_description("A big oval shaped room decorated with baroque style golden ornamentation and mirrors")

dining_hall = Room("Dining hall")
dining_hall.set_description("A candle-lit room with stone floors, wooden furniture, and a fire place")

# Linking rooms to each other 
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Creating the instance of Elsa
elsa = Friend("Elsa", "A gentle friendly ghost")
# Putting Elsa in the ballroom
ballroom.set_character(elsa)
# Setting up Elsa's convo
elsa.set_conversation("Hello, my name is Elsa. Are you lost?")
elsa.set_inventory("hug")

# Creating the instance of good old Dave 
dave = Enemy("Dave", "A smelly zombie")
# Putting Dave in the dining hall
dining_hall.set_character(dave)
# Setting Dave's convo + fight
dave.set_conversation("Hi my name is Dave. How about I eat your brain?")
dave.set_weakness("beer")
dave.set_inventory("beer")
dave.steal("beer")

# Removed the below code, didn't seem to do anything: 
# print("What will you fight with?")
# fight_with = input("\n> ")
# dave.fight(fight_with)

#Possible options for adding item/s to inventory - as per ChatGPT suggestions:  
#my_item = Item("Sword", "A sharp blade")
#my_character.set_inventory([my_item]) # Adds an item to inventory
#my_character.set_inventory(["Sword", "Shield"])  # Strings as items

# Create current room plus interaction with the character in the room
current_room = kitchen
while dead == False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    # Added 'talk' and 'fight' instructions to the string so that these appear in the console for the player to read
    print("Which direction would you like to go? North, east, south, west \n Or would you rather 'talk' or 'fight'?")
    command = input("\n> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None and isinstance(inhabitant, Friend):
            inhabitant.talk()
            print("Do you need a hug?")
            hug_with = input()
            if hug_with =="yes": # need to fix this
                 inhabitant.hug 
            else:
                 print("No worries, stay safe and hope you find what you are looking for.")
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            inhabitant.show_inventory() # DOES NOT WORK - need to fix line 33-34 in character file!!!
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                # What happens if you lose?
                print("Oh dear, you lost the fight.")
                dead = True
        else:
            print("There is no one here to fight with \n Which direction would you like to go? North, east, south, west")
