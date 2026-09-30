"""Panel del instructor de ForceTech."""
import json
import os
from datetime import date

DB_FILE = "database.json"


from clientes import cargar_datos, guardar_datos
from matriculas import matricula_vigente


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
    
    except (json.JSONDecodeError, IOError):
        print("Error al cargar los datos. Se utilizarán datos vacíos.")
        return {
            "clientes": [],
            "servicios": [],
            "instructores": [],
            "matriculas": [],
            "asistencias": [],
            "progresos": []
        }


def _buscar_por_id(registros, identificador):
    """Busca un registro por su ID."""
    return next(
        (
            registro
            for registro in registros
            if str(registro.get("id")) == str(identificador)
        ),
        None,
    )




def obtener_clientes_asignados(id_instructor):
    """Devuelve los clientes asignados al instructor."""
    datos = cargar_datos()

    clientes = []

    for matricula in datos["matriculas"]:
        if (
            str(matricula.get("id_instructor")) == str(id_instructor)
            and matricula_vigente(matricula)
        ):
            cliente = _buscar_por_id(
                datos["clientes"],
                matricula.get("id_cliente")
            )

            if cliente and cliente not in clientes:
                clientes.append(cliente)

    return clientes


def registrar_asistencia(id_instructor):
    """Registra la asistencia de un cliente asignado."""
    datos = cargar_datos()

    clientes = obtener_clientes_asignados(id_instructor)

    print("\n" + "=" * 55)
    print("REGISTRAR ASISTENCIA".center(55))
    print("=" * 55)

    if not clientes:
        print("No tienes clientes asignados.")
        return

    print("\nCLIENTES ASIGNADOS:")

    for cliente in clientes:
        print(
            f"ID {cliente.get('id')}: "
            f"{cliente.get('nombre', 'Sin nombre')}"
        )

    id_cliente = input("\nIngrese el ID del cliente: ").strip()

    cliente = _buscar_por_id(clientes, id_cliente)

    if cliente is None:
        print("El cliente no está asignado a este instructor.")
        return

    print("\n1. Presente")
    print("2. Ausente")

    opcion = input("Seleccione una opción: ").strip()

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

    print(
        f"\nAsistencia registrada para "
        f"{cliente['nombre']}: {estado}."
    )


def registrar_evaluacion(id_instructor):
    """Registra una evaluación del progreso físico del cliente."""
    datos = cargar_datos()

    clientes = obtener_clientes_asignados(id_instructor)

    print("\n" + "=" * 55)
    print("EVALUACIÓN DEL PROGRESO FÍSICO".center(55))
    print("=" * 55)

    if not clientes:
        print("No tienes clientes asignados.")
        return

    print("\nCLIENTES ASIGNADOS:")

    for cliente in clientes:
        print(
            f"ID {cliente.get('id')}: "
            f"{cliente.get('nombre', 'Sin nombre')}"
        )

    id_cliente = input("\nIngrese el ID del cliente: ").strip()

    cliente = _buscar_por_id(clientes, id_cliente)

    if cliente is None:
        print("El cliente no está asignado a este instructor.")
        return

    while True:
        entrada = input(
            "Ingrese el progreso físico (0 a 100 %): "
        ).strip()

        try:
            porcentaje = float(entrada.replace(",", "."))

            if 0 <= porcentaje <= 100:
                break

        except ValueError:
            pass

        print("Error: ingrese un número entre 0 y 100.")

    observacion = input(
        "Observación sobre el progreso: "
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

    print(
        f"\nEvaluación registrada correctamente "
        f"para {cliente['nombre']}."
    )


def ver_asistencias(id_instructor):
    """Muestra las asistencias registradas por el instructor."""
    datos = cargar_datos()

    asistencias = [
        asistencia
        for asistencia in datos["asistencias"]
        if str(asistencia.get("id_instructor")) == str(id_instructor)
    ]

    print("\n" + "=" * 55)
    print("HISTORIAL DE ASISTENCIAS".center(55))
    print("=" * 55)

    if not asistencias:
        print("No hay asistencias registradas.")
        return

    for asistencia in asistencias:
        cliente = _buscar_por_id(
            datos["clientes"],
            asistencia.get("id_cliente")
        )

        nombre = (
            cliente.get("nombre", "Desconocido")
            if cliente else "Desconocido"
        )

        print(
            f"\nCliente: {nombre}"
            f"\nFecha: {asistencia.get('fecha')}"
            f"\nEstado: {asistencia.get('estado')}"
        )