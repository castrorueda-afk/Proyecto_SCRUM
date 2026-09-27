from clientes import registrar_cliente

def mostrar_menu():
    print("\nSISTEMA DE GESTIÓN - GIMNASIO FORCETECH")
    print("1. Registrar nuevo cliente")
    print("2. Control de aforo / Registrar asistencia")
    print("3. Consultar servicios")
    print("4. Generar reporte de clientes")
    print("5. Salir")

def ejecutar_sistema():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n[+] Opción 1: Ejecutando registro de cliente...")
            
        elif opcion == "2":
            print("\n[+] Opción 2: Control de aforo seleccionado...")

        elif opcion == "3":
            print("\n[+] Opción 3: Consultando servicios...")
            
        elif opcion == "4":
            print("\n[+] Opción 4: Generando reporte...")
            
        elif opcion == "5":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("\n[!] Opción inválida. Selecciona un número entre 1 y 5.")
if __name__ == "__main__":
    ejecutar_sistema()