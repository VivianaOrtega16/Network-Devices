from Router import Router

def router_menu():
    router = None

    while True:
        print("\n===== MENÚ ROUTER =====")
        print("1. Crear Router")
        print("2. Encender Router")
        print("3. Apagar Router")
        print("4. Conectar Router")
        print("5. Desconectar Router")
        print("6. Añadir ruta")
        print("7. Eliminar ruta")
        print("8. Mostrar tabla de rutas")
        print("9. Buscar siguiente salto")
        print("10. Añadir interfaz")
        print("11. Eliminar interfaz")
        print("12. Mostrar información")
        print("13. Ejecutar protocolo de enrutamiento")
        print("14. Ver logs")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            router = Router(
                device_name=input("Nombre del router: "),
                manufacturer=input("Fabricante: "),
                model=input("Modelo: "),
                routing_protocols=input("Protocolos de enrutamiento (separados por coma): ").split(",")
            )
            print("Router creado correctamente.")

        elif router is None and opcion != "0":
            print("Primero debe crear un router (opción 1).")

        elif opcion == "2":
            router.turn_on()

        elif opcion == "3":
            router.turn_off()

        elif opcion == "4":
            router.connect()

        elif opcion == "5":
            router.disconnect()

        elif opcion == "6":
            dest = input("Destino (ej. 192.168.1.0/24): ")
            hop = input("Siguiente salto (ej. 192.168.1.254): ")
            router.add_route(dest, hop)

        elif opcion == "7":
            dest = input("Destino a eliminar: ")
            router.remove_route(dest)

        elif opcion == "8":
            router.show_routes()

        elif opcion == "9":
            dest = input("Destino a buscar: ")
            print("Next hop:", router.find_next_hop(dest))

        elif opcion == "10":
            name = input("Nombre de la interfaz (ej. Gig0/0): ")
            ip = input("IP de la interfaz: ")
            router.add_interface(name, ip)

        elif opcion == "11":
            name = input("Nombre de la interfaz a eliminar: ")
            router.remove_interface(name)

        elif opcion == "12":
            print(router.display_info())

        elif opcion == "13":
            proto = input("Protocolo de enrutamiento: ")
            router.run_routing_protocol(proto)

        elif opcion == "14":
            for log in router.logs:
                print(log)

        elif opcion == "0":
            print("Saliendo del menú Router...")
            break
        else:
            print("Opción inválida.")

# 🔹 Este bloque asegura que el menú se ejecute si corres este archivo directamente
if __name__ == "__main__":
    router_menu()
