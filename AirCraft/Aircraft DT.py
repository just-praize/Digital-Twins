import random

class AircraftEngine:
    def __init__(self, Initial_Temperature):
        self.Temperature = Initial_Temperature

    def Simulate_Engine_Operation(self):
        Temperature_Change = random.uniform(-10, 20)
        self.Temperature += Temperature_Change

    def Get_Temperature(self):
        return self.Temperature


class AircraftDigitalTwin:
    def __init__(self, Engine):
        self.Engine = Engine

    def Monitor_Engine(self, No_of_iterations):
        for i in range(No_of_iterations):
            self.Engine.Simulate_Engine_Operation()
            Current_Temperature = self.Engine.Get_Temperature()
            print(f"Aircraft Engine Temperature in Celcius: {Current_Temperature}")


AE = AircraftEngine(Initial_Temperature=290)

ADT = AircraftDigitalTwin(Engine=AE)

ADT.Monitor_Engine(No_of_iterations=10)
