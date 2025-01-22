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
    command = input("> ")
    current_room = current_room.move(command)
    break