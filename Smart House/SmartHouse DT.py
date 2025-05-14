class SmartHomeDigitalTwin:
    def __init__(self):
        # Initialize the initial states of devices
        self.light_status = "off"
        self.thermostat_temperature = 22  # Default temperature setting
        self.door_lock_status = "locked"
        self.speaker_status = "on"

    def get_light_status(self):
        self.get_light_status(self.light_status)
        print(f"Light is {self.light_status}")

    def toggle_light(self):
        self.light_status = "on" if self.light_status == "off" else "off"
        print(f"Light is turned {self.light_status}")

    def get_thermostat_status(self):
        self.get_thermostat_status(self.thermostat_temperature)
        print(f"Thermostat is set to {self.thermostat_temperature}")

    def set_temperature(self, temperature):
        self.temperature = temperature
        if self.temperature < 10 or self.temperature > 30:
            print(f"Error: Value is out of range")
        print(f"Temperature set to {self.temperature}")

    def get_door_lock_status(self):
        self.get_door_lock_status(self.door_lock_status)
        print(f"Door is {self.door_lock_status}")

    def toggle_door_lock(self):
        self.toggle_door_lock = (
            "locked" if self.toggle_door_lock == "unlocked" else "unlocked"
        )

    # Additional Device (Smart Speaker) Implementation
    def get_speaker_status(self):
        self.get_speaker_status(self.speaker_status)
        print(f"Speaker is {self.speaker_status}")

    def toggle_speaker(self):
        self.toggle_speaker = "on" if self.toggle_speaker == "off" else "off"
        print(f"Speaker is {self.toggle_speaker}")

    def simulate_user_interractions(self):
        print(self.get_light_status())
        self.toggle_light()
        print(self.get_light_status())

        print(self.get_thermostat_status())
        self.set_temperature(25)
        print(self.get_thermostat_status())

        print(self.get_door_lock_status())
        self.toggle_door_lock()
        print(self.get_door_lock_status())

        print(self.get_speaker_status())
        self.toggle_speaker()
        print(self.get_speaker_status())


SHDT = SmartHomeDigitalTwin()

SHDT.simulate_user_interractions()
