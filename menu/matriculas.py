"""Matrículas y catálogos básicos para el sistema ForceTech.

Los datos se guardan en el mismo database.json que usa clientes.py.
"""
from datetime import date, timedelta

from clientes import cargar_datos, guardar_datos


def _obtener_datos():
    """Lee el JSON y asegura que existan las listas de este módulo."""
    datos = cargar_datos()
    for clave in ("clientes", "servicios", "instructores", "matriculas"):
        datos.setdefault(clave, [])
    return datos


def _siguiente_id(registros):
    """Devuelve un identificador numérico consecutivo como texto."""
    ids = [
        int(item["id"])
        for item in registros
        if str(item.get("id", "")).isdigit()
    ]
    return str(max(ids, default=0) + 1)


def _pedir_numero_positivo(mensaje):
    """Pide un número entero mayor que cero y repite si es inválido."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("Error: escribe un número entero mayor que cero.")


def _buscar_por_id(registros, identificador):
    """Encuentra un registro por su ID, comparando como texto."""
    return next(
        (
            item for item in registros
            if str(item.get("id")) == identificador
        ),
        None,
    )


def matricula_vigente(matricula):
    """Indica si la matrícula sigue dentro de su duración y está activa."""
    if matricula.get("estado") != "Activa":
        return False

    try:
        inicio = date.fromisoformat(matricula["fecha_inicio"])
        semanas = int(matricula["duracion_semanas"])
        fin = inicio + timedelta(weeks=semanas)
        return inicio <= date.today() <= fin
    except (KeyError, TypeError, ValueError):
        # Conserva como activa una matrícula antigua sin fechas completas.
        return True


def registrar_servicio():
    """Agrega al catálogo un servicio con su capacidad máxima."""
    datos = _obtener_datos()
    print("\nREGISTRAR SERVICIO")

    nombre = input("Nombre del servicio: ").strip()
    if not nombre:
        print("El nombre no puede quedar vacío.")
        return

    capacidad = _pedir_numero_positivo("Capacidad máxima: ")

    servicio = {
        "id": _siguiente_id(datos["servicios"]),
        "nombre": nombre,
        "capacidad": capacidad,
        "estado": "Activo",
    }

    datos["servicios"].append(servicio)
    guardar_datos(datos)
    print(f"Servicio '{nombre}' guardado con ID {servicio['id']}.")


def registrar_instructor():
    """Agrega al catálogo un instructor activo."""
    datos = _obtener_datos()
    print("\nREGISTRAR INSTRUCTOR")

    nombre = input("Nombre completo del instructor: ").strip()
    if not nombre:
        print("El nombre no puede quedar vacío.")
        return

    instructor = {
        "id": _siguiente_id(datos["instructores"]),
        "nombre": nombre,
        "estado": "Activo",
    }

    datos["instructores"].append(instructor)
    guardar_datos(datos)
    print(f"Instructor '{nombre}' guardado con ID {instructor['id']}.")


def _mostrar_opciones(registros, titulo):
    """Imprime IDs y nombres para ayudar a elegir un registro."""
    print(f"\n{titulo}")
    for registro in registros:
        print(f"ID {registro['id']}: {registro['nombre']}")


def _pedir_fecha_inicio():
    """Valida que la fecha de inicio use el formato AAAA-MM-DD."""
    while True:
        texto = input("Fecha de inicio (AAAA-MM-DD): ").strip()
        try:
            return date.fromisoformat(texto).isoformat()
        except ValueError:
            print("Fecha inválida. Ejemplo correcto: 2026-10-15.")


def registrar_matricula():
    """Asigna un cliente activo a un servicio e instructor."""
    datos = _obtener_datos()

    clientes = [
        item for item in datos["clientes"]
        if str(item.get("estado", "")).strip().lower() == "activo"
    ]

    servicios = [
        item for item in datos["servicios"]
        if str(item.get("estado", "Activo")).strip().lower() == "activo"
    ]

    instructores = [
        item for item in datos["instructores"]
        if str(item.get("estado", "Activo")).strip().lower() == "activo"
    ]

    if not clientes:
        print("No hay clientes activos registrados.")
        return

    if not servicios:
        print("No hay servicios activos. Registra un servicio primero.")
        return

    if not instructores:
        print("No hay instructores activos. Registra un instructor primero.")
        return

    _mostrar_opciones(clientes, "CLIENTES ACTIVOS")
    id_cliente = input("ID del cliente: ").strip()
    cliente = _buscar_por_id(clientes, id_cliente)

    if cliente is None:
        print("No existe un cliente activo con ese ID.")
        return

    _mostrar_opciones(servicios, "SERVICIOS ACTIVOS")
    id_servicio = input("ID del servicio: ").strip()
    servicio = _buscar_por_id(servicios, id_servicio)

    if servicio is None:
        print("No existe un servicio activo con ese ID.")
        return

    capacidad = int(servicio.get("capacidad", 0))

    ocupados = sum(
        1
        for matricula in datos["matriculas"]
        if str(matricula.get("id_servicio")) == str(servicio["id"])
        and matricula_vigente(matricula)
    )

    if capacidad > 0 and ocupados >= capacidad:
        print("El servicio ya alcanzó su capacidad máxima.")
        return

    duplicada = any(
        str(matricula.get("id_cliente")) == str(cliente["id"])
        and str(matricula.get("id_servicio")) == str(servicio["id"])
        and matricula_vigente(matricula)
        for matricula in datos["matriculas"]
    )

    if duplicada:
        print("El cliente ya tiene una matrícula activa en ese servicio.")
        return

    _mostrar_opciones(instructores, "INSTRUCTORES ACTIVOS")
    id_instructor = input("ID del instructor: ").strip()
    instructor = _buscar_por_id(instructores, id_instructor)

    if instructor is None:
        print("No existe un instructor activo con ese ID.")
        return

    fecha_inicio = _pedir_fecha_inicio()
    duracion = _pedir_numero_positivo("Duración en semanas: ")

    matricula = {
        "id": _siguiente_id(datos["matriculas"]),
        "id_cliente": str(cliente["id"]),
        "id_servicio": str(servicio["id"]),
        "id_instructor": str(instructor["id"]),
        "fecha_inicio": fecha_inicio,
        "duracion_semanas": duracion,
        "estado": "Activa",
    }

    datos["matriculas"].append(matricula)
    guardar_datos(datos)
    print(f"Matrícula guardada con ID {matricula['id']}.")