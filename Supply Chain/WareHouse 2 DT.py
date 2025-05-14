class Truck:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.cargo = {}

    def load_cargo(self, item, quantity):
        if sum(self.cargo.values()) <= self.capacity:
            if item in self.cargo:
                self.cargo[item] += quantity
            else:
                self.cargo[item] = quantity
            print(f"{item} loaded to truck.. Quantity: {quantity}")
        else:
            print("Error: Not enough capacity to load cargo")

    def unload_cargo(self, item, quantity):
        if item in self.cargo and self.cargo[item] >= quantity:
            self.cargo[item] -= quantity
            print(f"{item} unloaded from truck... Quantity: {quantity}")
        else:
            print("Error: Cannot fulfil order")

    def move_to(self, location):
        self.location = location
        print(f"Package moved to {location}")


T = Truck("Tenerife", 200)

T.load_cargo("Lambourghini", 69)

T.move_to("Ibiza")

T.unload_cargo("Lambourghini", 30)
