from Gateway import Gateway

def gateway_menu():
    gateway = None

    while True:
        print("\n===== MENU GATEWAY =====")
        print("1. Crear Gateway")
        print("2. Encender Gateway")
        print("3. Apagar Gateway")
        print("4. Conectar Gateway")
        print("5. Desconectar Gateway")
        print("6. Añadir ruta")
        print("7. Eliminar ruta")
        print("8. Mostrar tabla de rutas")
        print("9. Traducir protocolo")
        print("10. Habilitar seguridad")
        print("11. Deshabilitar seguridad")
        print("12. Mostrar información")
        print("0. Salir")
        
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            gateway = Gateway(
                device_name=input("Nombre del gateway: "),
                manufacturer=input("Fabricante: "),
                model=input("Modelo: "),
                supported_protocols=input("Protocolos soportados (separados por coma): ").split(","),
                max_connections=int(input("Numero máximo de conexiones: ")),
                security_features=input("Funciones de seguridad iniciales (separadas por coma): ").split(",")
            )
            print("Gateway creado correctamente.")

        elif gateway is None and opcion != "0":
            print("Primero debe crear un gateway (opcion 1).")

        elif opcion == "2":
            gateway.turn_on()

        elif opcion == "3":
            gateway.turn_off()

        elif opcion == "4":
            gateway.connect()

        elif opcion == "5":
            gateway.disconnect()

        elif opcion == "6":
            dest = input("Destino (ej. 10.0.0.0/24): ")
            hop = input("Siguiente salto: ")
            gateway.add_route(dest, hop)

        elif opcion == "7":
            dest = input("Destino a eliminar: ")
            gateway.remove_route(dest)

        elif opcion == "8":
            gateway.show_routes()

        elif opcion == "9":
            packet = input("Paquete a traducir: ")
            from_proto = input("De protocolo: ")
            to_proto = input("A protocolo: ")
            print(gateway.translate_protocol(packet, from_proto, to_proto))

        elif opcion == "10":
            feature = input("Funcion de seguridad a habilitar: ")
            gateway.enable_security(feature)

        elif opcion == "11":
            feature = input("Funcion de seguridad a deshabilitar: ")
            gateway.disable_security(feature)

        elif opcion == "12":
            print(gateway.display_info())

        elif opcion == "0":
            print("Saliendo del menu Gateway...")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    gateway_menu()
