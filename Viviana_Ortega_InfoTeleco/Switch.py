from NetworkDevice import NetworkDevice
class Switch(NetworkDevice):
    def __init__(self, device_name: str, manufacturer: str, model: str,
                 num_ports: int, switching_capacity: float, port_speed: str):
        
        super().__init__(device_name, manufacturer, model, "Switch")
        self.__num_ports = num_ports
        self.__switching_capacity = switching_capacity
        self.__mac_address_table = {}
        self.__vlans_supported = []
        self.__port_speed = port_speed

    # ====== GETTERS ======
    @property
    def num_ports(self) -> int:
        return self.__num_ports

    @property
    def switching_capacity(self) -> float:
        return self.__switching_capacity

    @property
    def mac_address_table(self) -> dict:
        return self.__mac_address_table

    @property
    def vlans_supported(self) -> list:
        return self.__vlans_supported

    @property
    def port_speed(self) -> str:
        return self.__port_speed

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

    # ====== SETTERS ======
    @num_ports.setter
    def num_ports(self, value: int):
        self.__num_ports = value

    @switching_capacity.setter
    def switching_capacity(self, value: float):
        self.__switching_capacity = value

    @port_speed.setter
    def port_speed(self, value: str):
        self.__port_speed = value

    # ====== MÉTODOS ÚNICOS ======
    def learn_mac_address(self, mac: str, port: int):
        if port > self.__num_ports or port < 1:
            print(f"Error: Puerto {port} inválido.")
            return
        self.__mac_address_table[mac] = port
        print(f"MAC {mac} aprendida en puerto {port}.")

    def forward_frame(self, mac_destino: str):
        if mac_destino in self.__mac_address_table:
            port = self.__mac_address_table[mac_destino]
            print(f"Enviando trama a puerto {port}.")
        else:
            print("MAC desconocida, enviando trama a todos los puertos (broadcast).")

    def create_vlan(self, vlan_id: int):
        if vlan_id not in self.__vlans_supported:
            self.__vlans_supported.append(vlan_id)
            print(f"VLAN {vlan_id} creada.")
        else:
            print(f"VLAN {vlan_id} ya existe.")

    def show_mac_table(self):
        if not self.__mac_address_table:
            print("Tabla MAC vacía.")
        else:
            for mac, port in self.__mac_address_table.items():
                print(f"{mac} -> Puerto {port}")

    # ====== MÉTODO SOBREESCRITO ======
    def display_info(self) -> str:
        base_info = super().display_info()
        return (f"{base_info}\n"
                f"Número de puertos: {self.__num_ports}\n"
                f"Capacidad de conmutación: {self.__switching_capacity} Gbps\n"
                f"Velocidad por puerto: {self.__port_speed}\n"
                f"VLANs soportadas: {self.__vlans_supported}\n"
                f"Entradas en tabla MAC: {len(self.__mac_address_table)}")

    # ====== MÉTODO ABSTRACTO IMPLEMENTADO ======
    def special_function(self):
        return "Priorización automática de tráfico según tipo de servicio (QoS)."
 