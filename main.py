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

from character import Enemy 

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrhaargh... rghlaar... brains...")
dave.set_weakness("beer")

dining_hall.set_character(dave)

current_room = kitchen
while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        
    command = input("> ")
    current_room = current_room.move(command)

    #The code runs and would let move to south but then stuck between ballroom and dining rooms
    # The code not giving any conversation, i.e., no option for convo/fight inputs