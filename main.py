from room import Room

kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room()
ballroom.set_name("ballroom")
ballroom.set_description("A big oval shaped room decorated with baroque style golden ornamentation and mirrors")

dining_hall = Room()
dining_hall.set_name("dining hall")
dining_hall.set_description("A candle-lit room with stone floors, wooden furniture, and a fire place")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

        command = input("> ")
        current_room = current_room.move(command)
        break

from character import Enemy # If removeing the break in the above block of code, Code is unreachable Pylance - 

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrhaargh... rghlaar... brains...")
dave.set_weakness("beer")
dining_hall.set_character(dave)

# Note on Code is unreachable: Exception error (??)
# If you're calling a function that we know is going to never return, it means the code after that can't be analysed.
# Ref: https://github.com/microsoft/pylance-release/issues/2981