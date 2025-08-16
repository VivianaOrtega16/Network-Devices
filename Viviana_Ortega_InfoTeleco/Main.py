from RouterMain import router_menu
from GatewayMain import gateway_menu
from SwitchMain import switch_menu
from ModemMain import modem_menu

def main_menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Administrar Router")
        print("2. Administrar Gateway")
        print("3. Administrar Switch")
        print("4. Administrar Módem")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            router_menu()
        elif opcion == "2":
            gateway_menu()
        elif opcion == "3":
            switch_menu()
        elif opcion == "4":
            modem_menu()
        elif opcion == "0":
            print("Cerrando aplicación...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main_menu()
