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
    #Renamed metod as 'say_name' as causing a conflict with the self.name attribute (ChatGPT suggestion)
    def say_name(self): 
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
                #print(item.name)  # Print the name of each item (error?) - 'str' object has no attribute 'name'
                # tried replacing the above with item.describe_item() but something still missing in the code
                #ChatGPT suggested fix below
                # If 'item' is an object, print item.name. If it's a string, print it directly.
                if hasattr(item, 'name'):
                    print(item.name)
                else:
                    print(item)  # Print the string item directly
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
    # ChatGPT suggested the following code for the above so that it would still have a default implementation from the Character class.
    # def fight(self, combat_item):
    #     print(f"{self.name} doesn't want to fight!")
    #     return False
    
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
            self.inventory -= item # ChatGPT suggested rewriting using remove method: self.inventory.remove(item)

    # Add a new steal method to the Enemy character 
class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(f"{self.name} hugs you back!")

    # Could a gift method to the Friend character - ChatGPT suggested to re-write as below:
    # def gift(self, item):
    #   if item not in self.inventory:
    #       print(f"{self.name} doesn't have that item to give!")
    #   else:
    #       print(f"A gift from {self.name} to you: {item}")
    #       self.inventory.remove(item)  # Removes the item from the friend's inventory
        # Here, ChatGPT suggests I would need to add the item to the recipient's inventory