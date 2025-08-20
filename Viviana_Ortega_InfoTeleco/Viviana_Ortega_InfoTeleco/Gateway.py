from NetworkDevice import NetworkDevice

# como hay distintos tipos de gateway , este es particular es un gateway network

class Gateway(NetworkDevice):
    def __init__(self, device_name: str, manufacturer: str, model: str,
                 supported_protocols: list, max_connections: int, security_features: list):
        
        super().__init__(device_name, manufacturer, model, "Network Gateway")
        self.__supported_protocols = supported_protocols          # IPv4, IPv6, TCP/IP
        self.__routing_table = {}                                # Tabla de rutas (destino -> siguiente salto)
        self.__max_connections = max_connections                 # Máx. conexiones simultáneas
        self.__security_features = security_features             # Funciones de seguridad (NAT, firewall, VPN)
        self.__active_connections = 0                            # Contador de conexiones activas

    # ====== GETTERS ======
    @property
    def supported_protocols(self) -> list:
        return self.__supported_protocols

    @property
    def routing_table(self) -> dict:
        return self.__routing_table

    @property
    def max_connections(self) -> int:
        return self.__max_connections

    @property
    def security_features(self) -> list:
        return self.__security_features
    
    @property
    def active_connections(self) -> int:
        return self.__active_connections

    # ====== METODOS DE CONEXION ======
    def connect(self):
        if self.is_on and not self.is_online:
            self.is_online = True
            print(f"{self.device_type} '{self.device_name}' conectado a la red.")
        else:
            print(f"Por favor encienda el {self.device_type} '{self.device_name}'.")

    def disconnect(self):
        if self.is_on and self.is_online:
            self.is_online = False
            self.__active_connections = 0
            print(f"{self.device_type} '{self.device_name}' desconectado de la red.")
        else:
            print(f"El {self.device_type} '{self.device_name}' ya estaba apagado o desconectado.")

    # ====== METODOS UNICOS DEL GATEWAY ======
    def translate_protocol(self, packet: str, from_protocol: str, to_protocol: str) -> str:
        
        if from_protocol in self.__supported_protocols and to_protocol in self.__supported_protocols:
            return f"Traduciendo paquete '{packet}' de {from_protocol} a {to_protocol}."
        return "Error: protocolo no soportado por este Gateway."

    def add_route(self, destination: str, next_hop: str):
        
        self.__routing_table[destination] = next_hop
        print(f"Ruta añadida: {destination} -> {next_hop}")

    def remove_route(self, destination: str):
        
        if destination in self.__routing_table:
            del self.__routing_table[destination]
            print(f"Ruta eliminada: {destination}")
        else:
            print(f"No existe una ruta para {destination}")

    def show_routes(self):
        
        if not self.__routing_table:
            print("Tabla de rutas vacia")
        else:
            print("Tabla de rutas:")
            for dest, hop in self.__routing_table.items():
                print(f"   {dest} ➝ {hop}")

    def enable_security(self, feature: str):
        
        if feature not in self.__security_features:
            self.__security_features.append(feature)
            print(f"Función de seguridad '{feature}' activada.")

    def disable_security(self, feature: str):
        
        if feature in self.__security_features:
            self.__security_features.remove(feature)
            print(f"Función de seguridad '{feature}' desactivada.")

    def open_connection(self):
        """Simula la apertura de una conexión a través del Gateway."""
        if self.__active_connections < self.__max_connections:
            self.__active_connections += 1
            print(f"Conexion establecida. Total activas: {self.__active_connections}")
        else:
            print("Límite de conexiones alcanzado. No se puede abrir mas.")

    def close_connection(self):
        """Simula el cierre de una conexión."""
        if self.__active_connections > 0:
            self.__active_connections -= 1
            print(f"Conexion cerrada. Total activas: {self.__active_connections}")
        else:
            print("No hay conexiones activas para cerrar.")

    # ====== MÉTODO SOBREESCRITO ======
    def display_info(self) -> str:
        base_info = super().display_info()
        return (f"{base_info}\n"
                f"Protocolos soportados: {', '.join(self.__supported_protocols)}\n"
                f"Max. conexiones: {self.__max_connections}\n"
                f"Conexiones activas: {self.__active_connections}\n"
                f"Funciones de seguridad activas: {', '.join(self.__security_features)}\n"
                f"Rutas configuradas: {len(self.__routing_table)}")

    # ====== MÉTODO ESPECIAL ======
    def special_function(self):
        return "Balanceo dinámico de tráfico entre múltiples enlaces WAN (Multi-WAN Gateway)."

