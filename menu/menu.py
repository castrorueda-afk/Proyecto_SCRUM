"""Menú de consola del sistema ForceTech."""
import sys
from pathlib import Path

# Agrega la carpeta principal del proyecto a la ruta de Python.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from clientes import registrar_cliente
from matriculas import (
    registrar_instructor,
    registrar_matricula,
    registrar_servicio,
)
from reportes import (
    mostrar_menu_reportes,
    mostrar_servicios_y_capacidad,
    registrar_progreso,
)


def _menu_catalogos():
    """Permite cargar los servicios y los instructores."""
    while True:
        print("\nADMINISTRAR CATÁLOGOS")
        print("1. Registrar servicio")
        print("2. Registrar instructor")
        print("0. Volver")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_servicio()
        elif opcion == "2":
            registrar_instructor()
        elif opcion == "0":
            return
        else:
            print("Opción inválida.")


def mostrar_menu():
    """Muestra las acciones disponibles en el sistema."""
    print("\nSISTEMA DE GESTIÓN - GIMNASIO FORCETECH")
    print("1. Registrar nuevo cliente")
    print("2. Control de aforo / Registrar asistencia")
    print("3. Consultar servicios y cupos")
    print("4. Crear matrícula")
    print("5. Ver reportes")
    print("6. Registrar progreso de cliente")
    print("7. Registrar servicios o instructores")
    print("8. Salir")


def ejecutar_sistema():
    """Lee la opción del usuario y llama la función correspondiente."""
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-8): ").strip()

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            print("\nControl de aforo todavía no está implementado.")
        elif opcion == "3":
            mostrar_servicios_y_capacidad()
        elif opcion == "4":
            registrar_matricula()
        elif opcion == "5":
            mostrar_menu_reportes()
        elif opcion == "6":
            registrar_progreso()
        elif opcion == "7":
            _menu_catalogos()
        elif opcion == "8":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break
            
        else:
            print("\nOpción inválida. Selecciona un número entre 1 y 8.")


if __name__ == "__main__":
    ejecutar_sistema()