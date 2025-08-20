from Switch import Switch

def switch_menu():
    switch = None

    while True:
        print("\n===== MENÚ SWITCH =====")
        print("1. Crear Switch")
        print("2. Encender Switch")
        print("3. Apagar Switch")
        print("4. Conectar Switch")
        print("5. Desconectar Switch")
        print("6. Aprender dirección MAC")
        print("7. Reenviar trama")
        print("8. Crear VLAN")
        print("9. Mostrar VLANs")
        print("10. Mostrar tabla MAC")
        print("11. Mostrar información")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            switch = Switch(
                device_name=input("Nombre del switch: "),
                manufacturer=input("Fabricante: "),
                model=input("Modelo: "),
                num_ports=int(input("Número de puertos: ")),
                switching_capacity=float(input("Capacidad de conmutación (Gbps): ")),
                port_speed=input("Velocidad de puertos (ej. 1Gbps): ")
            )
            print("Switch creado correctamente.")

        elif switch is None and opcion != "0":
            print("Primero debe crear un switch (opción 1).")

        elif opcion == "2":
            switch.turn_on()

        elif opcion == "3":
            switch.turn_off()

        elif opcion == "4":
            switch.connect()

        elif opcion == "5":
            switch.disconnect()

        elif opcion == "6":
            mac = input("Dirección MAC (ej. AA:BB:CC:DD:EE:FF): ")
            port = int(input("Puerto: "))
            switch.learn_mac_address(mac, port)

        elif opcion == "7":
            mac_destino = input("MAC de destino: ")
            switch.forward_frame(mac_destino)

        elif opcion == "8":
            vlan_id = int(input("ID de VLAN: "))
            switch.create_vlan(vlan_id)

        elif opcion == "9":
            print("VLANs soportadas:", switch.vlans_supported)

        elif opcion == "10":
            switch.show_mac_table()

        elif opcion == "11":
            print(switch.display_info())

        elif opcion == "0":
            print("Saliendo del menú Switch...")
            break
        else:
            print("Opción inválida.")

# 🔹 Este bloque asegura que se ejecute el menú si corres este archivo directamente
if __name__ == "__main__":
    switch_menu()
