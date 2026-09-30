
from funciones import (
    ver_clases_asignadas,
    registrar_asistencia,
    registrar_evaluacion,
    ver_asistencias
)


def menu_instructor(id_instructor):
    """Muestra el menú de opciones del instructor."""

    while True:
        print("\n" + "=" * 55)
        print("PANEL DEL INSTRUCTOR - FORCETECH".center(55))
        print("=" * 55)

        print("1. Ver mis clases y clientes asignados")
        print("2. Registrar asistencia")
        print("3. Evaluar progreso físico")
        print("4. Ver historial de asistencias")
        print("0. Volver")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            ver_clases_asignadas(id_instructor)

        elif opcion == "2":
            registrar_asistencia(id_instructor)

        elif opcion == "3":
            registrar_evaluacion(id_instructor)

        elif opcion == "4":
            ver_asistencias(id_instructor)

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")

        input("\nPresiona Enter para continuar...")