"""Vistas de reportes y seguimiento de progreso para ForceTech."""
from datetime import date

from clientes import cargar_datos, guardar_datos
from matriculas import matricula_vigente


# Un progreso igual o inferior a este porcentaje aparece como bajo rendimiento.
UMBRAL_BAJO_RENDIMIENTO = 40


def _obtener_datos():
    """Carga el JSON y agrega listas vacías para los módulos del gimnasio."""
    datos = cargar_datos()

    for clave in (
        "clientes",
        "servicios",
        "instructores",
        "matriculas",
        "progresos",
    ):
        datos.setdefault(clave, [])

    return datos


def _buscar(registros, identificador):
    """Busca un elemento del catálogo sin importar si el ID es texto o número."""
    return next(
        (
            item for item in registros
            if str(item.get("id")) == str(identificador)
        ),
        None,
    )


def _ultimo_progreso(datos, id_cliente):
    """Devuelve el registro más reciente de progreso para un cliente."""
    historial = [
        item for item in datos["progresos"]
        if str(item.get("id_cliente")) == str(id_cliente)
    ]

    return max(
        historial,
        key=lambda item: item.get("fecha", ""),
        default=None,
    )


def mostrar_clientes_inscritos():
    """Muestra cada matrícula activa con el cliente, servicio e instructor."""
    datos = _obtener_datos()
    activas = [
        matricula for matricula in datos["matriculas"]
        if matricula_vigente(matricula)
    ]

    print("\nCLIENTES INSCRITOS")

    if not activas:
        print("No hay clientes con matrículas activas.")
        return

    for matricula in activas:
        cliente = _buscar(datos["clientes"], matricula.get("id_cliente"))
        servicio = _buscar(datos["servicios"], matricula.get("id_servicio"))
        instructor = _buscar(datos["instructores"], matricula.get("id_instructor"))

        nombre_cliente = (
            cliente.get("nombre", "Desconocido")
            if cliente else "Desconocido"
        )
        nombre_servicio = (
            servicio.get("nombre", "Desconocido")
            if servicio else "Desconocido"
        )
        nombre_instructor = (
            instructor.get("nombre", "Desconocido")
            if instructor else "Desconocido"
        )

        print(
            f"- {nombre_cliente} | {nombre_servicio} "
            f"| Instructor: {nombre_instructor} "
            f"| Inicio: {matricula.get('fecha_inicio', 'Sin fecha')} "
            f"| Duración: {matricula.get('duracion_semanas', '?')} semanas"
        )


def mostrar_servicios_y_capacidad():
    """Muestra servicios, capacidad máxima y cupos ocupados."""
    datos = _obtener_datos()
    print("\nSERVICIOS Y CAPACIDAD")

    if not datos["servicios"]:
        print("No hay servicios registrados.")
        return

    for servicio in datos["servicios"]:
        ocupados = sum(
            1
            for matricula in datos["matriculas"]
            if str(matricula.get("id_servicio")) == str(servicio.get("id"))
            and matricula_vigente(matricula)
        )

        capacidad = servicio.get("capacidad", 0)

        print(
            f"- {servicio.get('nombre', 'Sin nombre')} "
            f"| Estado: {servicio.get('estado', 'Activo')} "
            f"| Cupos: {ocupados}/{capacidad}"
        )


def mostrar_instructores_activos():
    """Muestra solo los instructores cuyo estado es activo."""
    datos = _obtener_datos()

    activos = [
        instructor for instructor in datos["instructores"]
        if str(instructor.get("estado", "Activo")).strip().lower() == "activo"
    ]

    print("\nINSTRUCTORES ACTIVOS")

    if not activos:
        print("No hay instructores activos registrados.")
        return

    for instructor in activos:
        print(
            f"- ID {instructor.get('id')}: "
            f"{instructor.get('nombre', 'Sin nombre')}"
        )


def registrar_progreso():
    """Guarda una medición porcentual para un cliente existente."""
    datos = _obtener_datos()
    print("\nREGISTRAR PROGRESO")

    if not datos["clientes"]:
        print("No hay clientes registrados.")
        return

    for cliente in datos["clientes"]:
        print(f"ID {cliente.get('id')}: {cliente.get('nombre', 'Sin nombre')}")

    id_cliente = input("ID del cliente: ").strip()
    cliente = _buscar(datos["clientes"], id_cliente)

    if cliente is None:
        print("No existe un cliente con ese ID.")
        return

    while True:
        texto = input("Progreso alcanzado (0 a 100 %): ").strip()

        try:
            porcentaje = float(texto.replace(",", "."))
            if 0 <= porcentaje <= 100:
                break
        except ValueError:
            pass

        print("Escribe un porcentaje entre 0 y 100.")

    observacion = input("Observación (opcional): ").strip()

    datos["progresos"].append({
        "id_cliente": str(cliente["id"]),
        "fecha": date.today().isoformat(),
        "porcentaje": porcentaje,
        "observacion": observacion,
    })

    guardar_datos(datos)
    print("Progreso guardado.")


def mostrar_riesgo_y_bajo_rendimiento():
    """Lista clientes con riesgo alto o progreso bajo el umbral definido."""
    datos = _obtener_datos()
    print("\nCLIENTES EN RIESGO O CON BAJO RENDIMIENTO")
    encontrados = 0

    for cliente in datos["clientes"]:
        progreso = _ultimo_progreso(datos, cliente.get("id"))
        riesgo_alto = (
            str(cliente.get("riesgo", "")).strip().lower() == "alto"
        )

        porcentaje = (
            float(progreso["porcentaje"])
            if progreso else None
        )

        rendimiento_bajo = (
            porcentaje is not None
            and porcentaje <= UMBRAL_BAJO_RENDIMIENTO
        )

        if riesgo_alto or rendimiento_bajo:
            encontrados += 1
            motivos = []

            if riesgo_alto:
                motivos.append("riesgo alto")

            if rendimiento_bajo:
                motivos.append(f"progreso {porcentaje:g}%")

            print(
                f"- {cliente.get('nombre', 'Sin nombre')}: "
                f"{', '.join(motivos)}"
            )

    if encontrados == 0:
        print("No hay clientes que cumplan estos criterios.")

    print(
        f"Criterio de bajo rendimiento: "
        f"progreso <= {UMBRAL_BAJO_RENDIMIENTO}%."
    )


def mostrar_progreso_consolidado():
    """Resume el progreso más reciente de cada cliente y su cambio."""
    datos = _obtener_datos()
    print("\nPROGRESO CONSOLIDADO")

    if not datos["clientes"]:
        print("No hay clientes registrados.")
        return

    for cliente in datos["clientes"]:
        historial = sorted(
            [
                progreso for progreso in datos["progresos"]
                if str(progreso.get("id_cliente")) == str(cliente.get("id"))
            ],
            key=lambda item: item.get("fecha", ""),
        )

        if not historial:
            print(
                f"- {cliente.get('nombre', 'Sin nombre')}: "
                "sin mediciones."
            )
            continue

        ultimo = historial[-1]
        anterior = historial[-2] if len(historial) > 1 else None

        if anterior:
            cambio = (
                float(ultimo["porcentaje"])
                - float(anterior["porcentaje"])
            )
            tendencia = f"cambio {cambio:+g} puntos porcentuales"
        else:
            tendencia = "primera medición"

        print(
            f"- {cliente.get('nombre', 'Sin nombre')}: "
            f"{float(ultimo['porcentaje']):g}% "
            f"el {ultimo.get('fecha', 'sin fecha')} ({tendencia})"
        )

        if ultimo.get("observacion"):
            print(f"  Observación: {ultimo['observacion']}")


def mostrar_menu_reportes():
    """Presenta el menú de vistas de reportes y ejecuta la opción elegida."""
    opciones = {
        "1": mostrar_clientes_inscritos,
        "2": mostrar_servicios_y_capacidad,
        "3": mostrar_instructores_activos,
        "4": mostrar_riesgo_y_bajo_rendimiento,
        "5": mostrar_progreso_consolidado,
    }

    while True:
        print("\nREPORTES")
        print("1. Clientes inscritos")
        print("2. Servicios y capacidad")
        print("3. Instructores activos")
        print("4. Clientes en riesgo o bajo rendimiento")
        print("5. Progreso consolidado")
        print("0. Volver")

        opcion = input("Elige un reporte: ").strip()

        if opcion == "0":
            return

        funcion = opciones.get(opcion)

        if funcion:
            funcion()
        else:
            print("Opción inválida.")