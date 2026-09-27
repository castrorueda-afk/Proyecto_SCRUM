from funciones import (
    ver_clases_asignadas,
    registrar_asistencia,
    registrar_evaluacion,
    ver_asistencias
)


def menu_instructor(id_instructor):

    while True:

        print("\n===== PANEL DEL INSTRUCTOR =====")
        print("1. Ver mis clases y clientes")
        print("2. Registrar asistencia")
        print("3. Evaluar progreso físico")
        print("4. Ver historial de asistencias")
        print("0. Volver")

        opcion = input(
            "Seleccione una opción: "
        ).strip()

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

        input("\nPresione Enter para continuar...")