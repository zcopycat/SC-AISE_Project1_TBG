# Important imports 
from room import Room
from character import Enemy 

# Add a truth condition to ...?
dead = False

# Setting up the rooms  
kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room()
ballroom.set_name("ballroom")
ballroom.set_description("A big oval shaped room decorated with baroque style golden ornamentation and mirrors")

dining_hall = Room()
dining_hall.set_name("dining hall")
dining_hall.set_description("A candle-lit room with stone floors, wooden furniture, and a fire place")

# Linking rooms to each other 
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

# Creating the instance of good old Dave 
dave = Enemy("Dave", "A smelly zombie")

# Putting Dave in the dining hall
dining_hall.set_character(dave)

# Setting Dave's convo + fight
dave.set_conversation("Hi my name is Dave. How about I eat your brain?")
dave.set_weakness("beer")
dave.set_inventory("beer")
dave.steal("beer")
print("What will fight with?")
fight_with = input("\n> ")
dave.fight(fight_with)

# Create current room plus interaction with the character in the room
current_room = kitchen
while dead == False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Which direction would you like to go? North, east, south, west")
    command = input("\n> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
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
            print("There is no one here to fight with")
