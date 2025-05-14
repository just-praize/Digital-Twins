import random


class ConveyorBelt:
    def __init__(self, lenght=10):
        self.length = lenght
        self.products_on_belt = []

    def add_product(self, product):
        if len(self.products_on_belt) < self.length:
            self.products_on_belt.append(product)
            print(f"product {product} is added to the conveyor belt")
        else:
            print(f"Conveyor belt is full. Unable to add {product}")

    def move_belt(self):
        if self.products_on_belt:
            moved_product = self.products_on_belt.pop(0)
            print(f"Product {moved_product} moved along the conveyor belt")
        else:
            print("Conveyor belt is empty")


class ManufacturingDigitalTwin:
    def __init__(self, conveyor_belt):
        self.conveyor_belt = conveyor_belt

    def simulate_production(self, number_steps=8):
        for i in range(number_steps):
            random_product = f"Product-{random.randint(1, 100)}"
            self.conveyor_belt.add_product(random_product)
            self.conveyor_belt.move_belt()


conveyor_belt = ConveyorBelt(lenght=8)
manufacturing_twin = ManufacturingDigitalTwin(conveyor_belt=conveyor_belt)
manufacturing_twin.simulate_production()
