from item import *

# Create Character (Base) class 
class Character:

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.inventory = []

    # Introduce the character
    def describe(self):
        print(f"{self.name} is here!") #updated to f string
        print(self.description)

    # Set what this character will say when talked to
    def name(self):
        print(self.name)

    def set_conversation(self, conversation):
        self.conversation = conversation

    # Set the inventory 
    def set_inventory(self, inventory):
        self.inventory += inventory

    # Show the item/s added to the character 
    def show_inventory(self):
        if self.inventory:
            print(f"{self.name}'s inventory:")
            for item in self.inventory:
                print(item.name)  # Print the name of each item
        else:
            print(f"{self.name} has no items in their inventory.")

    # Talk to the character
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}") # updated method to f str from #print("[" + self.name + " says]: " + self.conversation)
        else:
          print(f"{self.name} doesn't want to talk to you") 

    # Fight the character 
    def fight(self, combat_item):
        print(f"{self.name} How about we talk this through?")
        return True
    
class Enemy(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False
        
    # Add a new steal method to the Enemy character 
    def steal(self, item):
        if item in self.inventory:
            print(f"You steal from {self.name}")
            self.inventory -= item

    # Add a new steal method to the Enemy character 
class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(f"{self.name} hugs you back!")

    # Could a gift method to the Friend character 
    # def gift(self, item):
    #     if item in self.inventory:
    #         print(f"A gift from {self.name} to you")
    #         self.inventory += item