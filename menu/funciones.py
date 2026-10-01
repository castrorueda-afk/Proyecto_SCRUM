import os
import json
from datetime import date


DB_FILE = "database.json"


def cargar_datos():

    if not os.path.exists(DB_FILE):
        return {
            "clientes": [],
            "servicios": [],
            "instructores": [],
            "matriculas": [],
            "asistencias": [],
            "progresos": []
        }

    try:

        with open(DB_FILE, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        datos.setdefault("clientes", [])
        datos.setdefault("servicios", [])
        datos.setdefault("instructores", [])
        datos.setdefault("matriculas", [])
        datos.setdefault("asistencias", [])
        datos.setdefault("progresos", [])

        return datos

    except json.JSONDecodeError:

        print("Error: database.json tiene un formato incorrecto.")

        return {
            "clientes": [],
            "servicios": [],
            "instructores": [],
            "matriculas": [],
            "asistencias": [],
            "progresos": []
        }


def guardar_datos(datos):

    with open(DB_FILE, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def buscar_por_id(lista, id_buscado):

    for elemento in lista:

        if str(elemento.get("id")) == str(id_buscado):
            return elemento

    return None


def ver_clases_asignadas(id_instructor):

    datos = cargar_datos()

    instructor = buscar_por_id(
        datos["instructores"],
        id_instructor
    )

    if instructor is None:
        print("No se encontró el instructor.")
        return

    print("\n===== MIS CLASES ASIGNADAS =====")

    print("Instructor:", instructor["nombre"])

    encontro = False

    for matricula in datos["matriculas"]:

        if str(matricula["id_instructor"]) != str(id_instructor):
            continue

        if matricula["estado"] != "Activa":
            continue

        cliente = buscar_por_id(
            datos["clientes"],
            matricula["id_cliente"]
        )

        servicio = buscar_por_id(
            datos["servicios"],
            matricula["id_servicio"]
        )

        if cliente and servicio:

            print("\nCliente:", cliente["nombre"])
            print("Servicio:", servicio["nombre"])
            print("Fecha de inicio:", matricula["fecha_inicio"])
            print(
                "Duración:",
                matricula["duracion_semanas"],
                "semanas"
            )

            encontro = True

    if not encontro:
        print("No tienes clientes asignados.")


def registrar_asistencia(id_instructor):

    datos = cargar_datos()

    instructor = buscar_por_id(
        datos["instructores"],
        id_instructor
    )

    if instructor is None:
        print("No se encontró el instructor.")
        return

    print("\n===== REGISTRAR ASISTENCIA =====")
    print("Instructor:", instructor["nombre"])

    clientes_asignados = []

    for matricula in datos["matriculas"]:

        if str(matricula["id_instructor"]) == str(id_instructor):

            if matricula["estado"] == "Activa":

                cliente = buscar_por_id(
                    datos["clientes"],
                    matricula["id_cliente"]
                )

                if cliente:
                    clientes_asignados.append(cliente)

    if not clientes_asignados:

        print("No tienes clientes asignados.")
        return

    print("\nClientes asignados:")

    for cliente in clientes_asignados:

        print(
            f"ID: {cliente['id']} | "
            f"Nombre: {cliente['nombre']}"
        )

    id_cliente = input(
        "\nIngrese el ID del cliente: "
    ).strip()

    cliente = buscar_por_id(
        clientes_asignados,
        id_cliente
    )

    if cliente is None:

        print(
            "Ese cliente no está asignado "
            "a este instructor."
        )

        return

    print("\n1. Presente")
    print("2. Ausente")

    opcion = input("Seleccione: ").strip()

    if opcion == "1":

        estado = "Presente"

    elif opcion == "2":

        estado = "Ausente"

    else:

        print("Opción inválida.")
        return

    asistencia = {
        "id_cliente": str(cliente["id"]),
        "id_instructor": str(id_instructor),
        "fecha": date.today().isoformat(),
        "estado": estado
    }

    datos["asistencias"].append(asistencia)

    guardar_datos(datos)

    print("\nAsistencia registrada correctamente.")


def registrar_evaluacion(id_instructor):

    datos = cargar_datos()

    instructor = buscar_por_id(
        datos["instructores"],
        id_instructor
    )

    if instructor is None:

        print("No se encontró el instructor.")
        return

    print("\n===== EVALUAR PROGRESO =====")

    clientes_asignados = []

    for matricula in datos["matriculas"]:

        if str(matricula["id_instructor"]) == str(id_instructor):

            if matricula["estado"] == "Activa":

                cliente = buscar_por_id(
                    datos["clientes"],
                    matricula["id_cliente"]
                )

                if cliente:
                    clientes_asignados.append(cliente)

    if not clientes_asignados:

        print("No tienes clientes asignados.")
        return

    for cliente in clientes_asignados:

        print(
            f"ID: {cliente['id']} | "
            f"Nombre: {cliente['nombre']}"
        )

    id_cliente = input(
        "\nIngrese el ID del cliente: "
    ).strip()

    cliente = buscar_por_id(
        clientes_asignados,
        id_cliente
    )

    if cliente is None:

        print("Cliente no encontrado.")
        return

    try:

        porcentaje = float(
            input("Porcentaje de progreso (0-100): ")
        )

    except ValueError:

        print("Debe ingresar un número.")
        return

    if porcentaje < 0 or porcentaje > 100:

        print("El porcentaje debe estar entre 0 y 100.")
        return

    observacion = input(
        "Observación: "
    ).strip()

    progreso = {
        "id_cliente": str(cliente["id"]),
        "id_instructor": str(id_instructor),
        "fecha": date.today().isoformat(),
        "porcentaje": porcentaje,
        "observacion": observacion
    }

    datos["progresos"].append(progreso)

    guardar_datos(datos)

    print("\nEvaluación registrada correctamente.")


def ver_asistencias(id_instructor):

    datos = cargar_datos()

    print("\n===== HISTORIAL DE ASISTENCIAS =====")

    encontro = False

    for asistencia in datos["asistencias"]:

        if str(asistencia["id_instructor"]) == str(id_instructor):

            cliente = buscar_por_id(
                datos["clientes"],
                asistencia["id_cliente"]
            )

            if cliente:

                print(
                    f"Cliente: {cliente['nombre']} | "
                    f"Fecha: {asistencia['fecha']} | "
                    f"Estado: {asistencia['estado']}"
                )

                encontro = True

    if not encontro:

        print("No hay asistencias registradas.")