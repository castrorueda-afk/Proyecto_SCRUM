"""Reportes y seguimiento del progreso de los clientes de ForceTech."""

from datetime import date

from clientes import cargar_datos, guardar_datos
from matriculas import matricula_vigente


UMBRAL_BAJO_RENDIMIENTO = 40


def _obtener_datos():
    """Carga la información y crea las listas necesarias si no existen."""
    datos = cargar_datos() or {}

    for clave in (
        "clientes",
        "servicios",
        "instructores",
        "matriculas",
        "progresos",
    ):
        datos.setdefault(clave, [])

    return datos


def _buscar_por_id(registros, identificador):
    """Encuentra un registro comparando los IDs como texto."""
    return next(
        (
            registro
            for registro in registros
            if str(registro.get("id")) == str(identificador)
        ),
        None,
    )


def _imprimir_encabezado(titulo):
    """Muestra un título para separar visualmente cada reporte."""
    print(f"\n{'=' * 54}")
    print(f"{titulo.upper():^54}")
    print(f"{'=' * 54}")


def _progreso_mas_reciente(datos, id_cliente):
    """Obtiene la última medición registrada para un cliente."""
    historial = [
        progreso
        for progreso in datos["progresos"]
        if str(progreso.get("id_cliente")) == str(id_cliente)
    ]

    return max(
        historial,
        key=lambda progreso: progreso.get("fecha", ""),
        default=None,
    )


def mostrar_clientes_inscritos():
    """Lista las matrículas que siguen vigentes."""
    datos = _obtener_datos()
    matriculas_activas = [
        matricula
        for matricula in datos["matriculas"]
        if matricula_vigente(matricula)
    ]

    _imprimir_encabezado("Clientes inscritos")

    if not matriculas_activas:
        print("No hay clientes con matrículas activas.")
        return

    for matricula in matriculas_activas:
        cliente = _buscar_por_id(
            datos["clientes"], matricula.get("id_cliente")
        )
        servicio = _buscar_por_id(
            datos["servicios"], matricula.get("id_servicio")
        )
        instructor = _buscar_por_id(
            datos["instructores"], matricula.get("id_instructor")
        )

        nombre_cliente = cliente.get("nombre", "Desconocido") if cliente else "Desconocido"
        nombre_servicio = servicio.get("nombre", "Desconocido") if servicio else "Desconocido"
        nombre_instructor = instructor.get("nombre", "Desconocido") if instructor else "Desconocido"

        print(f"\n• {nombre_cliente}")
        print(f"  Servicio:   {nombre_servicio}")
        print(f"  Instructor: {nombre_instructor}")
        print(f"  Inicio:     {matricula.get('fecha_inicio', 'Sin fecha')}")
        print(
            f"  Duración:   "
            f"{matricula.get('duracion_semanas', '?')} semanas"
        )


def mostrar_servicios_y_capacidad():
    """Muestra la ocupación actual de cada servicio."""
    datos = _obtener_datos()
    _imprimir_encabezado("Servicios y capacidad")

    if not datos["servicios"]:
        print("No hay servicios registrados.")
        return

    for servicio in datos["servicios"]:
        matriculas_del_servicio = [
            matricula
            for matricula in datos["matriculas"]
            if str(matricula.get("id_servicio")) == str(servicio.get("id"))
            and matricula_vigente(matricula)
        ]

        capacidad = servicio.get("capacidad", 0)
        print(f"\n• {servicio.get('nombre', 'Sin nombre')}")
        print(f"  Estado: {servicio.get('estado', 'Activo')}")
        print(f"  Cupos:  {len(matriculas_del_servicio)}/{capacidad}")


def mostrar_instructores_activos():
    """Presenta los instructores cuyo estado está marcado como activo."""
    datos = _obtener_datos()
    instructores = [
        instructor
        for instructor in datos["instructores"]
        if str(instructor.get("estado", "Activo")).strip().lower() == "activo"
    ]

    _imprimir_encabezado("Instructores activos")

    if not instructores:
        print("No hay instructores activos registrados.")
        return

    for instructor in instructores:
        print(
            f"• {instructor.get('nombre', 'Sin nombre')} "
            f"(ID: {instructor.get('id', 'Sin ID')})"
        )


def registrar_progreso():
    """Registra una medición de progreso para un cliente."""
    datos = _obtener_datos()
    _imprimir_encabezado("Registrar progreso")

    if not datos["clientes"]:
        print("No hay clientes registrados.")
        return

    print("Clientes:")
    for cliente in datos["clientes"]:
        print(
            f"• ID {cliente.get('id')}: "
            f"{cliente.get('nombre', 'Sin nombre')}"
        )

    id_cliente = input("\nEscribe el ID del cliente: ").strip()
    cliente = _buscar_por_id(datos["clientes"], id_cliente)

    if cliente is None:
        print("No se encontró un cliente con ese ID.")
        return

    while True:
        entrada = input("Progreso alcanzado (0 a 100 %): ").strip()

        try:
            porcentaje = float(entrada.replace(",", "."))
            if 0 <= porcentaje <= 100:
                break
        except ValueError:
            pass

        print("Ingresa un número entre 0 y 100.")

    observacion = input("Observación (opcional): ").strip()

    datos["progresos"].append(
        {
            "id_cliente": str(cliente["id"]),
            "fecha": date.today().isoformat(),
            "porcentaje": porcentaje,
            "observacion": observacion,
        }
    )

    guardar_datos(datos)
    print("El progreso se guardó correctamente.")


def mostrar_riesgo_y_bajo_rendimiento():
    """Muestra clientes con riesgo alto o progreso bajo."""
    datos = _obtener_datos()
    _imprimir_encabezado("Clientes que requieren seguimiento")
    encontrados = 0

    for cliente in datos["clientes"]:
        progreso = _progreso_mas_reciente(datos, cliente.get("id"))
        riesgo_alto = (
            str(cliente.get("riesgo", "")).strip().lower() == "alto"
        )

        try:
            porcentaje = float(progreso["porcentaje"]) if progreso else None
        except (TypeError, ValueError, KeyError):
            porcentaje = None

        progreso_bajo = (
            porcentaje is not None
            and porcentaje <= UMBRAL_BAJO_RENDIMIENTO
        )

        if riesgo_alto or progreso_bajo:
            razones = []

            if riesgo_alto:
                razones.append("riesgo alto")
            if progreso_bajo:
                razones.append(f"progreso de {porcentaje:g}%")

            nombre = cliente.get("nombre", "Sin nombre")
            print(f"• {nombre}: {', '.join(razones)}")
            encontrados += 1

    if encontrados == 0:
        print("No hay clientes que cumplan estos criterios.")

    print(
        "\nSe considera bajo rendimiento un progreso igual o inferior "
        f"a {UMBRAL_BAJO_RENDIMIENTO}%."
    )


def mostrar_progreso_consolidado():
    """Resume la última medición y su cambio frente a la anterior."""
    datos = _obtener_datos()
    _imprimir_encabezado("Progreso consolidado")

    if not datos["clientes"]:
        print("No hay clientes registrados.")
        return

    for cliente in datos["clientes"]:
        historial = sorted(
            (
                progreso
                for progreso in datos["progresos"]
                if str(progreso.get("id_cliente"))
                == str(cliente.get("id"))
            ),
            key=lambda progreso: progreso.get("fecha", ""),
        )

        nombre = cliente.get("nombre", "Sin nombre")

        if not historial:
            print(f"• {nombre}: todavía no tiene mediciones.")
            continue

        ultimo = historial[-1]
        anterior = historial[-2] if len(historial) > 1 else None

        try:
            porcentaje = float(ultimo["porcentaje"])

            if anterior:
                diferencia = porcentaje - float(anterior["porcentaje"])
                detalle = f"cambio de {diferencia:+g} puntos"
            else:
                detalle = "primera medición"
        except (TypeError, ValueError, KeyError):
            print(f"• {nombre}: la medición contiene datos inválidos.")
            continue

        fecha = ultimo.get("fecha", "sin fecha")
        print(f"• {nombre}: {porcentaje:g}% el {fecha} ({detalle})")

        if ultimo.get("observacion"):
            print(f"  Observación: {ultimo['observacion']}")


def mostrar_menu_reportes():
    """Permite elegir y consultar los reportes disponibles."""
    opciones = {
        "1": mostrar_clientes_inscritos,
        "2": mostrar_servicios_y_capacidad,
        "3": mostrar_instructores_activos,
        "4": mostrar_riesgo_y_bajo_rendimiento,
        "5": mostrar_progreso_consolidado,
    }

    while True:
        _imprimir_encabezado("Reportes ForceTech")
        print("1. Clientes inscritos")
        print("2. Servicios y capacidad")
        print("3. Instructores activos")
        print("4. Clientes que requieren seguimiento")
        print("5. Progreso consolidado")
        print("0. Volver")

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "0":
            break

        reporte = opciones.get(opcion)

        if reporte is None:
            print("Opción inválida. Intenta nuevamente.")
            continue

        reporte()
        input("\nPresiona Enter para regresar al menú...")

if __name__ == "__main__":
    mostrar_menu_reportes()