from NetworkDevice import NetworkDevice
class Repeater(NetworkDevice):
    # The initializer for the Repeater class.
    def __init__(self, device_name:str, manufacturer:str, model:str, speed:float):
        # Call the initializer of the parent class (NetworkDevice) to set up common attributes.
        # It's generally better practice to use `super().__init__(...)` here.
        NetworkDevice.__init__(self, device_name, manufacturer, model, "Repeater")
        # Attributes specific to the Repeater class.
        self.__speed = speed
        self.__signal_strength = 0
        self.__max_speed = speed

    # Properties to get repeater-specific attributes.
    @property
    def max_speed(self) -> float:
        return self.__max_speed

    @property
    def speed(self) -> float:
        return self.__speed

    # Setter for the 'speed' property with validation logic.
    @speed.setter
    def speed(self, value):
        # Ensures the new speed is within a valid range.
        if 0<= value <= self.__max_speed:
            self.__speed = value

    @property
    def signal_strength(self) -> float:
        return self.__signal_strength

    # Setter for the 'signal_strength' property with validation.
    @signal_strength.setter
    def signal_strength(self, value):
        # Ensures signal strength is between 0 and 100.
        if 0<= value <= 100:
            self.__signal_strength = value

    # Provide the required implementation for the 'connect' abstract method.
    def connect(self):
        if self.is_on and not self.is_online:
            self.is_online = True
            print(f"The  {self.device_type} {self.device_name} is connected")
        else:
            print(f"Please turn on the {self.device_type} {self.device_name}")

    # Provide the required implementation for the 'disconnect' abstract method.
    def disconnect(self):
        if self.is_on and self.__is_online:
            self.is_online = False
            print(f"The  {self.device_type} {self.device_name} is disconnected")
        else:
            # This line has the same error.
            print(f"Please turn on the {self.device_type} {self.device_name}")

    # Override the parent's print_info method to add more details.
    def display_info(self):
        # `super().print_info()` calls the parent class's version of the method first.
        super().display_info()
        # Then, print the details specific to the Repeater.
        print(f"\t speed: {self.__speed}, Max speed: {self.__max_speed}")
        print(f"\t signal_strength: {self.__signal_strength}")
