#PRIMER TRABAJO INFORMATICA PARA TELECOMUNICACIONES
# Import the tools needed to create an Abstract Base Class (ABC)
from abc import ABC, abstractmethod

# Define an abstract base class 'NetworkDevice'. It serves as a template for other device classes.
# It cannot be instantiated
class NetworkDevice(ABC):
    # The initializer method of NetworkDevice
    def __init__(self, device_name:str, manufacturer:str, model:str, device_type:str):
        # A single underscore `_` conventionally means this attribute is protected and two underscores __ private.
        self.__device_name = device_name
        self.__manufacturer = manufacturer
        self.__model = model
        self.__device_type = device_type
        self.__is_online = False
        self.__is_on = False

    # The @property decorator turns a method into a read-only attribute.
    # This allows you to get self._device_type by simply calling `my_device.device_type`.
    @property
    def device_type(self) -> str:
        return self.__device_type

    @property
    def device_name(self) -> str:
        return self.__device_name

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @property
    def model(self) -> str:
        return self.__model

    @property
    def is_on(self):
        return self.__is_on

    @property
    def is_online(self):
        return self.__is_online

    # The @setter decorator allows you to define logic for when a property's value is set.
    # This enables controlled writing to the attribute.
    #setter
    @manufacturer.setter
    def manufacturer(self, value: str):
        if not value.strip():
            raise ValueError("El fabricante no puede estar vacío.")
        self.__manufacturer = value

    @model.setter
    def model(self, value: str):
        if not value.strip():
            raise ValueError("El modelo no puede estar vacío.")
        self.__model = value

    @device_type.setter
    def device_type(self, value: str):
        if not value.strip():
            raise ValueError("El tipo de dispositivo no puede estar vacío.")
        self.__device_type = value

    @is_online.setter
    def is_online(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("is_online debe ser un valor booleano.")
        self.__is_online = value

    @is_on.setter
    def is_on(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("is_on debe ser un valor booleano.")
        self.__is_on = value
    # An @abstractmethod must be implemented by any concrete subclass that inherits from NetworkDevice.
    # It defines a contract that subclasses must follow.
    @abstractmethod
    def connect(self):
        # 'pass' means this method has no implementation in the base class so it should be implemented by sub-classes
        pass

    @abstractmethod
    def disconnect(self):
        pass

    # A concrete method that is inherited by all subclasses.
    def turn_on(self):
        # Turns the device on if it is currently off.
        if not self.__is_on:
            self.__is_on = True

    def turn_off(self):
        # Turns the device off if it is currently on.
        if self.__is_on:
            self.__is_on = False

    # A concrete method to print the device's information. Subclasses can extend this.
    def display_info(self):
        print("*********************")
        print(f"\t name {self.device_name}, type {self.device_type}")
        print(f"\t manufacturer {self.manufacturer}")
        print(f"\t model {self.model}")
        print(f"\t isOn {self.is_on}")
        print(f"\t isOnline {self.is_online}")

  



