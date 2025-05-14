class Store:
    def __init__(self, location, inventory):
        self.location = location
        self.inventory = inventory

    def place_order(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            print(f"Order for {item} has been fulfiled")
        else:
            print("Could not fulfil order")


S = Store("prague", {"Durex Condoms": 69})

S.place_order("Durex Condoms", 79)
