# this is the import of all class
from Repeater import Repeater
from Gateway import Gateway
from Modem import Modem
from Switch import Switch
from Router import Router

# --- Example Usage ---

# Create an instance of the Repeater class.
rep1 = Repeater("Rep1", "Cisco", "RP234234", 125.2)

# Print the initial state of the repeater.
rep1.display_info()
# Turn the repeater on.
rep1.turn_on()
# Connect the repeater to the network.
rep1.connect()
# Set new values for speed and signal strength using the setters.
rep1.speed = 100.0
rep1.signal_strength = 70.0

# Print the final state of the repeater to see the changes.
rep1.display_info()

#----example of modem
# Crear un objeto de tipo Modem
modem_cisco = Modem(
    device_name="Modem_Viviana",
    manufacturer="Cisco Systems",
    model="DPC3928",
    connection_type="Cable",
    max_download_speed=200.0,
    max_upload_speed=20.0,
    signal_strength=-50,  # en dB
    frequency_range=( 88 , 108)  # en MHz
)

# Encender el módem
modem_cisco.is_on = True
modem_cisco.is_online = True

# Mostrar la información completa del módem
print(modem_cisco.display_info())

# Probar métodos únicos
print(modem_cisco.modulate("Hola Mundo"))
print(modem_cisco.demodulate("Señal Analógica"))
print(modem_cisco.check_signal())


# Reiniciar la conexión
modem_cisco.reset_connection()

# ===== Crear un objeto Switch =====
switch_hp = Switch(
    device_name="Switch_Viviana",
    manufacturer="HP",
    model="2530-24G",
    num_ports=24,
    switching_capacity=56.0,  # Gbps
    port_speed="1Gbps"
)

# Encender el switch y conectarlo
switch_hp.is_on = True
switch_hp.is_online = True

# Mostrar información del switch
print(switch_hp.display_info())

# Aprender direcciones MAC
switch_hp.learn_mac_address("AA:BB:CC:DD:EE:01", 5)
switch_hp.learn_mac_address("AA:BB:CC:DD:EE:02", 10)

# Ver tabla MAC
switch_hp.show_mac_table()

# Reenviar trama
switch_hp.forward_frame("AA:BB:CC:DD:EE:01")
switch_hp.forward_frame("FF:FF:FF:FF:FF:FF")  # MAC desconocida → broadcast

# Crear VLAN
switch_hp.create_vlan(10)
switch_hp.create_vlan(20)



# ==== 1. CREAR EL GATEWAY ====
gateway1 = Gateway(
    device_name="Gateway_Viviana",
    manufacturer="Cisco",
    model="GW-9000",
    supported_protocols=["IPv4", "IPv6", "TCP/IP"],
    max_connections=3,
    security_features=["NAT"]
)

print("\n===== INFO INICIAL DEL GATEWAY =====")
print(gateway1.display_info())

# ==== 2. ENCENDER Y CONECTAR ====
print("\n===== CONECTANDO EL GATEWAY =====")
gateway1.turn_on()
gateway1.connect()

# ==== 3. AÑADIR Y MOSTRAR RUTAS ====
print("\n===== CONFIGURANDO RUTAS =====")
gateway1.add_route("192.168.1.0/24", "10.0.0.1")
gateway1.add_route("2001:db8::/32", "fe80::1")
gateway1.show_routes()

# ==== 4. TRADUCCIÓN DE PROTOCOLOS ====
print("\n===== TRADUCCIÓN DE PROTOCOLOS =====")
print(gateway1.translate_protocol("Paquete1", "IPv4", "IPv6"))
print(gateway1.translate_protocol("Paquete2", "IPv6", "TCP/IP"))
print(gateway1.translate_protocol("Paquete3", "IPv4", "MPLS"))  # Protocolo no soportado

# ==== 5. FUNCIONES DE SEGURIDAD ====
print("\n===== GESTIÓN DE SEGURIDAD =====")
gateway1.enable_security("Firewall")
gateway1.enable_security("VPN")
gateway1.disable_security("NAT")   # Quitamos NAT
print(gateway1.display_info())

# ==== 6. CONEXIONES ACTIVAS =====
print("\n===== SIMULANDO CONEXIONES =====")
gateway1.open_connection()
gateway1.open_connection()
gateway1.open_connection()
gateway1.open_connection()  # debería fallar, pasa el límite
gateway1.close_connection()
gateway1.close_connection()
gateway1.close_connection()
gateway1.close_connection()  # debería avisar que no hay conexiones

# ==== 7. ELIMINAR RUTA =====
print("\n===== ELIMINANDO RUTA =====")
gateway1.remove_route("192.168.1.0/24")
gateway1.remove_route("8.8.8.0/24")  # ruta no existente
gateway1.show_routes()

# ==== 8. SPECIAL FUNCTION =====
print("\n===== FUNCIÓN ESPECIAL =====")
print(gateway1.special_function())

# ==== 9. DESCONECTAR Y APAGAR =====
print("\n===== DESCONECTANDO Y APAGANDO =====")
gateway1.disconnect()
gateway1.turn_off()

from Router import Router

# ==== 1. CREAR EL ROUTER ====
router1 = Router(
    device_name="Router_Viviana",
    manufacturer="Cisco",
    model="XR5000",
    routing_protocols=["OSPF", "RIP"]
)

print("\n===== INFO INICIAL DEL ROUTER =====")
print(router1.display_info())

# ==== 2. ENCENDER Y CONECTAR ====
print("\n===== CONECTANDO EL ROUTER =====")
router1.turn_on()
router1.connect()

# ==== 3. CONFIGURAR INTERFACES ====
print("\n===== CONFIGURANDO INTERFACES =====")
router1.add_interface("Gig0/0", "192.168.1.1")
router1.add_interface("Gig0/1", "10.0.0.1")
router1.add_interface("Gig0/2", "2001:db8::1")   # IPv6
router1.remove_interface("Gig0/3")               # interfaz inexistente

# ==== 4. AÑADIR Y MOSTRAR RUTAS ====
print("\n===== CONFIGURANDO RUTAS =====")
router1.add_route("192.168.1.0/24", "192.168.1.254")
router1.add_route("10.0.0.0/16", "10.0.0.254")
router1.add_route("2001:db8::/32", "2001:db8::2")
router1.show_routes()

# ==== 5. BUSCAR SIGUIENTE SALTO ====
print("\n===== BUSCAR SIGUIENTE SALTO =====")
print("Next hop para 192.168.1.0/24:", router1.find_next_hop("192.168.1.0/24"))
print("Next hop para 8.8.8.0/24:", router1.find_next_hop("8.8.8.0/24"))

# ==== 6. EJECUTAR PROTOCOLO DE ENRUTAMIENTO ====
print("\n===== EJECUTAR OSPF =====")
router1.run_routing_protocol("OSPF")
router1.show_routes()

print("\n===== PROBAR PROTOCOLO NO IMPLEMENTADO =====")
router1.run_routing_protocol("BGP")

# ==== 7. ELIMINAR RUTAS ====
print("\n===== ELIMINANDO RUTAS =====")
router1.remove_route("10.0.0.0/16")
router1.remove_route("172.16.0.0/16")  # inexistente
router1.show_routes()

# ==== 8. MOSTRAR INFO Y LOGS =====
print("\n===== MOSTRAR INFORMACIÓN DEL ROUTER =====")
print(router1.display_info())

print("\n===== LOGS DEL ROUTER =====")
for log in router1.logs:
    print(log)

# ==== 9. SPECIAL FUNCTION =====
print("\n===== FUNCIÓN ESPECIAL =====")
print(router1.special_function())

# ==== 10. DESCONECTAR Y APAGAR =====
print("\n===== DESCONECTANDO Y APAGANDO =====")
router1.disconnect()
router1.turn_off()
