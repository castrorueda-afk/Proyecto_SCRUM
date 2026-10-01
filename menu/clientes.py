import json
import os
from clientes import buscar_cliente_por_id

buscar_cliente_por_id()
DB_FILE = "database.json"

def cargar_datos():
    if not os.path.exists(DB_FILE):
        return {"clientes": []}
    try:
        with open(DB_FILE, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if not contenido.strip():
                return {"clientes": []}
            return json.loads(contenido)
    except json.JSONDecodeError:
        return {"clientes": []}

def guardar_datos(datos):
    with open(DB_FILE, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def registrar_cliente():
    print("\n REGISTRO DE NUEVO CLIENTE (FORCETECH) ")
    
    while True:
        id_cliente = input("Ingrese el ID del cliente (solo números): ").strip()
        if id_cliente.isdigit():
            break
        else:
            print(" Error: Solo se permiten números para el ID. Intente de nuevo.")

    while True:
        nombre = input("Ingrese el nombre completo (solo letras): ").strip()
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print(" Error: El nombre solo debe contener letras. Intente de nuevo.")

    estado = input("Ingrese el estado (Ej: Activo / Inactivo): ").strip()
    riesgo = input("Ingrese el nivel de riesgo (Bajo / Medio / Alto): ").strip()
    
    datos = cargar_datos()
    
    nuevo_cliente = {
        "id": id_cliente,
        "nombre": nombre,
        "estado": estado,
        "riesgo": riesgo
    }
    
    datos["clientes"].append(nuevo_cliente)

    guardar_datos(datos)
    print("\nÉxito, Cliente registrado y guardado en el archivo JSON con éxito.")

def ver_prioridad():
    datos = cargar_datos()
    clientes = datos.get("clientes", [])
    
    print("\n LISTA DE CLIENTES Y ESTADOS ")
    if not clientes:
        print("No hay clientes registrados todavía.")
        return
        
    for c in clientes:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Estado: {c['estado']} | Riesgo: {c['riesgo']}")
        def ver_prioridad():
            datos = cargar_datos()
            clientes = datos.get("clientes", [])
    
    print("\n LISTA DE CLIENTES Y ESTADOS ")
    if not clientes:
        print("No hay clientes registrados todavía.")
        return
        
    for c in clientes:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Estado: {c['estado']} | Riesgo: {c['riesgo']}")

def buscar_cliente_por_id():
    """Busca y muestra un cliente usando su ID."""
    datos = cargar_datos()
    clientes = datos.get("clientes", [])

    id_busqueda = input("Escribe el ID del cliente que quieres buscar: ").strip()

    for cliente in clientes:
        if str(cliente.get("id", "")) == id_busqueda:
            print("\nCLIENTE ENCONTRADO")
            print(f"ID: {cliente.get('id', 'Sin ID')}")
            print(f"Nombre: {cliente.get('nombre', 'Sin nombre')}")
            print(f"Estado: {cliente.get('estado', 'Sin estado')}")
            print(f"Riesgo: {cliente.get('riesgo', 'Sin riesgo')}")
            return

    print(f"No se encontró un cliente con el ID {id_busqueda}.")

