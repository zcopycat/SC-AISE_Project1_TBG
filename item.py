class Item:
    def __init__(self):
        self.name = None
        self.description = None
        # self.value = None
        # self.quantity = None

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name
    
    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.description = item_description

    def describe_item(self):
        print(self.description)

    # def get_item_value(self):
    #     return self.value
    
    # def set_item_value(self, item_value):
    #     self.value = item_value

    # def get_quantity(self):
    #     return self.quantity
    
    # def set_quantity(self, item_quantity):
    #     self.quantity = item_quantity