class WareHouse:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.inventory = {}

    def add_inventory(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f"{item} added to inventory: {quantity}")

    def remove_inventory(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            print(
                f"{item} removed from inventory: {quantity}... Remainder: {self.inventory[item]}"
            )
        else:
            print("Error: Not enough in Inventory to fulfil order")


WH = WareHouse("Ferrol", 1000)

WH.add_inventory("Arduino Boards", 75)

WH.remove_inventory("Arduino Boards", 10)
