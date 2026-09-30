from clientes import registrar_cliente, ver_prioridad

def mostrar_menu():
    print("   SISTEMA DE GESTIÓN - GIMNASIO FORCETECH   ")
    print("1. Registrar nuevo cliente")
    print("2. Ver clientes, estado y riesgo (Prioridad)")
    print("3. Consultar servicios (Próximamente)")
    print("4. Generar reporte (Próximamente)")
    print("5. Salir del sistema")

def ejecutar_sistema():
    while True:
        mostrar_menu()
        
        opcion = input("\nSelecciona una opción (1-5): ").strip()

        if opcion == "1":
            registrar_cliente()  
            
        elif opcion == "2":
            ver_prioridad()     
            
        elif opcion == "3":
            print("\n[+] Opción 3: Módulo de servicios en desarrollo...")
            
        elif opcion == "4":
            print("\n[+] Opción 4: Módulo de reportes en desarrollo...")
            
        elif opcion == "5":
            print("\n¡Gracias por usar ForceTech! Saliendo del sistema...")
            break
            
        else:
            print("\n[!] Error: Opción inválida. Por favor, ingresa un número entre 1 y 5.")

if __name__ == "__main__":
    ejecutar_sistema()