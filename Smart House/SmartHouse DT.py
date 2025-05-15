import random
class SmartHomeDigitalTwin:
    def __init__(self):
        # Initialize the initial states of devices
        self.light_status = "off"
        self.thermostat_temperature = 22  # Default temperature setting
        self.door_lock_status = "locked"
        self.speaker_status = "on"

    def get_light_status(self):
        if self.light_status:
            print(f"Light is {self.light_status}")

    def toggle_light(self):
        self.light_status = "on" if self.light_status == "off" else "off"
        print(f"Light is turned {self.light_status}")

    def set_temperature(self, temperature):
        self.temperature = temperature
        if self.temperature < 10 or self.temperature > 30:
            print(f"Warning: Extreme Temperature")
        print(f"Temperature set to {self.temperature}")

    def get_thermostat_status(self):
        if self.thermostat_temperature:
            print(f"Thermostat is set to {self.thermostat_temperature}")

    def get_door_lock_status(self):
        if self.door_lock_status:
            print(f"Door is {self.door_lock_status}")

    def toggle_door_lock(self):
        self.door_lock_status = "unlocked" if self.door_lock_status == "locked" else "locked"
        print(f"Door is now {self.door_lock_status}")

    # Additional Device (Smart Speaker) Implementation
    def get_speaker_status(self):
        if self.speaker_status:
            print(f"Speaker is {self.speaker_status}")

    def toggle_speaker(self):
        self.speaker_status = "off" if self.speaker_status == "on" else "on"
        print(f"Speaker is {self.speaker_status}")

    def simulate_user_interractions(self, no_of_interractions):
        for i in range(no_of_interractions):
            self.get_light_status()
            self.toggle_light()
            self.set_temperature(temperature=random.randint(9, 32))
            self.get_thermostat_status()
            self.get_door_lock_status()
            self.toggle_door_lock()
            self.get_speaker_status()
            self.toggle_speaker()

SHDT = SmartHomeDigitalTwin()

SHDT.simulate_user_interractions(4)
