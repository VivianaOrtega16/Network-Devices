from NetworkDevice import NetworkDevice

class Modem(NetworkDevice):
    def __init__(self, device_name: str, manufacturer: str, model: str, connection_type: str,
                 max_download_speed: float, max_upload_speed: float, signal_strength: int,
                 frequency_range: tuple):
        
        super().__init__(device_name, manufacturer, model, "Modem")
        self.__connection_type = connection_type
        self.__max_download_speed = max_download_speed
        self.__max_upload_speed = max_upload_speed
        self.__signal_strength = signal_strength
        self.__frequency_range = frequency_range

    # ====== GETTERS ======
    @property
    def connection_type(self) -> str:
        return self.__connection_type

    @property
    def max_download_speed(self) -> float:
        return self.__max_download_speed

    @property
    def max_upload_speed(self) -> float:
        return self.__max_upload_speed

    @property
    def signal_strength(self) -> int:
        return self.__signal_strength

    @property
    def frequency_range(self) -> tuple:
        return self.__frequency_range

    # ====== SETTERS ======
    @connection_type.setter
    def connection_type(self, value: str):
        self.__connection_type = value

    @max_download_speed.setter
    def max_download_speed(self, value: float):
        self.__max_download_speed = value

    @max_upload_speed.setter
    def max_upload_speed(self, value: float):
        self.__max_upload_speed = value

    @signal_strength.setter
    def signal_strength(self, value: int):
        self.__signal_strength = value

    @frequency_range.setter
    def frequency_range(self, value: tuple):
        self.__frequency_range = value
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

    # ====== unique methods ======
    def modulate(self, data: str) -> str:
        return f"Modulando datos '{data}' en señal analógica usando {self.__connection_type}."

    def demodulate(self, signal: str) -> str:
        return f"Demodulando señal '{signal}' a datos digitales."

    def check_signal(self) -> str:
        return f"Intensidad de señal: {self.__signal_strength} dB"

    def reset_connection(self):
        self.is_online = False
        print("Reiniciando conexión con el ISP...")
        self.is_online = True
        print("Conexión restablecida.")
        
    # Override the parent's print_info method to add more details.
    def display_info(self):
        
        super().display_info()
        # Then, print the details specific to the modem
        
        print(f"\t signal_strength: {self.__signal_strength}")
        print(f"\t Tipo de conexión: {self.__connection_type}")
        print(f"\t Velocidad descarga: {self.__max_download_speed} Mbps")
        print(f"\t Velocidad subida: {self.__max_upload_speed} Mbps")
        print(f"\t Intensidad señal: {self.__signal_strength} dB")
        print(f"\t Rango de frecuencia: {self.__frequency_range}")



    
