from room import Room

kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room ("dining hall")

kitchen.set_description("A dank and dirty room buzzing with flies")
kitchen.describe()

ballroom.set_description("An big oval shaped room decorated with baroque style golden ornaments and mirrors")
ballroom.describe()

dining_hall.set_description("A candle-lit room with stone floors, wooden furniture, and a fire place")
dining_hall.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")