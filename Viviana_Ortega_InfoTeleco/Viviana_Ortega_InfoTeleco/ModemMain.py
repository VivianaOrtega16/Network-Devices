from Modem import Modem

def modem_menu():
    modem = None

    while True:
        print("\n===== MENÚ MÓDEM =====")
        print("1. Crear Módem")
        print("2. Encender Módem")
        print("3. Apagar Módem")
        print("4. Conectar Módem")
        print("5. Desconectar Módem")
        print("6. Modulación de datos")
        print("7. Demodulación de señal")
        print("8. Revisar intensidad de señal")
        print("9. Reiniciar conexión")
        print("10. Mostrar información")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            modem = Modem(
                device_name=input("Nombre del módem: "),
                manufacturer=input("Fabricante: "),
                model=input("Modelo: "),
                connection_type=input("Tipo de conexión (ADSL, Fibra, Cable, etc.): "),
                max_download_speed=float(input("Velocidad máxima de descarga (Mbps): ")),
                max_upload_speed=float(input("Velocidad máxima de subida (Mbps): ")),
                signal_strength=int(input("Intensidad de señal (dB): ")),
                frequency_range=tuple(map(int, input("Rango de frecuencia (ej. 50 1000): ").split()))
            )
            print("Módem creado correctamente.")

        elif modem is None and opcion != "0":
            print("Primero debe crear un módem (opción 1).")

        elif opcion == "2":
            modem.turn_on()

        elif opcion == "3":
            modem.turn_off()

        elif opcion == "4":
            modem.connect()

        elif opcion == "5":
            modem.disconnect()

        elif opcion == "6":
            data = input("Ingrese los datos a modular: ")
            print(modem.modulate(data))

        elif opcion == "7":
            signal = input("Ingrese la señal a demodular: ")
            print(modem.demodulate(signal))

        elif opcion == "8":
            print(modem.check_signal())

        elif opcion == "9":
            modem.reset_connection()

        elif opcion == "10":
            modem.display_info()

        elif opcion == "0":
            print("Saliendo del menú Módem...")
            break

        else:
            print("Opción inválida.")

# 🔹 Este bloque asegura que el menú se ejecute si corres este archivo directamente
if __name__ == "__main__":
    modem_menu()
