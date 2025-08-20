from NetworkDevice import NetworkDevice
import ipaddress
import datetime


class Router(NetworkDevice):
    def __init__(self, device_name: str, manufacturer: str, model: str,
                 routing_protocols: list):

        super().__init__(device_name, manufacturer, model, "Router")
        self.__routing_table = {}        # { destino: next_hop }
        self.__routing_protocols = routing_protocols
        self.__interfaces = {}           # { nombre: ip }
        self.__logs = []                 # historial de operaciones

    # ====== GETTERS ======
    @property
    def routing_table(self) -> dict:
        return self.__routing_table

    @property
    def routing_protocols(self) -> list:
        return self.__routing_protocols

    @property
    def interfaces(self) -> dict:
        return self.__interfaces

    @property
    def logs(self) -> list:
        return self.__logs

    # ====== SETTERS ======
    @routing_protocols.setter
    def routing_protocols(self, value: list):
        self.__routing_protocols = value

    # ====== MÉTODOS DE CONEXIÓN ======
    def connect(self):
        if self.is_on and not self.is_online:
            self.is_online = True
            self.__log_event("Router conectado a la red.")
            print(f"The {self.device_type} {self.device_name} is connected")
        else:
            print(f"Please turn on the {self.device_type} {self.device_name}")

    def disconnect(self):
        if self.is_on and self.is_online:
            self.is_online = False
            self.__log_event("Router desconectado de la red.")
            print(f"The {self.device_type} {self.device_name} is disconnected")
        else:
            print(f"Please turn on the {self.device_type} {self.device_name}")

    # ====== MÉTODOS ÚNICOS ======
    def add_route(self, destination: str, next_hop: str):
        try:
            ipaddress.ip_network(destination, strict=False)  # valida subred
            ipaddress.ip_address(next_hop)                   # valida IP
            self.__routing_table[destination] = next_hop
            self.__log_event(f"Ruta añadida: {destination} -> {next_hop}")
            print(f"Ruta añadida: {destination} -> {next_hop}")
        except ValueError:
            print("Error: dirección o subred inválida.")

    def remove_route(self, destination: str):
        if destination in self.__routing_table:
            del self.__routing_table[destination]
            self.__log_event(f"Ruta eliminada: {destination}")
            print(f"Ruta eliminada: {destination}")
        else:
            print(f"No existe una ruta para {destination}")

    def show_routes(self):
        if not self.__routing_table:
            print("Tabla de rutas vacía.")
        else:
            for dest, hop in self.__routing_table.items():
                print(f"{dest} -> {hop}")

    def find_next_hop(self, destination: str) -> str:
        return self.__routing_table.get(destination, "Ruta no encontrada")

    def add_interface(self, name: str, ip: str):
        try:
            ipaddress.ip_address(ip)  # valida dirección IP
            self.__interfaces[name] = ip
            self.__log_event(f"Interfaz {name} configurada con IP {ip}")
            print(f"Interfaz {name} configurada con IP {ip}")
        except ValueError:
            print("Error: dirección IP inválida.")

    def remove_interface(self, name: str):
        if name in self.__interfaces:
            del self.__interfaces[name]
            self.__log_event(f"Interfaz {name} eliminada")
            print(f"Interfaz {name} eliminada")
        else:
            print(f"No existe la interfaz {name}")

    # ====== NUEVO: Simulación de protocolo dinámico ======
    def run_routing_protocol(self, protocol: str):
        if protocol not in self.__routing_protocols:
            print(f"Error: protocolo {protocol} no soportado.")
            return
        if protocol.upper() == "OSPF":
            # Simula que descubre redes vecinas
            self.__routing_table["10.10.0.0/16"] = "10.10.0.1"
            self.__routing_table["172.16.0.0/16"] = "172.16.0.1"
            self.__log_event("OSPF ejecutado: rutas dinámicas añadidas.")
            print("OSPF ejecutado: nuevas rutas aprendidas dinámicamente.")
        else:
            print(f"Protocolo {protocol} soportado pero no implementado aún.")

    # ====== MÉTODO SOBREESCRITO ======
    def display_info(self) -> str:
        base_info = super().display_info()
        return (f"{base_info}\n"
                f"Protocolos de enrutamiento: {', '.join(self.__routing_protocols)}\n"
                f"Interfaces configuradas: {self.__interfaces}\n"
                f"Rutas configuradas: {len(self.__routing_table)}\n"
                f"Logs: {len(self.__logs)} eventos registrados")

    # ====== MÉTODO ABSTRACTO IMPLEMENTADO ======
    def special_function(self):
        return "Optimización dinámica de rutas usando métricas de latencia y ancho de banda."

    # ====== MÉTODO PRIVADO PARA LOGS ======
    def __log_event(self, event: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__logs.append(f"[{timestamp}] {event}")
